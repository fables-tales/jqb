class JQBuilder:
    def __init__(self):
        self.expression_parts = []


    def query(self, query):
        self.expression_parts.append(query)
        return self

    def pipe(self):
        self.expression_parts.append(" | ")
        return self

    def map_select(self, boolean_query):
        self.query("map(select(%s))" % (boolean_query))
        return self

    def iter(self):
        self.pipe()
        self.query(".[]")
        return self

    def make_object(self, object):
        self.query("{")
        for idx, (key, value) in enumerate(object.items()):
            self.query("%s: %s" % (key, value))
            if idx != len(object) - 1:
                self.query(",")
        self.query("}")
        return self

    def __str__(self):
        return "".join((str(x) for x in self.expression_parts))


def main():
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

    print(str(b))

if __name__ == "__main__":
    main()
