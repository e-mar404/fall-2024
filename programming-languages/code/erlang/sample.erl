#!/usr/bin/env escript

main(_) ->
 process([1, 2, 3, 4]).

process([H | []]) ->
  io:format("~p", [H]);

process([H | T]) ->
  io:format("~p-", [H]),
  process(T).
