import json


class Path:
    source_file = "../../resources/out.json"
    source_path = "../../resources/"


class Resource:
    wood = "WOOD"
    quartz = "QUARTZ"
    fur = "FUR"
    rum = "RUM"
    iron = "IRON"
    fish = "FISH"
    flower = "FLOWER"
    fruits = "FRUITS"
    ore = "ORE"
    sugar_cane = "SUGAR_CANE"
    glass = "glass"
    ingot = "INGOT"
    leather = "LEATHER"
    plank = "PLANK"


class JsonArguments:
    data = "data"
    budget = "budget"
    contracts = "contracts"
    amount = 'amount'
    resource = 'resource'
    cost = "cost"
    extras = "extras"
    creek = "creeks"
    site = "sites"
    action = "action"
    exploit = "exploit"
    parameters = "parameters"


__all__ = ["json", "Resource", "Path", "JsonArguments"]
