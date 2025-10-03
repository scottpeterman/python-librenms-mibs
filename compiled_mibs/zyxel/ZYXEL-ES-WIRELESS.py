# SNMP MIB module (ZYXEL-ES-WIRELESS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zyxel\ZYXEL-ES-WIRELESS
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:58 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

esWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlanRadioTable_Object = MibTable
wlanRadioTable = _WlanRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1)
)
if mibBuilder.loadTexts:
    wlanRadioTable.setStatus("current")
_WlanRadioEntry_Object = MibTableRow
wlanRadioEntry = _WlanRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1)
)
wlanRadioEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanRadioIndex"),
)
if mibBuilder.loadTexts:
    wlanRadioEntry.setStatus("current")


class _WlanCurrentChannel_Type(Integer32):
    """Custom type wlanCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              1,
              2,
              3,
              4,
              5,
              5,
              6,
              7,
              8,
              9,
              9,
              10,
              11,
              12,
              13,
              13,
              17,
              21,
              25,
              29,
              33,
              36,
              37,
              40,
              41,
              44,
              45,
              48,
              49,
              51,
              52,
              53,
              55,
              56,
              57,
              60,
              64,
              69,
              73,
              77,
              81,
              85,
              89,
              93,
              97,
              100,
              101,
              104,
              105,
              108,
              109,
              112,
              113,
              116,
              117,
              120,
              121,
              124,
              125,
              128,
              129,
              132,
              133,
              136,
              137,
              140,
              141,
              145,
              149,
              149,
              153,
              153,
              157,
              157,
              161,
              161,
              165,
              165,
              169,
              173,
              177,
              181,
              185,
              189,
              193,
              197,
              201,
              205,
              209,
              213,
              217,
              221,
              225,
              229,
              233)
        )
    )
    namedValues = NamedValues(
        *(("device_is_disable", 0),
          ("channel-01_2412mhz", 1),
          ("channel-01_5955mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-05_5975mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-09_5995mhz", 9),
          ("channel-10_2457mhz", 10),
          ("channel-11_2462mhz", 11),
          ("channel-12_2467mhz", 12),
          ("channel-13_2472mhz", 13),
          ("channel-13_6015mhz", 13),
          ("channel-17_6035mhz", 17),
          ("channel-21_6055mhz", 21),
          ("channel-25_6075mhz", 25),
          ("channel-29_6095mhz", 29),
          ("channel-33_6115mhz", 33),
          ("channel-36_5180mhz", 36),
          ("channel-37_6135mhz", 37),
          ("channel-40_5200mhz", 40),
          ("channel-41_6155mhz", 41),
          ("channel-44_5220mhz", 44),
          ("channel-45_6175mhz", 45),
          ("channel-48_5240mhz", 48),
          ("channel-49_6195mhz", 49),
          ("channel-61_6255mhz", 51),
          ("channel-52_5260mhz", 52),
          ("channel-53_6215mhz", 53),
          ("channel-65_6275mhz", 55),
          ("channel-56_5280mhz", 56),
          ("channel-57_6235mhz", 57),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64),
          ("channel-69_6295mhz", 69),
          ("channel-73_6315mhz", 73),
          ("channel-77_6335mhz", 77),
          ("channel-81_6355mhz", 81),
          ("channel-85_6375mhz", 85),
          ("channel-89_6395mhz", 89),
          ("channel-93_6415mhz", 93),
          ("channel-97_6435mhz", 97),
          ("channel-100_5500mhz", 100),
          ("channel-101_6455mhz", 101),
          ("channel-104_5520mhz", 104),
          ("channel-105_6475mhz", 105),
          ("channel-108_5540mhz", 108),
          ("channel-109_6495mhz", 109),
          ("channel-112_5560mhz", 112),
          ("channel-113_6515mhz", 113),
          ("channel-116_5580mhz", 116),
          ("channel-117_6535mhz", 117),
          ("channel-120_5600mhz", 120),
          ("channel-121_6555mhz", 121),
          ("channel-124_5620mhz", 124),
          ("channel-125_6575mhz", 125),
          ("channel-128_5640mhz", 128),
          ("channel-129_6595mhz", 129),
          ("channel-132_5660mhz", 132),
          ("channel-133_6615mhz", 133),
          ("channel-136_5680mhz", 136),
          ("channel-137_6635mhz", 137),
          ("channel-140_5700mhz", 140),
          ("channel-141_6655mhz", 141),
          ("channel-145_6675mhz", 145),
          ("channel-149_5745mhz", 149),
          ("channel-149_6695mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-153_6715mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-157_6735mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-161_6755mhz", 161),
          ("channel-165_5825mhz", 165),
          ("channel-165_6775mhz", 165),
          ("channel-169_6795mhz", 169),
          ("channel-173_6815mhz", 173),
          ("channel-177_6835mhz", 177),
          ("channel-181_6855mhz", 181),
          ("channel-185_6875mhz", 185),
          ("channel-189_6895mhz", 189),
          ("channel-193_6915mhz", 193),
          ("channel-197_6935mhz", 197),
          ("channel-201_6955mhz", 201),
          ("channel-205_6975mhz", 205),
          ("channel-209_6995mhz", 209),
          ("channel-213_7015mhz", 213),
          ("channel-217_7035mhz", 217),
          ("channel-221_7055mhz", 221),
          ("channel-225_7075mhz", 225),
          ("channel-229_7095mhz", 229),
          ("channel-233_7115mhz", 233))
    )


_WlanCurrentChannel_Type.__name__ = "Integer32"
_WlanCurrentChannel_Object = MibTableColumn
wlanCurrentChannel = _WlanCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 1),
    _WlanCurrentChannel_Type()
)
wlanCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentChannel.setStatus("current")
_WlanStationCount_Type = Unsigned32
_WlanStationCount_Object = MibTableColumn
wlanStationCount = _WlanStationCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 2),
    _WlanStationCount_Type()
)
wlanStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStationCount.setStatus("current")
_WlanSupportedChannel_Type = OctetString
_WlanSupportedChannel_Object = MibTableColumn
wlanSupportedChannel = _WlanSupportedChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 3),
    _WlanSupportedChannel_Type()
)
wlanSupportedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSupportedChannel.setStatus("current")


class _WlanMode_Type(Integer32):
    """Custom type wlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode_2_4G", 1),
          ("mode_5G", 2),
          ("mode_6G", 3))
    )


