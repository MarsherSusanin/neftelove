<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTaskTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('tasks', function (Blueprint $table) {
            $table->id();
            $table->string('name', 100)->index('name');
            $table->text('description');
            $table->text('pereodic');
            $table->string('name_sputnik', 100)->index('name_sputnik');
            $table->integer('contour_line_width');
            $table->integer('sensetivity');
            $table->integer('maxcc');
            $table->string('lat', 20);
            $table->string('long', 20);
            $table->integer('i_leng');
            $table->string('status', 100)->default('in_proccess')->index('status');
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
        Schema::dropIfExists('tasks');
    }
}
