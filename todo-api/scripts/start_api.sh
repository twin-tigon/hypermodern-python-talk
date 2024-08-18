#!/usr/bin/env bash

rye run alembic upgrade head

rye run start