_WlanMode_Type.__name__ = "Integer32"
_WlanMode_Object = MibTableColumn
wlanMode = _WlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 5),
    _WlanMode_Type()
)
wlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMode.setStatus("current")


class _WlanChannel_Type(Integer32):
    """Custom type wlanChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              2,
              3,
              4,
              5,
              5,
              6,
              7,
              8,
              9,
              9,
              10,
              11,
              12,
              13,
              13,
              17,
              21,
              25,
              29,
              33,
              36,
              37,
              40,
              41,
              44,
              45,
              48,
              49,
              51,
              52,
              53,
              55,
              56,
              57,
              60,
              64,
              69,
              73,
              77,
              81,
              85,
              89,
              93,
              97,
              100,
              101,
              104,
              105,
              108,
              109,
              112,
              113,
              116,
              117,
              120,
              121,
              124,
              125,
              128,
              129,
              132,
              133,
              136,
              137,
              140,
              141,
              145,
              149,
              149,
              153,
              153,
              157,
              157,
              161,
              161,
              165,
              165,
              169,
              173,
              177,
              181,
              185,
              189,
              193,
              197,
              201,
              205,
              209,
              213,
              217,
              221,
              225,
              229,
              233)
        )
    )
    namedValues = NamedValues(
        *(("channel-01_2412mhz", 1),
          ("channel-01_5955mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-05_5975mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-09_5995mhz", 9),
          ("channel-10_2457mhz", 10),
          ("channel-11_2462mhz", 11),
          ("channel-12_2467mhz", 12),
          ("channel-13_2472mhz", 13),
          ("channel-13_6015mhz", 13),
          ("channel-17_6035mhz", 17),
          ("channel-21_6055mhz", 21),
          ("channel-25_6075mhz", 25),
          ("channel-29_6095mhz", 29),
          ("channel-33_6115mhz", 33),
          ("channel-36_5180mhz", 36),
          ("channel-37_6135mhz", 37),
          ("channel-40_5200mhz", 40),
          ("channel-41_6155mhz", 41),
          ("channel-44_5220mhz", 44),
          ("channel-45_6175mhz", 45),
          ("channel-48_5240mhz", 48),
          ("channel-49_6195mhz", 49),
          ("channel-61_6255mhz", 51),
          ("channel-52_5260mhz", 52),
          ("channel-53_6215mhz", 53),
          ("channel-65_6275mhz", 55),
          ("channel-56_5280mhz", 56),
          ("channel-57_6235mhz", 57),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64),
          ("channel-69_6295mhz", 69),
          ("channel-73_6315mhz", 73),
          ("channel-77_6335mhz", 77),
          ("channel-81_6355mhz", 81),
          ("channel-85_6375mhz", 85),
          ("channel-89_6395mhz", 89),
          ("channel-93_6415mhz", 93),
          ("channel-97_6435mhz", 97),
          ("channel-100_5500mhz", 100),
          ("channel-101_6455mhz", 101),
          ("channel-104_5520mhz", 104),
          ("channel-105_6475mhz", 105),
          ("channel-108_5540mhz", 108),
          ("channel-109_6495mhz", 109),
          ("channel-112_5560mhz", 112),
          ("channel-113_6515mhz", 113),
          ("channel-116_5580mhz", 116),
          ("channel-117_6535mhz", 117),
          ("channel-120_5600mhz", 120),
          ("channel-121_6555mhz", 121),
          ("channel-124_5620mhz", 124),
          ("channel-125_6575mhz", 125),
          ("channel-128_5640mhz", 128),
          ("channel-129_6595mhz", 129),
          ("channel-132_5660mhz", 132),
          ("channel-133_6615mhz", 133),
          ("channel-136_5680mhz", 136),
          ("channel-137_6635mhz", 137),
          ("channel-140_5700mhz", 140),
          ("channel-141_6655mhz", 141),
          ("channel-145_6675mhz", 145),
          ("channel-149_5745mhz", 149),
          ("channel-149_6695mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-153_6715mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-157_6735mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-161_6755mhz", 161),
          ("channel-165_5825mhz", 165),
          ("channel-165_6775mhz", 165),
          ("channel-169_6795mhz", 169),
          ("channel-173_6815mhz", 173),
          ("channel-177_6835mhz", 177),
          ("channel-181_6855mhz", 181),
          ("channel-185_6875mhz", 185),
          ("channel-189_6895mhz", 189),
          ("channel-193_6915mhz", 193),
          ("channel-197_6935mhz", 197),
          ("channel-201_6955mhz", 201),
          ("channel-205_6975mhz", 205),
          ("channel-209_6995mhz", 209),
          ("channel-213_7015mhz", 213),
          ("channel-217_7035mhz", 217),
          ("channel-221_7055mhz", 221),
          ("channel-225_7075mhz", 225),
          ("channel-229_7095mhz", 229),
          ("channel-233_7115mhz", 233))
    )


_WlanChannel_Type.__name__ = "Integer32"
_WlanChannel_Object = MibTableColumn
wlanChannel = _WlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 6),
    _WlanChannel_Type()
)
wlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannel.setStatus("current")


class _WlanRadioIndex_Type(Integer32):
    """Custom type wlanRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WlanRadioIndex_Type.__name__ = "Integer32"
