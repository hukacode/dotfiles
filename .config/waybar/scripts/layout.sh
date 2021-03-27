#!/bin/bash

main_index=$(riverctl get-option -focused-output main_index)
master_layout=$(riverctl get-option -focused-output master_layout)
slave_layout=$(riverctl get-option -focused-output slave_layout)

TEXT="($main_index) $master_layout - $slave_layout"

echo "{\"text\": \"$TEXT\", \"tooltip\": \"leftwm is cringe\" }"
