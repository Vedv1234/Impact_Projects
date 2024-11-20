"""
Author: Ved Vyas, Maarifa International Club
Functionality of code: This is my implementation of a safety-focused routing system that helps women 
find the safest route home. It uses historical crime data, lighting information, population density, 
and real-time factors to calculate safety scores for different routes. The system prioritizes safety 
over speed when suggesting routes.
"""

import numpy as np
import pandas as pd
import folium
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import osmnx as ox
import geopandas as gpd
from sklearn.preprocessing import MinMaxScaler

class SafeRouteMapper:
    def __init__(self):
        # Initialize our safety parameters
        self.safety_weights = {
            'crime_rate': 0.4,
            'lighting': 0.2,
            'population_density': 0.2,
            'emergency_services_proximity': 0.1,
            'business_activity': 0.1
        }
        
    def load_crime_data(self, crime_data_path):
        """
        Load and process historical crime data for safety analysis
        """
        self.crime_data = pd.read_csv(crime_data_path)
        # Create a heat map of crime incidents
        self.crime_density = self._calculate_crime_density()
        
    def _calculate_crime_density(self):
        """
        Calculate crime density for each area using kernel density estimation
        """
        from sklearn.neighbors import KernelDensity
        
        # Convert crime locations to a density map
        crime_locations = self.crime_data[['latitude', 'longitude']].values
        kde = KernelDensity(bandwidth=0.01)
        kde.fit(crime_locations)
        
        return kde
    
    def get_street_network(self, location):
        """
        Get street network for the specified location using OSMnx
        """
        self.G = ox.graph_from_place(location, network_type='walk')
        return self.G
    
    def calculate_safety_score(self, node):
        """
        Calculate safety score for a given node based on multiple factors
        """
        location = (self.G.nodes[node]['y'], self.G.nodes[node]['x'])
        
        # Calculate individual safety factors
        crime_score = -self.crime_density.score([[location[0], location[1]]])
        lighting_score = self._get_lighting_score(location)
        population_score = self._get_population_density(location)
        emergency_score = self._get_emergency_services_proximity(location)
        business_score = self._get_business_activity(location)
        
        # Weighted combination of safety factors
        safety_score = (
            crime_score * self.safety_weights['crime_rate'] +
            lighting_score * self.safety_weights['lighting'] +
            population_score * self.safety_weights['population_density'] +
            emergency_score * self.safety_weights['emergency_services_proximity'] +
            business_score * self.safety_weights['business_activity']
        )
        
        return safety_score
    
    def find_safest_route(self, start_point, end_point):
        """
        Find the safest route between two points
        """
        # Convert start and end points to nearest network nodes
        start_node = ox.nearest_nodes(self.G, start_point[1], start_point[0])
        end_node = ox.nearest_nodes(self.G, end_point[1], end_point[0])
        
        # Create safety-weighted graph
        safety_weights = {}
        for u, v, k, data in self.G.edges(keys=True, data=True):
            midpoint = (
                (self.G.nodes[u]['y'] + self.G.nodes[v]['y'])/2,
                (self.G.nodes[u]['x'] + self.G.nodes[v]['x'])/2
            )
            safety_weights[(u, v, k)] = self.calculate_safety_score((midpoint))
            
        # Find safest route using Dijkstra's algorithm with safety weights
        route = nx.shortest_path(
            self.G, 
            start_node, 
            end_node, 
            weight=safety_weights
        )
        
        return route
    
    def visualize_route(self, route):
        """
        Create an interactive map showing the safest route
        """
        # Create base map centered on the route
        center_lat = self.G.nodes[route[0]]['y']
        center_lon = self.G.nodes[route[0]]['x']
        m = folium.Map(location=[center_lat, center_lon], zoom_start=15)
        
        # Add crime heatmap
        self._add_crime_heatmap(m)
        
        # Draw the route
        route_coords = []
        for node in route:
            route_coords.append([self.G.nodes[node]['y'], self.G.nodes[node]['x']])
            
        folium.PolyLine(
            route_coords,
            weight=4,
            color='green',
            opacity=0.8
        ).add_to(m)
        
        return m
    
    def _get_lighting_score(self, location):
        """
        Calculate lighting score based on street lights and time of day
        """
        # This would integrate with city lighting data
        # Placeholder implementation
        return 0.5
    
    def _get_population_density(self, location):
        """
        Get population density score for location
        """
        # This would integrate with census data
        # Placeholder implementation
        return 0.5
    
    def _get_emergency_services_proximity(self, location):
        """
        Calculate proximity to police stations, hospitals, etc.
        """
        # This would integrate with emergency services location data
        # Placeholder implementation
        return 0.5
    
    def _get_business_activity(self, location):
        """
        Calculate score based on active businesses in the area
        """
        # This would integrate with business location/hours data
        # Placeholder implementation
        return 0.5

# Example usage
if __name__ == "__main__":
    # Initialize the mapper
    mapper = SafeRouteMapper()
    
    # Load crime data
    mapper.load_crime_data('crime_data.csv')
    
    # Get street network for a city
    mapper.get_street_network('Edmonton, Canada')
    
    # Find and visualize safest route
    start = (53.5461, -113.4937)  # Example coordinates
    end = (53.5444, -113.4909)
    
    route = mapper.find_safest_route(start, end)
    safety_map = mapper.visualize_route(route)
    safety_map.save('safe_route.html')