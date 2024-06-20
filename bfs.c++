#include <iostream>
#include <queue>
using namespace std;
const int MAX_VERTICES = 6;
void BFS(bool graph[MAX_VERTICES][MAX_VERTICES], int n, int start) {
    bool visited[MAX_VERTICES] = {false};
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int current = q.front();
        cout << current << " ";
        q.pop();

        for (int i = 0; i < n; ++i) {
            if (graph[current][i] && !visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}
int main() {
    bool graph[MAX_VERTICES][MAX_VERTICES] = {
        {0, 1, 1, 0, 0, 0},
        {1, 0, 0, 1, 1, 0},
        {1, 0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0, 1},
        {0, 1, 1, 0, 0, 1},
        {0, 0, 0, 1, 1, 0}
    };
   cout << "Breadth first traversal from vertex 0): ";
    BFS(graph, MAX_VERTICES, 0);
    return 0;
}
