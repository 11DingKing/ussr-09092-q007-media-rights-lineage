require "minitest/autorun"
require_relative "../app/models/asset"

class AssetTest < Minitest::Test
  def test_derivative_points_to_parent
    asset = Asset.new(digest: "child", parent_digest: "source")
    assert_equal "source", asset.parent_digest
  end
end
