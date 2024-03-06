from marshmallow import Schema, fields

    
class UserSchemaPost(Schema):
    user = fields.Str(required=True)

class TourSchemaPost(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Str(required=True)
    date = fields.Str(required=False)

class TourSchemaGet(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    price = fields.Str()
    date = fields.Str()

class TourSchemaShow(Schema):   
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    price = fields.Str()
    date = fields.Str()

class TourSchemaPut(Schema):
    name = fields.Str(required=False)
    description = fields.Str(required=False)
    price = fields.Str(required=False)
    date = fields.Str(required=False)

class BookingSchemaPost(Schema):
    date = fields.Str(required=True)
    quantity = fields.Int(required=True)
    user_id = fields.Int(required=True)
    tour_id = fields.Int(required=True)

class BookingSchemaGet(Schema):
    id = fields.Int()
    date = fields.Str()
    quantity = fields.Int()
    user_id = fields.Int()
    tour_id = fields.Int()

class BookingSchemaShow(Schema):
    id = fields.Int()
    date = fields.Str()
    quantity = fields.Int()
    user_id = fields.Int()
    tour_id = fields.Int()

