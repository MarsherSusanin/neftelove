<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateAlertTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('alerts', function (Blueprint $table) {
            $table->id();
            $table->longText('contours');
            $table->longText('contours2');
            $table->longText('image');
            $table->longText('result_image');
            $table->foreignId('task_id')->index('task_id');
            $table->foreignId('stack_id')->nullable()->index('stack_id');
            $table->string('status', 100)->default('pending')->index('status');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('alerts');
    }
}