_WlanRadioIndex_Object = MibTableColumn
wlanRadioIndex = _WlanRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 7),
    _WlanRadioIndex_Type()
)
wlanRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanRadioIndex.setStatus("current")
_WlanStationTable_Object = MibTable
wlanStationTable = _WlanStationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2)
)
if mibBuilder.loadTexts:
    wlanStationTable.setStatus("current")
_WlanStationEntry_Object = MibTableRow
wlanStationEntry = _WlanStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1)
)
wlanStationEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "stationIndex"),
)
if mibBuilder.loadTexts:
    wlanStationEntry.setStatus("current")


class _StationIndex_Type(Integer32):
    """Custom type stationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StationIndex_Type.__name__ = "Integer32"
_StationIndex_Object = MibTableColumn
stationIndex = _StationIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 1),
    _StationIndex_Type()
)
stationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stationIndex.setStatus("current")


class _StationMacAddress_Type(MacAddress):
    """Custom type stationMacAddress based on MacAddress"""
    defaultValue = OctetString("public")


_StationMacAddress_Type.__name__ = "MacAddress"
_StationMacAddress_Object = MibTableColumn
stationMacAddress = _StationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 2),
    _StationMacAddress_Type()
)
stationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationMacAddress.setStatus("current")
_StationAssociatedTime_Type = DateAndTime
_StationAssociatedTime_Object = MibTableColumn
stationAssociatedTime = _StationAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 3),
    _StationAssociatedTime_Type()
)
stationAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationAssociatedTime.setStatus("current")
_StationSSID_Type = OctetString
_StationSSID_Object = MibTableColumn
stationSSID = _StationSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 4),
    _StationSSID_Type()
)
stationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationSSID.setStatus("current")
_StationSignalStrength_Type = OctetString
_StationSignalStrength_Object = MibTableColumn
stationSignalStrength = _StationSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 5),
    _StationSignalStrength_Type()
)
stationSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationSignalStrength.setStatus("current")
_WlanStatisticsTable_Object = MibTable
wlanStatisticsTable = _WlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3)
)
if mibBuilder.loadTexts:
    wlanStatisticsTable.setStatus("current")
_WlanStatisticsEntry_Object = MibTableRow
wlanStatisticsEntry = _WlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1)
)
wlanStatisticsEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanStatisticsIndex"),
)
if mibBuilder.loadTexts:
    wlanStatisticsEntry.setStatus("current")
_Dot11FailedCount_Type = Counter64
_Dot11FailedCount_Object = MibTableColumn
dot11FailedCount = _Dot11FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 1),
    _Dot11FailedCount_Type()
)
dot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FailedCount.setStatus("current")
_Dot11RetryCount_Type = Counter64
_Dot11RetryCount_Object = MibTableColumn
dot11RetryCount = _Dot11RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 2),
    _Dot11RetryCount_Type()
)
dot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RetryCount.setStatus("current")
_Dot11ACKFailureCount_Type = Counter64
_Dot11ACKFailureCount_Object = MibTableColumn
dot11ACKFailureCount = _Dot11ACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 3),
    _Dot11ACKFailureCount_Type()
)
dot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ACKFailureCount.setStatus("current")
_Dot11ReceivedFragmentCount_Type = Counter64
_Dot11ReceivedFragmentCount_Object = MibTableColumn
dot11ReceivedFragmentCount = _Dot11ReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 4),
    _Dot11ReceivedFragmentCount_Type()
)
dot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFragmentCount.setStatus("current")
_Dot11TransmittedFrameCount_Type = Counter64
_Dot11TransmittedFrameCount_Object = MibTableColumn
dot11TransmittedFrameCount = _Dot11TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 5),
    _Dot11TransmittedFrameCount_Type()
)
dot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFrameCount.setStatus("current")
_Dot11ReceivedPktCount_Type = Counter64
_Dot11ReceivedPktCount_Object = MibTableColumn
dot11ReceivedPktCount = _Dot11ReceivedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 6),
    _Dot11ReceivedPktCount_Type()
)
dot11ReceivedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedPktCount.setStatus("current")
_Dot11TransmittedPktCount_Type = Counter64
_Dot11TransmittedPktCount_Object = MibTableColumn
dot11TransmittedPktCount = _Dot11TransmittedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 7),
    _Dot11TransmittedPktCount_Type()
)
dot11TransmittedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedPktCount.setStatus("current")


class _WlanStatisticsIndex_Type(Integer32):
    """Custom type wlanStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WlanStatisticsIndex_Type.__name__ = "Integer32"
