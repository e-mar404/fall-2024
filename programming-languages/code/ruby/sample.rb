class Person
  def work
    puts "working..."
  end

  def method_missing(name, *args)
    activities = ['Tennis', 'Football']

    activity = name.to_s.split('play')[1]

    if (activities.include?(activity))
      puts "is like to play #{activity}"
    else
      puts "i dont play #{activity}"
    end
  end
end

sam = Person.new
sam.work

sam.playTennis
sam.playFootball
sam.playSomethig
