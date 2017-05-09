<h1>Dungeon Crawler Game</h1>
<a href="https://github.com/JeremyLuman/Python/wiki/READ-ME:-Dungeon-Crawl-Game">READ ME</a>

## Dungeon Crawler Game Code Example 

```python
_world = {}
starting_position = (0, 0)

def tile_exists(x, y):
        return _world.get((x, y))


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
```