_WlanStatisticsIndex_Object = MibTableColumn
wlanStatisticsIndex = _WlanStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 8),
    _WlanStatisticsIndex_Type()
)
wlanStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanStatisticsIndex.setStatus("current")
_WlanTraps_ObjectIdentity = ObjectIdentity
wlanTraps = _WlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4)
)
if mibBuilder.loadTexts:
    wlanTraps.setStatus("current")
_TrapsControl_ObjectIdentity = ObjectIdentity
trapsControl = _TrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    trapsControl.setStatus("current")


class _WlanTrapsControl_Type(Integer32):
    """Custom type wlanTrapsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanTrapsControl_Type.__name__ = "Integer32"
_WlanTrapsControl_Object = MibScalar
wlanTrapsControl = _WlanTrapsControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 1, 1),
    _WlanTrapsControl_Type()
)
wlanTrapsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanTrapsControl.setStatus("current")
_TrapsFormat_ObjectIdentity = ObjectIdentity
trapsFormat = _TrapsFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    trapsFormat.setStatus("current")
_TrapGenericMessage_Type = DisplayString
_TrapGenericMessage_Object = MibScalar
trapGenericMessage = _TrapGenericMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2, 1),
    _TrapGenericMessage_Type()
)
trapGenericMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapGenericMessage.setStatus("current")
_TrapMACAddress_Type = MacAddress
_TrapMACAddress_Object = MibScalar
trapMACAddress = _TrapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2, 2),
    _TrapMACAddress_Type()
)
trapMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMACAddress.setStatus("current")
_TrapWlanSSID_Type = DisplayString
_TrapWlanSSID_Object = MibScalar
trapWlanSSID = _TrapWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 2, 3),
    _TrapWlanSSID_Type()
)
trapWlanSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapWlanSSID.setStatus("current")
_TrapsItems_ObjectIdentity = ObjectIdentity
trapsItems = _TrapsItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3)
)
if mibBuilder.loadTexts:
    trapsItems.setStatus("current")
_WlanControllerAPTable_Object = MibTable
wlanControllerAPTable = _WlanControllerAPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11)
)
if mibBuilder.loadTexts:
    wlanControllerAPTable.setStatus("current")
_WlanControllerAPEntry_Object = MibTableRow
wlanControllerAPEntry = _WlanControllerAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1)
)
wlanControllerAPEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerAPIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerAPEntry.setStatus("current")


class _WlanControllerAPIndex_Type(Integer32):
    """Custom type wlanControllerAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WlanControllerAPIndex_Type.__name__ = "Integer32"
