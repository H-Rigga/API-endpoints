class Order(object):

    order_data = []

    def __init__(self):
        pass

    @staticmethod
    def get_all_orders():

        return {"all_orders": Order.order_data}

    @staticmethod
    def get_order_by_id(order_id):

        for order in Order.order_data:
            if order_id == order['order_id']:
                return {"specific_order": order}

    def new_order(self, orderer, what_order):

        order_id = len(Order.order_data) + 1
        order_dict = {}
        completed = False

        if what_order is None:
            return {"msg": "Please place an order."}

        order_dict['orderer'] = orderer
        order_dict['order_id'] = order_id
        order_dict['what_order'] = what_order
        order_dict['completed'] = completed

        Order.order_data.append(order_dict)

        return {"message": "Order placed successfully.", "order_data": order_dict}

    def update_order(self, order_id):

        for order in Order.order_data:
            if order.get('order_id') == order_id:
                order['completed'] = True

                return {"msg": "Order completed", "order_data": order}
            return {"msg": "No such order has been made."}

    def delete_order(self, order_id):

        found_order = self.get_order_by_id(order_id)

        if found_order:

                self.order_data[:] = [d for d in self.order_data
                                         if d['order_id'] != found_order["specific_order"]['order_id']]

                return {"msg": "The order has been deleted successfully."}
        return {"msg": "No such order has been made."}