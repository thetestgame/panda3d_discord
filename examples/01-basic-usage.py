"""
 * Author: Jordan Maxwell
 * Written: 02/11/2019
 *
 * The MIT License (MIT)
 * 
 * Copyright (c) 2019 Nxt Games
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
"""

# include built pyd file
import sys
sys.path.append('../')

from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from discord import DiscordConnection, RichPresenceStatus

# Create Discord connection
connection = DiscordConnection.get_global_ptr()
connection.connect('345229890980937739', '')

# Set test status 
status = RichPresenceStatus()
status.state = 'Testing State'
status.details = 'Testing Details'
connection.publish_status(status)

def perform_update(task):
    """
    Calls the connection update function once per frame.
    Performs connection maintenance and callbacks.
    """

    connection.poll()
    
    return task.cont 

# Create showbase instance and add discord update task
base = ShowBase()
base.taskMgr.add(perform_update, 'discord-update-task')

# Run showbase
base.run()