_WlanControllerAPIndex_Object = MibTableColumn
wlanControllerAPIndex = _WlanControllerAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 1),
    _WlanControllerAPIndex_Type()
)
wlanControllerAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPIndex.setStatus("current")


class _WlanControllerAPMac_Type(OctetString):
    """Custom type wlanControllerAPMac based on OctetString"""
    defaultValue = OctetString("public")


_WlanControllerAPMac_Type.__name__ = "OctetString"
_WlanControllerAPMac_Object = MibTableColumn
wlanControllerAPMac = _WlanControllerAPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 2),
    _WlanControllerAPMac_Type()
)
wlanControllerAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPMac.setStatus("current")
_WlanControllerAPDescription_Type = OctetString
_WlanControllerAPDescription_Object = MibTableColumn
wlanControllerAPDescription = _WlanControllerAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 3),
    _WlanControllerAPDescription_Type()
)
wlanControllerAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPDescription.setStatus("current")
_WlanControllerAPMgmtIPAddr_Type = IpAddress
_WlanControllerAPMgmtIPAddr_Object = MibTableColumn
wlanControllerAPMgmtIPAddr = _WlanControllerAPMgmtIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 4),
    _WlanControllerAPMgmtIPAddr_Type()
)
wlanControllerAPMgmtIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPMgmtIPAddr.setStatus("current")
_WlanControllerAPStationNum_Type = Unsigned32
_WlanControllerAPStationNum_Object = MibTableColumn
wlanControllerAPStationNum = _WlanControllerAPStationNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 11, 1, 5),
    _WlanControllerAPStationNum_Type()
)
wlanControllerAPStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerAPStationNum.setStatus("current")
_WlanControllerAPRadioTable_Object = MibTable
wlanControllerAPRadioTable = _WlanControllerAPRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12)
)
if mibBuilder.loadTexts:
    wlanControllerAPRadioTable.setStatus("current")
_WlanControllerAPRadioEntry_Object = MibTableRow
wlanControllerAPRadioEntry = _WlanControllerAPRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1)
)
wlanControllerAPRadioEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerRadioIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerAPRadioEntry.setStatus("current")


class _WlanControllerRadioIndex_Type(Integer32):
    """Custom type wlanControllerRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlanControllerRadioIndex_Type.__name__ = "Integer32"
_WlanControllerRadioIndex_Object = MibTableColumn
wlanControllerRadioIndex = _WlanControllerRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 1),
    _WlanControllerRadioIndex_Type()
)
wlanControllerRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioIndex.setStatus("current")
_WlanControllerRadioStationNum_Type = Unsigned32
_WlanControllerRadioStationNum_Object = MibTableColumn
wlanControllerRadioStationNum = _WlanControllerRadioStationNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 2),
    _WlanControllerRadioStationNum_Type()
)
wlanControllerRadioStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioStationNum.setStatus("current")


class _WlanControllerRadioCurrentChannel_Type(Integer32):
    """Custom type wlanControllerRadioCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("device_is_disable", 0),
          ("channel-01_2412mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-10_2457mhz", 10),
          ("channel-11_2462mhz", 11),
          ("channel-12_2467mhz", 12),
          ("channel-13_2472mhz", 13),
          ("channel-36_5180mhz", 36),
          ("channel-40_5200mhz", 40),
          ("channel-44_5220mhz", 44),
          ("channel-48_5240mhz", 48),
          ("channel-52_5260mhz", 52),
          ("channel-56_5280mhz", 56),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64),
          ("channel-100_5500mhz", 100),
          ("channel-104_5520mhz", 104),
          ("channel-108_5540mhz", 108),
          ("channel-112_5560mhz", 112),
          ("channel-116_5580mhz", 116),
          ("channel-120_5600mhz", 120),
          ("channel-124_5620mhz", 124),
          ("channel-128_5640mhz", 128),
          ("channel-132_5660mhz", 132),
          ("channel-136_5680mhz", 136),
          ("channel-140_5700mhz", 140),
          ("channel-149_5745mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-165_5825mhz", 165))
    )


