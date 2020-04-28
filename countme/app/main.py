import falcon

sum_of_numbers = 0

class Count:
    def on_get(self, req, resp):
        global sum_of_numbers 
        resp.body = str(sum_of_numbers)


class NewNumber:
    def on_post(self, req, resp):
        global sum_of_numbers 
        new_number = int(req.stream.read())
        sum_of_numbers += new_number


app = falcon.API()
app.add_route('/count/', Count())
app.add_route('/', NewNumber())