<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

use App\Http\Controllers\TaskController;
use App\Http\Controllers\AlertController;
use App\Http\Controllers\StackController;
use App\Http\Controllers\OverviewController;

//Route::post('/overview', OverviewController::class);

Route::apiResources([
    'tasks' => TaskController::class,
    'stack' => StackController::class,
]);

Route::apiResource('alerts', AlertController::class)->except(['store']);
