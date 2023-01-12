import pyintercom

intercom = pyintercom.get_intercom_instance()

intercom.subscribe("hey", print)
intercom.publish("hey", "hello world")

intercom.wait_here()
