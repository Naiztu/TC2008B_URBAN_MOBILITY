using System.Collections.Generic;
[System.Serializable]

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
   public int width;

   /*public Agent(int height, int max_num_cars, int max_speed, int max_steps, Positions[] positions, int range_stop, int step_count, int time, int time_stop, int unique_id, int width)
   {
     this.height = height;
     this.max_num_cars = max_num_cars;
     this.max_speed = max_speed;
     this.max_steps = max_steps;
     this.positions = positions;
     this.range_stop = range_stop;
     this.step_count = step_count;
     this.time = time;
     this.time_stop = time_stop;
     this.unique_id = unique_id;
     this.width = width;
   }*/

   //public string message;

}

[System.Serializable]
public class PS
{
  public int direction;
  public Coor position;
  public int unique_id;
  public int speed;

  /*public Positions(int direction, Position[] position, int unique_id, int speed)
  {
    this.direction = direction;
    this.position = position;
    this.unique_id = unique_id;
    this.speed = speed;
  }*/


}




[System.Serializable]
public class Coor
{
    public int x;
    public int y;

    /*public Position(int x, int y)
    {
      this.x = x;
      this.y = y;
    }*/
}