using System.Collections.Generic;
[System.Serializable]

// Esta clase posee la estructura con la que el server de python genera los json.
public class Agent
{
    public int height;
    public int max_num_cars;
    public int max_speed;
    public int max_steps;
    public List<PS> positions;
    public int range_stop;
    public int step_count;
    public int time;
    public int time_stop;
    public int unique_id;
    public int state_num_cars;
    public int width;
    public int num_cars_is_out;


}

[System.Serializable]
public class PS
{
    public int direction;
    public Coor pos;
    public int unique_id;
    public int speed;


}


[System.Serializable]
public class Coor
{
    public int x;
    public int y;


}