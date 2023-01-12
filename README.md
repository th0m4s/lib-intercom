# Intercom introduction

**WARNING:** This version is not compatible with the original version found in the school GitHub repository as it planned that it will include more features.

*Intercom* was originally created as a Python package for a school project, the French Robotics Cup with the [DaVinciBot](https://davincibot.fr) student club.

It is now in a separate repository as it may be useful for other projects and might be extended to multiple programming languages.

For the moment, it is only available for the Python programming language.

It works by sending *data* to a *topic*. Data can be anything, as long as clients can decode it. For the 1st version of the protocol and to be easily understandable by many programming languages, it only supports data that can be serialized to JSON (numbers, strings, booleans, null, objects and arrays).

# Python quick-start

Internally, each topic is stored as a 24-bit integer computed using the CRC24 algorithm (derived from the well-known CRC32). This integer is then split into 3 bytes and appended to `224` to create an IP address in the range `224.0.0.0/8`.

**IMPORTANT:** You (ie. your machine) only receive (ie. process) messages sent to topics you subscribed to.

## Quick example:
*All packages include in-code comments to be used with any IntelliSense or autocompletion software.*

Start by importing and using the `get_intercom_instance` method to get an instance of the `Intercom` class:
```python
from pyintercom import get_intercom_instance
intercom = get_intercom_instance()
```
(you can also import the `Intercom` class and instantiate it if you need another instance)

To subscribe to a topic, use `subscribe`. It accepts a string or a list of strings as the topic(s) you want to subscribe to and an *optional* callback method:
```python
def callback(data):
    print(data)

intercom.subscribe('topic1', callback)
intercom.subscribe(['topic2', 'topic3'], callback)
```
This callback takes only 1 argument, the message data.

As Python is a *mainly single-threaded* language, you must ask the library to run your callbacks:
```python
intercom.run_callbacks()
```

However, this runs the callbacks once then continues. You can ask the library to run the callbacks indefinitely and block your current thread or be starting a new thread to do that:
```python
intercom.wait_here()
# or
intercom.wait_in_new_thread()
```
Calling `wait_in_new_thread` multiple times will not create multiple threads and do nothing after the first execution.

Finally, to publish data to a topic, just use the `publish` method with a topic and some data:
```python
intercom.publish('topic1', 'Hello world!')
```

Intercom also supports events, which are messages without additional data. They may be useful to trigger an important action like an emergency stop or an action that doesn't need a specific parameter.

You can either register a callback that runs on every event (for debugging purposes) by using `on_events`. This method only takes 1 argument, a callback:
```python
intercom.on_events(lambda event_name: print('Received event', event_name))
```
...or by listening to a specific event with `on_event` with takes 2 arguments, an event name as a string and a callback:
```python
intercom.on_event('emergency_stop', lambda: print('Emergency stop!'))
```

Finally, to send an event, you need to use the `publish_event` method that takes 1 argument, the event name as a string:
```python
intercom.publish_event('emergency_stop')
```

All `subscribe`, `on_events` and `on_event` return a reference as an `int` that can be used to unsubscribe from a topic or event with `unsubscribe`:
```python
ref = intercom.subscribe('topic1', callback)
intercom.unsubscribe(ref)
```

## Utils

Each language implementation may include some util methods used by intercom, including the CRC24 algorithm. For Python, theses methods are located in the `pyintercom.utils` package.


# Readme addendum
When more languages will be added, only the protocol will be presented here and the Python docs will be moved to `python/README.md`.