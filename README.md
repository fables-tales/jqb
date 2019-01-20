# JQB

JQB is a tiny python query builder for [JQ](https://stedolan.github.io/jq/).

## Installation

1. Clone this repo
2. vendor `builder.py` in to your project, or run it on the command line to generate
   the strings you need


## Motivating example

The [MagicTheGathering.io](https://docs.magicthegathering.io/#api_v1cards_list)
cards index endpoint is parsed by the following calls:

```python
b = JQBuilder()
b.query(".cards").pipe().map_select(".imageUrl != null").iter().pipe().make_object(
    {
        "name": ".name",
        "layout": ".layout",
        "colors": ".colors",
        "colorIdentity": ".colorIdentity",
        "supertypes": ".supertypes",
        "types": ".types",
        "subtypes": ".subtypes",
        "rarity": ".rarity",
        "setname": ".setname",
        "text": ".text",
        "power": ".power",
        "toughness": ".toughness",
        "loyalty": ".loyalty",
        "manaCost": ".manaCost",
        "imageUrl": ".imageUrl",
    }
)
```

as can be seen in [`test.sh`](./test.sh).
