<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Task extends Model
{
    use HasFactory;

    protected $guarded = [];

    public function allerts()
    {
        return $this->hasMany(Alert::class);
    }

    public function stack()
    {
        return $this->belongsTo(Stack::class);
    }
}