_WlanControllerRadioCurrentChannel_Type.__name__ = "Integer32"
_WlanControllerRadioCurrentChannel_Object = MibTableColumn
wlanControllerRadioCurrentChannel = _WlanControllerRadioCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 3),
    _WlanControllerRadioCurrentChannel_Type()
)
wlanControllerRadioCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioCurrentChannel.setStatus("current")


class _WlanControllerRadioOperationMode_Type(Integer32):
    """Custom type wlanControllerRadioOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ap", 1),
          ("monitor", 2),
          ("mesh-Root", 3),
          ("mesh-repeater", 4))
    )


_WlanControllerRadioOperationMode_Type.__name__ = "Integer32"
_WlanControllerRadioOperationMode_Object = MibTableColumn
wlanControllerRadioOperationMode = _WlanControllerRadioOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 4),
    _WlanControllerRadioOperationMode_Type()
)
wlanControllerRadioOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioOperationMode.setStatus("current")


class _WlanControllerRadioBand_Type(Integer32):
    """Custom type wlanControllerRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("mode_2_4G", 1),
          ("mode_5G", 2))
    )


_WlanControllerRadioBand_Type.__name__ = "Integer32"
_WlanControllerRadioBand_Object = MibTableColumn
wlanControllerRadioBand = _WlanControllerRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 5),
    _WlanControllerRadioBand_Type()
)
wlanControllerRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioBand.setStatus("current")
_WlanControllerRadioTxPkt_Type = Counter32
_WlanControllerRadioTxPkt_Object = MibTableColumn
wlanControllerRadioTxPkt = _WlanControllerRadioTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 6),
    _WlanControllerRadioTxPkt_Type()
)
wlanControllerRadioTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioTxPkt.setStatus("current")
_WlanControllerRadioRxPkt_Type = Counter32
_WlanControllerRadioRxPkt_Object = MibTableColumn
wlanControllerRadioRxPkt = _WlanControllerRadioRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 7),
    _WlanControllerRadioRxPkt_Type()
)
wlanControllerRadioRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioRxPkt.setStatus("current")
_WlanControllerRadioTxPower_Type = Integer32
_WlanControllerRadioTxPower_Object = MibTableColumn
wlanControllerRadioTxPower = _WlanControllerRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 12, 1, 8),
    _WlanControllerRadioTxPower_Type()
)
wlanControllerRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioTxPower.setStatus("current")
_WlanControllerAPVAPTable_Object = MibTable
wlanControllerAPVAPTable = _WlanControllerAPVAPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13)
)
if mibBuilder.loadTexts:
    wlanControllerAPVAPTable.setStatus("current")
_WlanControllerAPVAPEntry_Object = MibTableRow
wlanControllerAPVAPEntry = _WlanControllerAPVAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1)
)
wlanControllerAPVAPEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerRadioVAPIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerAPVAPEntry.setStatus("current")


class _WlanControllerRadioVAPIndex_Type(Integer32):
    """Custom type wlanControllerRadioVAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WlanControllerRadioVAPIndex_Type.__name__ = "Integer32"
_WlanControllerRadioVAPIndex_Object = MibTableColumn
wlanControllerRadioVAPIndex = _WlanControllerRadioVAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 1),
    _WlanControllerRadioVAPIndex_Type()
)
wlanControllerRadioVAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPIndex.setStatus("current")
_WlanControllerRadioVAPSSIDName_Type = OctetString
_WlanControllerRadioVAPSSIDName_Object = MibTableColumn
wlanControllerRadioVAPSSIDName = _WlanControllerRadioVAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 2),
    _WlanControllerRadioVAPSSIDName_Type()
)
wlanControllerRadioVAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPSSIDName.setStatus("current")


class _WlanControllerRadioVAPVLANID_Type(Integer32):
    """Custom type wlanControllerRadioVAPVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WlanControllerRadioVAPVLANID_Type.__name__ = "Integer32"
_WlanControllerRadioVAPVLANID_Object = MibTableColumn
wlanControllerRadioVAPVLANID = _WlanControllerRadioVAPVLANID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 3),
    _WlanControllerRadioVAPVLANID_Type()
)
wlanControllerRadioVAPVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPVLANID.setStatus("current")
_WlanControllerRadioVAPSecMode_Type = OctetString
_WlanControllerRadioVAPSecMode_Object = MibTableColumn
wlanControllerRadioVAPSecMode = _WlanControllerRadioVAPSecMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 13, 1, 4),
    _WlanControllerRadioVAPSecMode_Type()
)
wlanControllerRadioVAPSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerRadioVAPSecMode.setStatus("current")
_WlanControllerStationTable_Object = MibTable
wlanControllerStationTable = _WlanControllerStationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14)
)
if mibBuilder.loadTexts:
    wlanControllerStationTable.setStatus("current")
