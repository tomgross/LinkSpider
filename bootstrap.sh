#!/usr/bin/env bash
export DB=http://localhost:8080/db
export AUTH=root:root

bin/http --auth $AUTH $DB < json/container.json
bin/http --auth $AUTH $DB/urls/@addons id=linkspider