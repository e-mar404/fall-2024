class Person
  def work
    puts "workig.."
  end

  def method_missing(name, *args)
    activities = ['Teis', 'Football']

    activity = name.to_s.split('play')[1]

    if (activities.include?(activity))
      puts "is like to play #{activity}"
    else
      puts "i dot play #{activity}"
    end
  end
end

sam = Person.new
sam.work

sam.playTeis
sam.playFootball
sam.playSomethig
