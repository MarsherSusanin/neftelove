<?php

namespace App\Services;

use App\Models\Task;
use App\Models\Alert;
use Carbon\Carbon;
use Illuminate\Support\Facades\Http;

class SatteliteAnalizeProcessor {

    protected $task;

    public function __construct(Task $task) {
        $this->task = $task;
    }

    public function process() {
        $response = Http::post(config('api.computer_vision_api').'/getcontours',
        [
            "download_data" => "download",
            "name_sputnik" => $this->task['name_sputnik'],
            "type_relief" => "0",
            "contour_line_width" => "2",
            "sensitivity" => $this->task['sensetivity'],
            "maxcc" => $this->task['maxcc'],
            "time_interval" => Carbon::today()->subDays(5)->toDateString()."/".Carbon::today()->toDateString(),
            "lat" => $this->task['lat'],
            "long" => $this->task['long'],
            "iLeng" => $this->task['i_leng']
        ]
    );
        $response->throw(function ($response, $e) {

        });
        Alert::create([
            'contours' => json_encode( $response['contours'] ),
            'contours2' => json_encode( $response['contours2'] ),
            'image' => $response['image'],
            'result_image' => $response['result_image'],
            'task_id' => $this->task['id']
        ]);
    }
}