_WlanControllerStationEntry_Object = MibTableRow
wlanControllerStationEntry = _WlanControllerStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1)
)
wlanControllerStationEntry.setIndexNames(
    (0, "ZYXEL-ES-WIRELESS", "wlanControllerStationIndex"),
)
if mibBuilder.loadTexts:
    wlanControllerStationEntry.setStatus("current")


class _WlanControllerStationIndex_Type(Integer32):
    """Custom type wlanControllerStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WlanControllerStationIndex_Type.__name__ = "Integer32"
_WlanControllerStationIndex_Object = MibTableColumn
wlanControllerStationIndex = _WlanControllerStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 1),
    _WlanControllerStationIndex_Type()
)
wlanControllerStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationIndex.setStatus("current")


class _WlanControllerStationMacAddress_Type(OctetString):
    """Custom type wlanControllerStationMacAddress based on OctetString"""
    defaultValue = OctetString("public")


_WlanControllerStationMacAddress_Type.__name__ = "OctetString"
_WlanControllerStationMacAddress_Object = MibTableColumn
wlanControllerStationMacAddress = _WlanControllerStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 2),
    _WlanControllerStationMacAddress_Type()
)
wlanControllerStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationMacAddress.setStatus("current")
_WlanControllerStationAssociatedTime_Type = OctetString
_WlanControllerStationAssociatedTime_Object = MibTableColumn
wlanControllerStationAssociatedTime = _WlanControllerStationAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 3),
    _WlanControllerStationAssociatedTime_Type()
)
wlanControllerStationAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationAssociatedTime.setStatus("current")
_WlanControllerStationSSID_Type = OctetString
_WlanControllerStationSSID_Object = MibTableColumn
wlanControllerStationSSID = _WlanControllerStationSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 4),
    _WlanControllerStationSSID_Type()
)
wlanControllerStationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationSSID.setStatus("current")
_WlanControllerStationIPAddr_Type = IpAddress
_WlanControllerStationIPAddr_Object = MibTableColumn
wlanControllerStationIPAddr = _WlanControllerStationIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 5),
    _WlanControllerStationIPAddr_Type()
)
wlanControllerStationIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationIPAddr.setStatus("current")
_WlanControllerStationAssociatedAPMac_Type = OctetString
_WlanControllerStationAssociatedAPMac_Object = MibTableColumn
wlanControllerStationAssociatedAPMac = _WlanControllerStationAssociatedAPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 6),
    _WlanControllerStationAssociatedAPMac_Type()
)
wlanControllerStationAssociatedAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationAssociatedAPMac.setStatus("current")
_WlanControllerStationSignalStrength_Type = OctetString
_WlanControllerStationSignalStrength_Object = MibTableColumn
wlanControllerStationSignalStrength = _WlanControllerStationSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 7),
    _WlanControllerStationSignalStrength_Type()
)
wlanControllerStationSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationSignalStrength.setStatus("current")
_WlanControllerStationTxPkt_Type = Counter32
_WlanControllerStationTxPkt_Object = MibTableColumn
wlanControllerStationTxPkt = _WlanControllerStationTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 8),
    _WlanControllerStationTxPkt_Type()
)
wlanControllerStationTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationTxPkt.setStatus("current")
_WlanControllerStationRxPkt_Type = Counter32
_WlanControllerStationRxPkt_Object = MibTableColumn
wlanControllerStationRxPkt = _WlanControllerStationRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 14, 1, 9),
    _WlanControllerStationRxPkt_Type()
)
wlanControllerStationRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanControllerStationRxPkt.setStatus("current")
_WlanTotalStationCount_Type = Integer32
_WlanTotalStationCount_Object = MibScalar
wlanTotalStationCount = _WlanTotalStationCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 15),
    _WlanTotalStationCount_Type()
)
wlanTotalStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanTotalStationCount.setStatus("current")

# Managed Objects groups


# Notification objects

wlanStaAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    wlanStaAssociation.setStatus(
        "current"
    )

wlanStaDisassociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3, 2)
)
if mibBuilder.loadTexts:
    wlanStaDisassociation.setStatus(
        "current"
    )

wlanStaAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 3, 3)
)
if mibBuilder.loadTexts:
    wlanStaAuthFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-WIRELESS",
    **{"esWireless": esWireless,
       "wlanRadioTable": wlanRadioTable,
       "wlanRadioEntry": wlanRadioEntry,
       "wlanCurrentChannel": wlanCurrentChannel,
       "wlanStationCount": wlanStationCount,
       "wlanSupportedChannel": wlanSupportedChannel,
       "wlanMode": wlanMode,
       "wlanChannel": wlanChannel,
       "wlanRadioIndex": wlanRadioIndex,
       "wlanStationTable": wlanStationTable,
       "wlanStationEntry": wlanStationEntry,
       "stationIndex": stationIndex,
       "stationMacAddress": stationMacAddress,
       "stationAssociatedTime": stationAssociatedTime,
       "stationSSID": stationSSID,
       "stationSignalStrength": stationSignalStrength,
       "wlanStatisticsTable": wlanStatisticsTable,
       "wlanStatisticsEntry": wlanStatisticsEntry,
       "dot11FailedCount": dot11FailedCount,
       "dot11RetryCount": dot11RetryCount,
       "dot11ACKFailureCount": dot11ACKFailureCount,
       "dot11ReceivedFragmentCount": dot11ReceivedFragmentCount,
       "dot11TransmittedFrameCount": dot11TransmittedFrameCount,
       "dot11ReceivedPktCount": dot11ReceivedPktCount,
       "dot11TransmittedPktCount": dot11TransmittedPktCount,
       "wlanStatisticsIndex": wlanStatisticsIndex,
       "wlanTraps": wlanTraps,
       "trapsControl": trapsControl,
       "wlanTrapsControl": wlanTrapsControl,
       "trapsFormat": trapsFormat,
       "trapGenericMessage": trapGenericMessage,
       "trapMACAddress": trapMACAddress,
       "trapWlanSSID": trapWlanSSID,
       "trapsItems": trapsItems,
       "wlanStaAssociation": wlanStaAssociation,
       "wlanStaDisassociation": wlanStaDisassociation,
       "wlanStaAuthFail": wlanStaAuthFail,
       "wlanControllerAPTable": wlanControllerAPTable,
       "wlanControllerAPEntry": wlanControllerAPEntry,
       "wlanControllerAPIndex": wlanControllerAPIndex,
       "wlanControllerAPMac": wlanControllerAPMac,
       "wlanControllerAPDescription": wlanControllerAPDescription,
       "wlanControllerAPMgmtIPAddr": wlanControllerAPMgmtIPAddr,
       "wlanControllerAPStationNum": wlanControllerAPStationNum,
       "wlanControllerAPRadioTable": wlanControllerAPRadioTable,
       "wlanControllerAPRadioEntry": wlanControllerAPRadioEntry,
       "wlanControllerRadioIndex": wlanControllerRadioIndex,
       "wlanControllerRadioStationNum": wlanControllerRadioStationNum,
       "wlanControllerRadioCurrentChannel": wlanControllerRadioCurrentChannel,
       "wlanControllerRadioOperationMode": wlanControllerRadioOperationMode,
       "wlanControllerRadioBand": wlanControllerRadioBand,
       "wlanControllerRadioTxPkt": wlanControllerRadioTxPkt,
       "wlanControllerRadioRxPkt": wlanControllerRadioRxPkt,
       "wlanControllerRadioTxPower": wlanControllerRadioTxPower,
       "wlanControllerAPVAPTable": wlanControllerAPVAPTable,
       "wlanControllerAPVAPEntry": wlanControllerAPVAPEntry,
       "wlanControllerRadioVAPIndex": wlanControllerRadioVAPIndex,
       "wlanControllerRadioVAPSSIDName": wlanControllerRadioVAPSSIDName,
       "wlanControllerRadioVAPVLANID": wlanControllerRadioVAPVLANID,
       "wlanControllerRadioVAPSecMode": wlanControllerRadioVAPSecMode,
       "wlanControllerStationTable": wlanControllerStationTable,
       "wlanControllerStationEntry": wlanControllerStationEntry,
       "wlanControllerStationIndex": wlanControllerStationIndex,
       "wlanControllerStationMacAddress": wlanControllerStationMacAddress,
       "wlanControllerStationAssociatedTime": wlanControllerStationAssociatedTime,
       "wlanControllerStationSSID": wlanControllerStationSSID,
       "wlanControllerStationIPAddr": wlanControllerStationIPAddr,
       "wlanControllerStationAssociatedAPMac": wlanControllerStationAssociatedAPMac,
       "wlanControllerStationSignalStrength": wlanControllerStationSignalStrength,
       "wlanControllerStationTxPkt": wlanControllerStationTxPkt,
       "wlanControllerStationRxPkt": wlanControllerStationRxPkt,
       "wlanTotalStationCount": wlanTotalStationCount}
)
