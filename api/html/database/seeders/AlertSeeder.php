<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Alert;

class AlertSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {


        $response = json_decode($json, true);

        Alert::create([
            'contours' => json_encode( $response['contours'] ),
            'contours2' => json_encode( $response['contours2'] ),
            'image' => $response['image'],
            'result_image' => $response['result_image'],
            'task_id' => 5
        ]);
    }
}