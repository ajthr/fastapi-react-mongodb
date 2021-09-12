# {{cookiecutter.project_name}}

## Development

The only dependencies for this project should be docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
docker-compose up -d
```

And navigate to http://localhost/

### Rebuilding containers:

```
docker-compose build
```

### Bringing containers down:

```
docker-compose down
```

## Testing

To run test for api, run
```bash
docker-compose run --rm api sh -c "pytest"
```

to run test for web, run
```bash
docker-compose run --rm web sh -c "npm run test"
```
