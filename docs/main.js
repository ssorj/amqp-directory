/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

"use strict";

let transom = {
    getDescendant(elem, path) {
        var names = path.split(".");
        var node = elem;

        for (var i = 0; i < names.length; i++) {
            var elems = node.getElementsByTagName(names[i]);

            if (elems.length === 0) {
                return null;
            }

            node = elems[0];
        }

        return node;
    },

    updateGlobalNavigation() {
        console.log("Updating global navigation");

        var href = window.location.href;
        var elem = document.getElementById("-global-navigation");
        var child = elem.firstChild;

        if (href.charAt(href.length - 1) === "/") {
            href += "index.html";
        }

        while (child) {
            if (child.nodeType === 1) {
                if (child.href === href) {
                    child.className += " selected";
                    break;
                }
            }

            child = child.nextSibling;
        }
    }    
}

window.addEventListener("load", transom.updateGlobalNavigation);
