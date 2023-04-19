#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>

using namespace std;
struct City {
    int x, y;
    City(int x, int y) : x(x), y(y) {}
};
struct Node {
    int level, cost;
    vector<int> path;

    Node(int level, int cost, vector<int> path) : level(level), cost(cost), path(path) {}
    bool operator<(const Node& other) const {
        return cost > other.cost;
    }
};
double distance(const City& city1, const City& city2) {
    return sqrt(pow(city1.x - city2.x, 2) + pow(city1.y - city2.y, 2));
}
void bestFirstSearch(vector<City> cities) {
    priority_queue<Node> pq;
    vector<int> path(1, 0);
    Node initialNode(1, 0, path);
    pq.push(initialNode);
    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        if (node.level == cities.size()) {
            cout << "Path: ";
            for (int i = 0; i < node.path.size(); i++) {
                cout << node.path[i] << " ";
            }
            cout << "0" << endl;
            cout << "Cost: " << node.cost << endl;
            return;
        }
        int currentNode = node.path[node.path.size() - 1];
        for (int i = 1; i < cities.size(); i++) {
            if (find(node.path.begin(), node.path.end(), i) == node.path.end()) {
                vector<int> childPath = node.path;
                childPath.push_back(i);
                Node childNode(node.level + 1, node.cost + distance(cities[currentNode], cities[i]), childPath);
                pq.push(childNode);
            }
        }
    }
}
int main() {
    vector<City> cities;
    cities.push_back(City(0, 0));
    cities.push_back(City(2, 3));
    cities.push_back(City(3, 5));
    cities.push_back(City(5, 7));
    cities.push_back(City(7, 9));
    bestFirstSearch(cities);
    return 0;
}
