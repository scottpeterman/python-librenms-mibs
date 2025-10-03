# SNMP MIB module (SL-SONET-SUP-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-SONET-SUP-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:10 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slSonetMib,) = mibBuilder.importSymbols(
    "SL-SONET-MIB",
    "slSonetMib")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(sonetFarEndLineCurrentEntry,
 sonetFarEndLineIntervalEntry,
 sonetFarEndPathCurrentEntry,
 sonetFarEndPathIntervalEntry,
 sonetFarEndVTCurrentEntry,
 sonetFarEndVTIntervalEntry,
 sonetLineCurrentEntry,
 sonetLineIntervalEntry,
 sonetMediumEntry,
 sonetPathCurrentEntry,
 sonetPathIntervalEntry,
 sonetSectionCurrentEntry,
 sonetSectionIntervalEntry,
 sonetVTCurrentEntry,
 sonetVTIntervalEntry) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetFarEndLineCurrentEntry",
    "sonetFarEndLineIntervalEntry",
    "sonetFarEndPathCurrentEntry",
    "sonetFarEndPathIntervalEntry",
    "sonetFarEndVTCurrentEntry",
    "sonetFarEndVTIntervalEntry",
    "sonetLineCurrentEntry",
    "sonetLineIntervalEntry",
    "sonetMediumEntry",
    "sonetPathCurrentEntry",
    "sonetPathIntervalEntry",
    "sonetSectionCurrentEntry",
    "sonetSectionIntervalEntry",
    "sonetVTCurrentEntry",
    "sonetVTIntervalEntry")


# MODULE-IDENTITY

sonetSupPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetSupObjects_ObjectIdentity = ObjectIdentity
sonetSupObjects = _SonetSupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1)
)
_SonetSupConfig_ObjectIdentity = ObjectIdentity
sonetSupConfig = _SonetSupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 1)
)
_SonetSupMedium_ObjectIdentity = ObjectIdentity
sonetSupMedium = _SonetSupMedium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 2)
)
_SonetSupSection_ObjectIdentity = ObjectIdentity
sonetSupSection = _SonetSupSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3)
)
_SonetSectionDefaultThresholdTable_Object = MibTable
sonetSectionDefaultThresholdTable = _SonetSectionDefaultThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sonetSectionDefaultThresholdTable.setStatus("current")
_SonetSectionDefaultThresholdEntry_Object = MibTableRow
sonetSectionDefaultThresholdEntry = _SonetSectionDefaultThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1)
)
sonetSectionDefaultThresholdEntry.setIndexNames(
    (0, "SL-SONET-SUP-PM-MIB", "sonetSectionDefaultThresholdRate"),
)
if mibBuilder.loadTexts:
    sonetSectionDefaultThresholdEntry.setStatus("current")


class _SonetSectionDefaultThresholdRate_Type(Integer32):
    """Custom type sonetSectionDefaultThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("oc1", 1),
          ("oc3", 2),
          ("oc12", 3),
          ("oc24", 4),
          ("oc48", 5),
          ("oc192", 6))
    )


_SonetSectionDefaultThresholdRate_Type.__name__ = "Integer32"
_SonetSectionDefaultThresholdRate_Object = MibTableColumn
sonetSectionDefaultThresholdRate = _SonetSectionDefaultThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 1),
    _SonetSectionDefaultThresholdRate_Type()
)
sonetSectionDefaultThresholdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDefaultThresholdRate.setStatus("current")
_SonetSectionDefaultCVThreshold_Type = Integer32
_SonetSectionDefaultCVThreshold_Object = MibTableColumn
sonetSectionDefaultCVThreshold = _SonetSectionDefaultCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 2),
    _SonetSectionDefaultCVThreshold_Type()
)
sonetSectionDefaultCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultCVThreshold.setStatus("current")
_SonetSectionDefaultESThreshold_Type = Integer32
_SonetSectionDefaultESThreshold_Object = MibTableColumn
sonetSectionDefaultESThreshold = _SonetSectionDefaultESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 3),
    _SonetSectionDefaultESThreshold_Type()
)
sonetSectionDefaultESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultESThreshold.setStatus("current")
_SonetSectionDefaultSESThreshold_Type = Integer32
_SonetSectionDefaultSESThreshold_Object = MibTableColumn
sonetSectionDefaultSESThreshold = _SonetSectionDefaultSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 6),
    _SonetSectionDefaultSESThreshold_Type()
)
sonetSectionDefaultSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultSESThreshold.setStatus("current")
_SonetSectionDefaultSEFSThreshold_Type = Integer32
_SonetSectionDefaultSEFSThreshold_Object = MibTableColumn
sonetSectionDefaultSEFSThreshold = _SonetSectionDefaultSEFSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 7),
    _SonetSectionDefaultSEFSThreshold_Type()
)
sonetSectionDefaultSEFSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultSEFSThreshold.setStatus("current")
_SonetSectionDefaultDayCVThreshold_Type = Integer32
_SonetSectionDefaultDayCVThreshold_Object = MibTableColumn
sonetSectionDefaultDayCVThreshold = _SonetSectionDefaultDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 8),
    _SonetSectionDefaultDayCVThreshold_Type()
)
sonetSectionDefaultDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultDayCVThreshold.setStatus("current")
_SonetSectionDefaultDayESThreshold_Type = Integer32
_SonetSectionDefaultDayESThreshold_Object = MibTableColumn
sonetSectionDefaultDayESThreshold = _SonetSectionDefaultDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 9),
    _SonetSectionDefaultDayESThreshold_Type()
)
sonetSectionDefaultDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultDayESThreshold.setStatus("current")
_SonetSectionDefaultDaySESThreshold_Type = Integer32
_SonetSectionDefaultDaySESThreshold_Object = MibTableColumn
sonetSectionDefaultDaySESThreshold = _SonetSectionDefaultDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 12),
    _SonetSectionDefaultDaySESThreshold_Type()
)
sonetSectionDefaultDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultDaySESThreshold.setStatus("current")
_SonetSectionDefaultDaySEFSThreshold_Type = Integer32
_SonetSectionDefaultDaySEFSThreshold_Object = MibTableColumn
sonetSectionDefaultDaySEFSThreshold = _SonetSectionDefaultDaySEFSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 1, 1, 13),
    _SonetSectionDefaultDaySEFSThreshold_Type()
)
sonetSectionDefaultDaySEFSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDefaultDaySEFSThreshold.setStatus("current")
_SonetSectionThresholdTable_Object = MibTable
sonetSectionThresholdTable = _SonetSectionThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonetSectionThresholdTable.setStatus("current")
_SonetSectionThresholdEntry_Object = MibTableRow
sonetSectionThresholdEntry = _SonetSectionThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sonetSectionThresholdEntry.setStatus("current")


class _SonetSectionCurrentCVThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentCVThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionCurrentCVThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentCVThreshold_Object = MibTableColumn
sonetSectionCurrentCVThreshold = _SonetSectionCurrentCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 1),
    _SonetSectionCurrentCVThreshold_Type()
)
sonetSectionCurrentCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentCVThreshold.setStatus("current")


class _SonetSectionCurrentESThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentESThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionCurrentESThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentESThreshold_Object = MibTableColumn
sonetSectionCurrentESThreshold = _SonetSectionCurrentESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 2),
    _SonetSectionCurrentESThreshold_Type()
)
sonetSectionCurrentESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentESThreshold.setStatus("current")


class _SonetSectionCurrentSESThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentSESThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionCurrentSESThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentSESThreshold_Object = MibTableColumn
sonetSectionCurrentSESThreshold = _SonetSectionCurrentSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 5),
    _SonetSectionCurrentSESThreshold_Type()
)
sonetSectionCurrentSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentSESThreshold.setStatus("current")


class _SonetSectionCurrentSEFSThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentSEFSThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionCurrentSEFSThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentSEFSThreshold_Object = MibTableColumn
sonetSectionCurrentSEFSThreshold = _SonetSectionCurrentSEFSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 6),
    _SonetSectionCurrentSEFSThreshold_Type()
)
sonetSectionCurrentSEFSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentSEFSThreshold.setStatus("current")


class _SonetSectionDayCVThreshold_Type(Integer32):
    """Custom type sonetSectionDayCVThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionDayCVThreshold_Type.__name__ = "Integer32"
_SonetSectionDayCVThreshold_Object = MibTableColumn
sonetSectionDayCVThreshold = _SonetSectionDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 7),
    _SonetSectionDayCVThreshold_Type()
)
sonetSectionDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDayCVThreshold.setStatus("current")


class _SonetSectionDayESThreshold_Type(Integer32):
    """Custom type sonetSectionDayESThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionDayESThreshold_Type.__name__ = "Integer32"
_SonetSectionDayESThreshold_Object = MibTableColumn
sonetSectionDayESThreshold = _SonetSectionDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 8),
    _SonetSectionDayESThreshold_Type()
)
sonetSectionDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDayESThreshold.setStatus("current")


class _SonetSectionDaySESThreshold_Type(Integer32):
    """Custom type sonetSectionDaySESThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionDaySESThreshold_Type.__name__ = "Integer32"
_SonetSectionDaySESThreshold_Object = MibTableColumn
sonetSectionDaySESThreshold = _SonetSectionDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 11),
    _SonetSectionDaySESThreshold_Type()
)
sonetSectionDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDaySESThreshold.setStatus("current")


class _SonetSectionDaySEFSThreshold_Type(Integer32):
    """Custom type sonetSectionDaySEFSThreshold based on Integer32"""
    defaultValue = 0


_SonetSectionDaySEFSThreshold_Type.__name__ = "Integer32"
_SonetSectionDaySEFSThreshold_Object = MibTableColumn
sonetSectionDaySEFSThreshold = _SonetSectionDaySEFSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 2, 1, 12),
    _SonetSectionDaySEFSThreshold_Type()
)
sonetSectionDaySEFSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDaySEFSThreshold.setStatus("current")
_SonetSectionDayTable_Object = MibTable
sonetSectionDayTable = _SonetSectionDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15)
)
if mibBuilder.loadTexts:
    sonetSectionDayTable.setStatus("current")
_SonetSectionDayEntry_Object = MibTableRow
sonetSectionDayEntry = _SonetSectionDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1)
)
sonetSectionDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetSectionDayNumber"),
)
if mibBuilder.loadTexts:
    sonetSectionDayEntry.setStatus("current")


class _SonetSectionDayNumber_Type(Integer32):
    """Custom type sonetSectionDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_SonetSectionDayNumber_Type.__name__ = "Integer32"
_SonetSectionDayNumber_Object = MibTableColumn
sonetSectionDayNumber = _SonetSectionDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 1),
    _SonetSectionDayNumber_Type()
)
sonetSectionDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDayNumber.setStatus("current")
_SonetSectionDayStartTime_Type = DateAndTime
_SonetSectionDayStartTime_Object = MibTableColumn
sonetSectionDayStartTime = _SonetSectionDayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 2),
    _SonetSectionDayStartTime_Type()
)
sonetSectionDayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDayStartTime.setStatus("current")
_SonetSectionDayValidData_Type = TruthValue
_SonetSectionDayValidData_Object = MibTableColumn
sonetSectionDayValidData = _SonetSectionDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 3),
    _SonetSectionDayValidData_Type()
)
sonetSectionDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDayValidData.setStatus("current")
_SonetSectionDayCVs_Type = PerfTotalCount
_SonetSectionDayCVs_Object = MibTableColumn
sonetSectionDayCVs = _SonetSectionDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 4),
    _SonetSectionDayCVs_Type()
)
sonetSectionDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDayCVs.setStatus("current")
_SonetSectionDayESs_Type = PerfTotalCount
_SonetSectionDayESs_Object = MibTableColumn
sonetSectionDayESs = _SonetSectionDayESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 5),
    _SonetSectionDayESs_Type()
)
sonetSectionDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDayESs.setStatus("current")
_SonetSectionDaySESs_Type = PerfTotalCount
_SonetSectionDaySESs_Object = MibTableColumn
sonetSectionDaySESs = _SonetSectionDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 8),
    _SonetSectionDaySESs_Type()
)
sonetSectionDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDaySESs.setStatus("current")
_SonetSectionDaySEFSs_Type = PerfTotalCount
_SonetSectionDaySEFSs_Object = MibTableColumn
sonetSectionDaySEFSs = _SonetSectionDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 9),
    _SonetSectionDaySEFSs_Type()
)
sonetSectionDaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDaySEFSs.setStatus("current")
_SonetSectionDayTcaFlag_Type = TruthValue
_SonetSectionDayTcaFlag_Object = MibTableColumn
sonetSectionDayTcaFlag = _SonetSectionDayTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 10),
    _SonetSectionDayTcaFlag_Type()
)
sonetSectionDayTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDayTcaFlag.setStatus("current")
_SonetSectionDayReset_Type = Integer32
_SonetSectionDayReset_Object = MibTableColumn
sonetSectionDayReset = _SonetSectionDayReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 3, 15, 1, 11),
    _SonetSectionDayReset_Type()
)
sonetSectionDayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDayReset.setStatus("current")
_SonetSupLine_ObjectIdentity = ObjectIdentity
sonetSupLine = _SonetSupLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4)
)
_SonetLineDefaultThresholdTable_Object = MibTable
sonetLineDefaultThresholdTable = _SonetLineDefaultThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sonetLineDefaultThresholdTable.setStatus("current")
_SonetLineDefaultThresholdEntry_Object = MibTableRow
sonetLineDefaultThresholdEntry = _SonetLineDefaultThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1)
)
sonetLineDefaultThresholdEntry.setIndexNames(
    (0, "SL-SONET-SUP-PM-MIB", "sonetLineDefaultThresholdDirection"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetLineDefaultThresholdRate"),
)
if mibBuilder.loadTexts:
    sonetLineDefaultThresholdEntry.setStatus("current")


class _SonetLineDefaultThresholdDirection_Type(Integer32):
    """Custom type sonetLineDefaultThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nearEnd", 1),
          ("farEnd", 2))
    )


_SonetLineDefaultThresholdDirection_Type.__name__ = "Integer32"
_SonetLineDefaultThresholdDirection_Object = MibTableColumn
sonetLineDefaultThresholdDirection = _SonetLineDefaultThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 1),
    _SonetLineDefaultThresholdDirection_Type()
)
sonetLineDefaultThresholdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDefaultThresholdDirection.setStatus("current")


class _SonetLineDefaultThresholdRate_Type(Integer32):
    """Custom type sonetLineDefaultThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("vt1dot5", 1),
          ("vtg", 2),
          ("oc1", 3),
          ("oc3", 4),
          ("oc12", 5),
          ("oc24", 6),
          ("oc48", 7),
          ("oc192", 8))
    )


_SonetLineDefaultThresholdRate_Type.__name__ = "Integer32"
_SonetLineDefaultThresholdRate_Object = MibTableColumn
sonetLineDefaultThresholdRate = _SonetLineDefaultThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 2),
    _SonetLineDefaultThresholdRate_Type()
)
sonetLineDefaultThresholdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDefaultThresholdRate.setStatus("current")
_SonetLineDefaultCVThreshold_Type = Integer32
_SonetLineDefaultCVThreshold_Object = MibTableColumn
sonetLineDefaultCVThreshold = _SonetLineDefaultCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 3),
    _SonetLineDefaultCVThreshold_Type()
)
sonetLineDefaultCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultCVThreshold.setStatus("current")
_SonetLineDefaultESThreshold_Type = Integer32
_SonetLineDefaultESThreshold_Object = MibTableColumn
sonetLineDefaultESThreshold = _SonetLineDefaultESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 4),
    _SonetLineDefaultESThreshold_Type()
)
sonetLineDefaultESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultESThreshold.setStatus("current")
_SonetLineDefaultSESThreshold_Type = Integer32
_SonetLineDefaultSESThreshold_Object = MibTableColumn
sonetLineDefaultSESThreshold = _SonetLineDefaultSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 7),
    _SonetLineDefaultSESThreshold_Type()
)
sonetLineDefaultSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultSESThreshold.setStatus("current")
_SonetLineDefaultUASThreshold_Type = Integer32
_SonetLineDefaultUASThreshold_Object = MibTableColumn
sonetLineDefaultUASThreshold = _SonetLineDefaultUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 9),
    _SonetLineDefaultUASThreshold_Type()
)
sonetLineDefaultUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultUASThreshold.setStatus("current")
_SonetLineDefaultDayCVThreshold_Type = Integer32
_SonetLineDefaultDayCVThreshold_Object = MibTableColumn
sonetLineDefaultDayCVThreshold = _SonetLineDefaultDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 10),
    _SonetLineDefaultDayCVThreshold_Type()
)
sonetLineDefaultDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultDayCVThreshold.setStatus("current")
_SonetLineDefaultDayESThreshold_Type = Integer32
_SonetLineDefaultDayESThreshold_Object = MibTableColumn
sonetLineDefaultDayESThreshold = _SonetLineDefaultDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 11),
    _SonetLineDefaultDayESThreshold_Type()
)
sonetLineDefaultDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultDayESThreshold.setStatus("current")
_SonetLineDefaultDaySESThreshold_Type = Integer32
_SonetLineDefaultDaySESThreshold_Object = MibTableColumn
sonetLineDefaultDaySESThreshold = _SonetLineDefaultDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 14),
    _SonetLineDefaultDaySESThreshold_Type()
)
sonetLineDefaultDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultDaySESThreshold.setStatus("current")
_SonetLineDefaultDayUASThreshold_Type = Integer32
_SonetLineDefaultDayUASThreshold_Object = MibTableColumn
sonetLineDefaultDayUASThreshold = _SonetLineDefaultDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 1, 1, 16),
    _SonetLineDefaultDayUASThreshold_Type()
)
sonetLineDefaultDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDefaultDayUASThreshold.setStatus("current")
_SonetLineThresholdTable_Object = MibTable
sonetLineThresholdTable = _SonetLineThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sonetLineThresholdTable.setStatus("current")
_SonetLineThresholdEntry_Object = MibTableRow
sonetLineThresholdEntry = _SonetLineThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1)
)
sonetLineThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetLineThresholdDirection"),
)
if mibBuilder.loadTexts:
    sonetLineThresholdEntry.setStatus("current")


class _SonetLineThresholdDirection_Type(Integer32):
    """Custom type sonetLineThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nearEnd", 1),
          ("farEnd", 2))
    )


_SonetLineThresholdDirection_Type.__name__ = "Integer32"
_SonetLineThresholdDirection_Object = MibTableColumn
sonetLineThresholdDirection = _SonetLineThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 1),
    _SonetLineThresholdDirection_Type()
)
sonetLineThresholdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineThresholdDirection.setStatus("current")


class _SonetLineCurrentCVThreshold_Type(Integer32):
    """Custom type sonetLineCurrentCVThreshold based on Integer32"""
    defaultValue = 0


_SonetLineCurrentCVThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentCVThreshold_Object = MibTableColumn
sonetLineCurrentCVThreshold = _SonetLineCurrentCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 2),
    _SonetLineCurrentCVThreshold_Type()
)
sonetLineCurrentCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentCVThreshold.setStatus("current")


class _SonetLineCurrentESThreshold_Type(Integer32):
    """Custom type sonetLineCurrentESThreshold based on Integer32"""
    defaultValue = 0


_SonetLineCurrentESThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentESThreshold_Object = MibTableColumn
sonetLineCurrentESThreshold = _SonetLineCurrentESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 3),
    _SonetLineCurrentESThreshold_Type()
)
sonetLineCurrentESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentESThreshold.setStatus("current")


class _SonetLineCurrentSESThreshold_Type(Integer32):
    """Custom type sonetLineCurrentSESThreshold based on Integer32"""
    defaultValue = 0


_SonetLineCurrentSESThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentSESThreshold_Object = MibTableColumn
sonetLineCurrentSESThreshold = _SonetLineCurrentSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 4),
    _SonetLineCurrentSESThreshold_Type()
)
sonetLineCurrentSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentSESThreshold.setStatus("current")


class _SonetLineCurrentUASThreshold_Type(Integer32):
    """Custom type sonetLineCurrentUASThreshold based on Integer32"""
    defaultValue = 0


_SonetLineCurrentUASThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentUASThreshold_Object = MibTableColumn
sonetLineCurrentUASThreshold = _SonetLineCurrentUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 5),
    _SonetLineCurrentUASThreshold_Type()
)
sonetLineCurrentUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentUASThreshold.setStatus("current")


class _SonetLineDayCVThreshold_Type(Integer32):
    """Custom type sonetLineDayCVThreshold based on Integer32"""
    defaultValue = 0


_SonetLineDayCVThreshold_Type.__name__ = "Integer32"
_SonetLineDayCVThreshold_Object = MibTableColumn
sonetLineDayCVThreshold = _SonetLineDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 6),
    _SonetLineDayCVThreshold_Type()
)
sonetLineDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDayCVThreshold.setStatus("current")


class _SonetLineDayESThreshold_Type(Integer32):
    """Custom type sonetLineDayESThreshold based on Integer32"""
    defaultValue = 0


_SonetLineDayESThreshold_Type.__name__ = "Integer32"
_SonetLineDayESThreshold_Object = MibTableColumn
sonetLineDayESThreshold = _SonetLineDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 7),
    _SonetLineDayESThreshold_Type()
)
sonetLineDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDayESThreshold.setStatus("current")


class _SonetLineDaySESThreshold_Type(Integer32):
    """Custom type sonetLineDaySESThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonetLineDaySESThreshold_Type.__name__ = "Integer32"
_SonetLineDaySESThreshold_Object = MibTableColumn
sonetLineDaySESThreshold = _SonetLineDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 8),
    _SonetLineDaySESThreshold_Type()
)
sonetLineDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDaySESThreshold.setStatus("current")


class _SonetLineDayUASThreshold_Type(Integer32):
    """Custom type sonetLineDayUASThreshold based on Integer32"""
    defaultValue = 0


_SonetLineDayUASThreshold_Type.__name__ = "Integer32"
_SonetLineDayUASThreshold_Object = MibTableColumn
sonetLineDayUASThreshold = _SonetLineDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 2, 1, 9),
    _SonetLineDayUASThreshold_Type()
)
sonetLineDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDayUASThreshold.setStatus("current")
_SonetLineDayTable_Object = MibTable
sonetLineDayTable = _SonetLineDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5)
)
if mibBuilder.loadTexts:
    sonetLineDayTable.setStatus("current")
_SonetLineDayEntry_Object = MibTableRow
sonetLineDayEntry = _SonetLineDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1)
)
sonetLineDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetLineDayNumber"),
)
if mibBuilder.loadTexts:
    sonetLineDayEntry.setStatus("current")


class _SonetLineDayNumber_Type(Integer32):
    """Custom type sonetLineDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_SonetLineDayNumber_Type.__name__ = "Integer32"
_SonetLineDayNumber_Object = MibTableColumn
sonetLineDayNumber = _SonetLineDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 1),
    _SonetLineDayNumber_Type()
)
sonetLineDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayNumber.setStatus("current")
_SonetLineDayStartTime_Type = DateAndTime
_SonetLineDayStartTime_Object = MibTableColumn
sonetLineDayStartTime = _SonetLineDayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 2),
    _SonetLineDayStartTime_Type()
)
sonetLineDayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayStartTime.setStatus("current")
_SonetLineDayValidData_Type = TruthValue
_SonetLineDayValidData_Object = MibTableColumn
sonetLineDayValidData = _SonetLineDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 3),
    _SonetLineDayValidData_Type()
)
sonetLineDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayValidData.setStatus("current")
_SonetLineDayCVs_Type = PerfTotalCount
_SonetLineDayCVs_Object = MibTableColumn
sonetLineDayCVs = _SonetLineDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 5),
    _SonetLineDayCVs_Type()
)
sonetLineDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayCVs.setStatus("current")
_SonetLineDayESs_Type = PerfTotalCount
_SonetLineDayESs_Object = MibTableColumn
sonetLineDayESs = _SonetLineDayESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 6),
    _SonetLineDayESs_Type()
)
sonetLineDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayESs.setStatus("current")
_SonetLineDaySESs_Type = PerfTotalCount
_SonetLineDaySESs_Object = MibTableColumn
sonetLineDaySESs = _SonetLineDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 9),
    _SonetLineDaySESs_Type()
)
sonetLineDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDaySESs.setStatus("current")
_SonetLineDayUASs_Type = PerfTotalCount
_SonetLineDayUASs_Object = MibTableColumn
sonetLineDayUASs = _SonetLineDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 10),
    _SonetLineDayUASs_Type()
)
sonetLineDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayUASs.setStatus("current")
_SonetLineDayPSC_Type = PerfTotalCount
_SonetLineDayPSC_Object = MibTableColumn
sonetLineDayPSC = _SonetLineDayPSC_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 11),
    _SonetLineDayPSC_Type()
)
sonetLineDayPSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayPSC.setStatus("current")
_SonetLineDayPSD_Type = PerfTotalCount
_SonetLineDayPSD_Object = MibTableColumn
sonetLineDayPSD = _SonetLineDayPSD_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 12),
    _SonetLineDayPSD_Type()
)
sonetLineDayPSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayPSD.setStatus("current")
_SonetLineDayFCs_Type = PerfTotalCount
_SonetLineDayFCs_Object = MibTableColumn
sonetLineDayFCs = _SonetLineDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 13),
    _SonetLineDayFCs_Type()
)
sonetLineDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayFCs.setStatus("current")
_SonetLineDayTcaFlag_Type = TruthValue
_SonetLineDayTcaFlag_Object = MibTableColumn
sonetLineDayTcaFlag = _SonetLineDayTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 14),
    _SonetLineDayTcaFlag_Type()
)
sonetLineDayTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineDayTcaFlag.setStatus("current")
_SonetLineDayReset_Type = Integer32
_SonetLineDayReset_Object = MibTableColumn
sonetLineDayReset = _SonetLineDayReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 4, 5, 1, 15),
    _SonetLineDayReset_Type()
)
sonetLineDayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDayReset.setStatus("current")
_SonetSupFarEndLine_ObjectIdentity = ObjectIdentity
sonetSupFarEndLine = _SonetSupFarEndLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5)
)
_SonetFarEndLineDayTable_Object = MibTable
sonetFarEndLineDayTable = _SonetFarEndLineDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    sonetFarEndLineDayTable.setStatus("current")
_SonetFarEndLineDayEntry_Object = MibTableRow
sonetFarEndLineDayEntry = _SonetFarEndLineDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1)
)
sonetFarEndLineDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetFarEndLineDayNumber"),
)
if mibBuilder.loadTexts:
    sonetFarEndLineDayEntry.setStatus("current")


class _SonetFarEndLineDayNumber_Type(Integer32):
    """Custom type sonetFarEndLineDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_SonetFarEndLineDayNumber_Type.__name__ = "Integer32"
_SonetFarEndLineDayNumber_Object = MibTableColumn
sonetFarEndLineDayNumber = _SonetFarEndLineDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 1),
    _SonetFarEndLineDayNumber_Type()
)
sonetFarEndLineDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayNumber.setStatus("current")
_SonetFarEndLineDayStartTime_Type = DateAndTime
_SonetFarEndLineDayStartTime_Object = MibTableColumn
sonetFarEndLineDayStartTime = _SonetFarEndLineDayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 2),
    _SonetFarEndLineDayStartTime_Type()
)
sonetFarEndLineDayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayStartTime.setStatus("current")
_SonetFarEndLineDayValidData_Type = TruthValue
_SonetFarEndLineDayValidData_Object = MibTableColumn
sonetFarEndLineDayValidData = _SonetFarEndLineDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 3),
    _SonetFarEndLineDayValidData_Type()
)
sonetFarEndLineDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayValidData.setStatus("current")
_SonetFarEndLineDayCVs_Type = PerfTotalCount
_SonetFarEndLineDayCVs_Object = MibTableColumn
sonetFarEndLineDayCVs = _SonetFarEndLineDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 5),
    _SonetFarEndLineDayCVs_Type()
)
sonetFarEndLineDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayCVs.setStatus("current")
_SonetFarEndLineDayESs_Type = PerfTotalCount
_SonetFarEndLineDayESs_Object = MibTableColumn
sonetFarEndLineDayESs = _SonetFarEndLineDayESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 6),
    _SonetFarEndLineDayESs_Type()
)
sonetFarEndLineDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayESs.setStatus("current")
_SonetFarEndLineDaySESs_Type = PerfTotalCount
_SonetFarEndLineDaySESs_Object = MibTableColumn
sonetFarEndLineDaySESs = _SonetFarEndLineDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 9),
    _SonetFarEndLineDaySESs_Type()
)
sonetFarEndLineDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDaySESs.setStatus("current")
_SonetFarEndLineDayUASs_Type = PerfTotalCount
_SonetFarEndLineDayUASs_Object = MibTableColumn
sonetFarEndLineDayUASs = _SonetFarEndLineDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 10),
    _SonetFarEndLineDayUASs_Type()
)
sonetFarEndLineDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayUASs.setStatus("current")
_SonetFarEndLineDayFCs_Type = PerfTotalCount
_SonetFarEndLineDayFCs_Object = MibTableColumn
sonetFarEndLineDayFCs = _SonetFarEndLineDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 11),
    _SonetFarEndLineDayFCs_Type()
)
sonetFarEndLineDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayFCs.setStatus("current")
_SonetFarEndLineDayTcaFlag_Type = TruthValue
_SonetFarEndLineDayTcaFlag_Object = MibTableColumn
sonetFarEndLineDayTcaFlag = _SonetFarEndLineDayTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 12),
    _SonetFarEndLineDayTcaFlag_Type()
)
sonetFarEndLineDayTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineDayTcaFlag.setStatus("current")
_SonetFarEndLineDayReset_Type = Integer32
_SonetFarEndLineDayReset_Object = MibTableColumn
sonetFarEndLineDayReset = _SonetFarEndLineDayReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 5, 3, 1, 13),
    _SonetFarEndLineDayReset_Type()
)
sonetFarEndLineDayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFarEndLineDayReset.setStatus("current")
_SonetTrap_ObjectIdentity = ObjectIdentity
sonetTrap = _SonetTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 6)
)
_SonetCounterId_Type = ObjectIdentifier
_SonetCounterId_Object = MibScalar
sonetCounterId = _SonetCounterId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 6, 1),
    _SonetCounterId_Type()
)
sonetCounterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sonetCounterId.setStatus("current")
_SonetCounterValue_Type = Integer32
_SonetCounterValue_Object = MibScalar
sonetCounterValue = _SonetCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 6, 2),
    _SonetCounterValue_Type()
)
sonetCounterValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sonetCounterValue.setStatus("current")
_SonetSupObjectsPath_ObjectIdentity = ObjectIdentity
sonetSupObjectsPath = _SonetSupObjectsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2)
)
_SonetSupPath_ObjectIdentity = ObjectIdentity
sonetSupPath = _SonetSupPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1)
)
_SonetPathDefaultThresholdTable_Object = MibTable
sonetPathDefaultThresholdTable = _SonetPathDefaultThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sonetPathDefaultThresholdTable.setStatus("current")
_SonetPathDefaultThresholdEntry_Object = MibTableRow
sonetPathDefaultThresholdEntry = _SonetPathDefaultThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1)
)
sonetPathDefaultThresholdEntry.setIndexNames(
    (0, "SL-SONET-SUP-PM-MIB", "sonetPathDefaultThresholdDirection"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetPathDefaultThresholdRate"),
)
if mibBuilder.loadTexts:
    sonetPathDefaultThresholdEntry.setStatus("current")


class _SonetPathDefaultThresholdDirection_Type(Integer32):
    """Custom type sonetPathDefaultThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nearEnd", 1),
          ("farEnd", 2))
    )


_SonetPathDefaultThresholdDirection_Type.__name__ = "Integer32"
_SonetPathDefaultThresholdDirection_Object = MibTableColumn
sonetPathDefaultThresholdDirection = _SonetPathDefaultThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 1),
    _SonetPathDefaultThresholdDirection_Type()
)
sonetPathDefaultThresholdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDefaultThresholdDirection.setStatus("current")


class _SonetPathDefaultThresholdRate_Type(Integer32):
    """Custom type sonetPathDefaultThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sts1", 1),
          ("sts3", 2),
          ("sts12", 3),
          ("sts24", 4),
          ("sts48", 5),
          ("sts192", 6))
    )


_SonetPathDefaultThresholdRate_Type.__name__ = "Integer32"
_SonetPathDefaultThresholdRate_Object = MibTableColumn
sonetPathDefaultThresholdRate = _SonetPathDefaultThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 2),
    _SonetPathDefaultThresholdRate_Type()
)
sonetPathDefaultThresholdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDefaultThresholdRate.setStatus("current")
_SonetPathDefaultCVThreshold_Type = Integer32
_SonetPathDefaultCVThreshold_Object = MibTableColumn
sonetPathDefaultCVThreshold = _SonetPathDefaultCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 3),
    _SonetPathDefaultCVThreshold_Type()
)
sonetPathDefaultCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultCVThreshold.setStatus("current")
_SonetPathDefaultESThreshold_Type = Integer32
_SonetPathDefaultESThreshold_Object = MibTableColumn
sonetPathDefaultESThreshold = _SonetPathDefaultESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 4),
    _SonetPathDefaultESThreshold_Type()
)
sonetPathDefaultESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultESThreshold.setStatus("current")
_SonetPathDefaultSESThreshold_Type = Integer32
_SonetPathDefaultSESThreshold_Object = MibTableColumn
sonetPathDefaultSESThreshold = _SonetPathDefaultSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 7),
    _SonetPathDefaultSESThreshold_Type()
)
sonetPathDefaultSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultSESThreshold.setStatus("current")
_SonetPathDefaultUASThreshold_Type = Integer32
_SonetPathDefaultUASThreshold_Object = MibTableColumn
sonetPathDefaultUASThreshold = _SonetPathDefaultUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 8),
    _SonetPathDefaultUASThreshold_Type()
)
sonetPathDefaultUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultUASThreshold.setStatus("current")
_SonetPathDefaultDayCVThreshold_Type = Integer32
_SonetPathDefaultDayCVThreshold_Object = MibTableColumn
sonetPathDefaultDayCVThreshold = _SonetPathDefaultDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 16),
    _SonetPathDefaultDayCVThreshold_Type()
)
sonetPathDefaultDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultDayCVThreshold.setStatus("current")
_SonetPathDefaultDayESThreshold_Type = Integer32
_SonetPathDefaultDayESThreshold_Object = MibTableColumn
sonetPathDefaultDayESThreshold = _SonetPathDefaultDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 17),
    _SonetPathDefaultDayESThreshold_Type()
)
sonetPathDefaultDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultDayESThreshold.setStatus("current")
_SonetPathDefaultDaySESThreshold_Type = Integer32
_SonetPathDefaultDaySESThreshold_Object = MibTableColumn
sonetPathDefaultDaySESThreshold = _SonetPathDefaultDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 20),
    _SonetPathDefaultDaySESThreshold_Type()
)
sonetPathDefaultDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultDaySESThreshold.setStatus("current")
_SonetPathDefaultDayUASThreshold_Type = Integer32
_SonetPathDefaultDayUASThreshold_Object = MibTableColumn
sonetPathDefaultDayUASThreshold = _SonetPathDefaultDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 1, 1, 21),
    _SonetPathDefaultDayUASThreshold_Type()
)
sonetPathDefaultDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDefaultDayUASThreshold.setStatus("current")
_SonetPathThresholdTable_Object = MibTable
sonetPathThresholdTable = _SonetPathThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sonetPathThresholdTable.setStatus("current")
_SonetPathThresholdEntry_Object = MibTableRow
sonetPathThresholdEntry = _SonetPathThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1)
)
sonetPathThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetPathThresholdDirection"),
)
if mibBuilder.loadTexts:
    sonetPathThresholdEntry.setStatus("current")


class _SonetPathThresholdDirection_Type(Integer32):
    """Custom type sonetPathThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nearEnd", 1),
          ("farEnd", 2))
    )


_SonetPathThresholdDirection_Type.__name__ = "Integer32"
_SonetPathThresholdDirection_Object = MibTableColumn
sonetPathThresholdDirection = _SonetPathThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 1),
    _SonetPathThresholdDirection_Type()
)
sonetPathThresholdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathThresholdDirection.setStatus("current")


class _SonetPathCurrentCVThreshold_Type(Integer32):
    """Custom type sonetPathCurrentCVThreshold based on Integer32"""
    defaultValue = 0


_SonetPathCurrentCVThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentCVThreshold_Object = MibTableColumn
sonetPathCurrentCVThreshold = _SonetPathCurrentCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 2),
    _SonetPathCurrentCVThreshold_Type()
)
sonetPathCurrentCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentCVThreshold.setStatus("current")


class _SonetPathCurrentESThreshold_Type(Integer32):
    """Custom type sonetPathCurrentESThreshold based on Integer32"""
    defaultValue = 0


_SonetPathCurrentESThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentESThreshold_Object = MibTableColumn
sonetPathCurrentESThreshold = _SonetPathCurrentESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 3),
    _SonetPathCurrentESThreshold_Type()
)
sonetPathCurrentESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentESThreshold.setStatus("current")


class _SonetPathCurrentSESThreshold_Type(Integer32):
    """Custom type sonetPathCurrentSESThreshold based on Integer32"""
    defaultValue = 0


_SonetPathCurrentSESThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentSESThreshold_Object = MibTableColumn
sonetPathCurrentSESThreshold = _SonetPathCurrentSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 4),
    _SonetPathCurrentSESThreshold_Type()
)
sonetPathCurrentSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentSESThreshold.setStatus("current")


class _SonetPathCurrentUASThreshold_Type(Integer32):
    """Custom type sonetPathCurrentUASThreshold based on Integer32"""
    defaultValue = 0


_SonetPathCurrentUASThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentUASThreshold_Object = MibTableColumn
sonetPathCurrentUASThreshold = _SonetPathCurrentUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 5),
    _SonetPathCurrentUASThreshold_Type()
)
sonetPathCurrentUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentUASThreshold.setStatus("current")


class _SonetPathDayCVThreshold_Type(Integer32):
    """Custom type sonetPathDayCVThreshold based on Integer32"""
    defaultValue = 0


_SonetPathDayCVThreshold_Type.__name__ = "Integer32"
_SonetPathDayCVThreshold_Object = MibTableColumn
sonetPathDayCVThreshold = _SonetPathDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 6),
    _SonetPathDayCVThreshold_Type()
)
sonetPathDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDayCVThreshold.setStatus("current")


class _SonetPathDayESThreshold_Type(Integer32):
    """Custom type sonetPathDayESThreshold based on Integer32"""
    defaultValue = 0


_SonetPathDayESThreshold_Type.__name__ = "Integer32"
_SonetPathDayESThreshold_Object = MibTableColumn
sonetPathDayESThreshold = _SonetPathDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 7),
    _SonetPathDayESThreshold_Type()
)
sonetPathDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDayESThreshold.setStatus("current")


class _SonetPathDaySESThreshold_Type(Integer32):
    """Custom type sonetPathDaySESThreshold based on Integer32"""
    defaultValue = 0


_SonetPathDaySESThreshold_Type.__name__ = "Integer32"
_SonetPathDaySESThreshold_Object = MibTableColumn
sonetPathDaySESThreshold = _SonetPathDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 8),
    _SonetPathDaySESThreshold_Type()
)
sonetPathDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDaySESThreshold.setStatus("current")


class _SonetPathDayUASThreshold_Type(Integer32):
    """Custom type sonetPathDayUASThreshold based on Integer32"""
    defaultValue = 0


_SonetPathDayUASThreshold_Type.__name__ = "Integer32"
_SonetPathDayUASThreshold_Object = MibTableColumn
sonetPathDayUASThreshold = _SonetPathDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 2, 1, 9),
    _SonetPathDayUASThreshold_Type()
)
sonetPathDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDayUASThreshold.setStatus("current")
_SonetPathDayTable_Object = MibTable
sonetPathDayTable = _SonetPathDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17)
)
if mibBuilder.loadTexts:
    sonetPathDayTable.setStatus("current")
_SonetPathDayEntry_Object = MibTableRow
sonetPathDayEntry = _SonetPathDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1)
)
sonetPathDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetPathDayNumber"),
)
if mibBuilder.loadTexts:
    sonetPathDayEntry.setStatus("current")


class _SonetPathDayNumber_Type(Integer32):
    """Custom type sonetPathDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_SonetPathDayNumber_Type.__name__ = "Integer32"
_SonetPathDayNumber_Object = MibTableColumn
sonetPathDayNumber = _SonetPathDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 1),
    _SonetPathDayNumber_Type()
)
sonetPathDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayNumber.setStatus("current")
_SonetPathDayStartTime_Type = DateAndTime
_SonetPathDayStartTime_Object = MibTableColumn
sonetPathDayStartTime = _SonetPathDayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 2),
    _SonetPathDayStartTime_Type()
)
sonetPathDayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayStartTime.setStatus("current")
_SonetPathDayValidData_Type = TruthValue
_SonetPathDayValidData_Object = MibTableColumn
sonetPathDayValidData = _SonetPathDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 3),
    _SonetPathDayValidData_Type()
)
sonetPathDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayValidData.setStatus("current")
_SonetPathDayCVs_Type = PerfTotalCount
_SonetPathDayCVs_Object = MibTableColumn
sonetPathDayCVs = _SonetPathDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 5),
    _SonetPathDayCVs_Type()
)
sonetPathDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayCVs.setStatus("current")
_SonetPathDayESs_Type = PerfTotalCount
_SonetPathDayESs_Object = MibTableColumn
sonetPathDayESs = _SonetPathDayESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 6),
    _SonetPathDayESs_Type()
)
sonetPathDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayESs.setStatus("current")
_SonetPathDaySESs_Type = PerfTotalCount
_SonetPathDaySESs_Object = MibTableColumn
sonetPathDaySESs = _SonetPathDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 9),
    _SonetPathDaySESs_Type()
)
sonetPathDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDaySESs.setStatus("current")
_SonetPathDayUASs_Type = PerfTotalCount
_SonetPathDayUASs_Object = MibTableColumn
sonetPathDayUASs = _SonetPathDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 10),
    _SonetPathDayUASs_Type()
)
sonetPathDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayUASs.setStatus("current")
_SonetPathDayFCs_Type = PerfTotalCount
_SonetPathDayFCs_Object = MibTableColumn
sonetPathDayFCs = _SonetPathDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 11),
    _SonetPathDayFCs_Type()
)
sonetPathDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayFCs.setStatus("current")
_SonetPathDayTcaFlag_Type = TruthValue
_SonetPathDayTcaFlag_Object = MibTableColumn
sonetPathDayTcaFlag = _SonetPathDayTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 12),
    _SonetPathDayTcaFlag_Type()
)
sonetPathDayTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayTcaFlag.setStatus("current")
_SonetPathDayEBs_Type = PerfTotalCount
_SonetPathDayEBs_Object = MibTableColumn
sonetPathDayEBs = _SonetPathDayEBs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 13),
    _SonetPathDayEBs_Type()
)
sonetPathDayEBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathDayEBs.setStatus("current")
_SonetPathDayReset_Type = Integer32
_SonetPathDayReset_Object = MibTableColumn
sonetPathDayReset = _SonetPathDayReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 1, 17, 1, 14),
    _SonetPathDayReset_Type()
)
sonetPathDayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDayReset.setStatus("current")
_SonetSupFarEndPath_ObjectIdentity = ObjectIdentity
sonetSupFarEndPath = _SonetSupFarEndPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2)
)
_SonetFarEndPathDayTable_Object = MibTable
sonetFarEndPathDayTable = _SonetFarEndPathDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    sonetFarEndPathDayTable.setStatus("current")
_SonetFarEndPathDayEntry_Object = MibTableRow
sonetFarEndPathDayEntry = _SonetFarEndPathDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1)
)
sonetFarEndPathDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetFarEndPathDayNumber"),
)
if mibBuilder.loadTexts:
    sonetFarEndPathDayEntry.setStatus("current")


class _SonetFarEndPathDayNumber_Type(Integer32):
    """Custom type sonetFarEndPathDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SonetFarEndPathDayNumber_Type.__name__ = "Integer32"
_SonetFarEndPathDayNumber_Object = MibTableColumn
sonetFarEndPathDayNumber = _SonetFarEndPathDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 1),
    _SonetFarEndPathDayNumber_Type()
)
sonetFarEndPathDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayNumber.setStatus("current")
_SonetFarEndPathDayStartTime_Type = DateAndTime
_SonetFarEndPathDayStartTime_Object = MibTableColumn
sonetFarEndPathDayStartTime = _SonetFarEndPathDayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 2),
    _SonetFarEndPathDayStartTime_Type()
)
sonetFarEndPathDayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayStartTime.setStatus("current")
_SonetFarEndPathDayValidData_Type = TruthValue
_SonetFarEndPathDayValidData_Object = MibTableColumn
sonetFarEndPathDayValidData = _SonetFarEndPathDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 3),
    _SonetFarEndPathDayValidData_Type()
)
sonetFarEndPathDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayValidData.setStatus("current")
_SonetFarEndPathDayCVs_Type = PerfTotalCount
_SonetFarEndPathDayCVs_Object = MibTableColumn
sonetFarEndPathDayCVs = _SonetFarEndPathDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 5),
    _SonetFarEndPathDayCVs_Type()
)
sonetFarEndPathDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayCVs.setStatus("current")
_SonetFarEndPathDayESs_Type = PerfTotalCount
_SonetFarEndPathDayESs_Object = MibTableColumn
sonetFarEndPathDayESs = _SonetFarEndPathDayESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 6),
    _SonetFarEndPathDayESs_Type()
)
sonetFarEndPathDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayESs.setStatus("current")
_SonetFarEndPathDaySESs_Type = PerfTotalCount
_SonetFarEndPathDaySESs_Object = MibTableColumn
sonetFarEndPathDaySESs = _SonetFarEndPathDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 9),
    _SonetFarEndPathDaySESs_Type()
)
sonetFarEndPathDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDaySESs.setStatus("current")
_SonetFarEndPathDayUASs_Type = PerfTotalCount
_SonetFarEndPathDayUASs_Object = MibTableColumn
sonetFarEndPathDayUASs = _SonetFarEndPathDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 10),
    _SonetFarEndPathDayUASs_Type()
)
sonetFarEndPathDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayUASs.setStatus("current")
_SonetFarEndPathDayFCs_Type = PerfTotalCount
_SonetFarEndPathDayFCs_Object = MibTableColumn
sonetFarEndPathDayFCs = _SonetFarEndPathDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 11),
    _SonetFarEndPathDayFCs_Type()
)
sonetFarEndPathDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayFCs.setStatus("current")
_SonetFarEndPathDayTcaFlag_Type = TruthValue
_SonetFarEndPathDayTcaFlag_Object = MibTableColumn
sonetFarEndPathDayTcaFlag = _SonetFarEndPathDayTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 12),
    _SonetFarEndPathDayTcaFlag_Type()
)
sonetFarEndPathDayTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayTcaFlag.setStatus("current")
_SonetFarEndPathDayEBs_Type = PerfTotalCount
_SonetFarEndPathDayEBs_Object = MibTableColumn
sonetFarEndPathDayEBs = _SonetFarEndPathDayEBs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 13),
    _SonetFarEndPathDayEBs_Type()
)
sonetFarEndPathDayEBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathDayEBs.setStatus("current")
_SonetFarEndPathDayReset_Type = Integer32
_SonetFarEndPathDayReset_Object = MibTableColumn
sonetFarEndPathDayReset = _SonetFarEndPathDayReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 2, 2, 3, 1, 14),
    _SonetFarEndPathDayReset_Type()
)
sonetFarEndPathDayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFarEndPathDayReset.setStatus("current")
_SonetSupObjectsVT_ObjectIdentity = ObjectIdentity
sonetSupObjectsVT = _SonetSupObjectsVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3)
)
_SonetSupVT_ObjectIdentity = ObjectIdentity
sonetSupVT = _SonetSupVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1)
)
_SonetVTDefaultThresholdTable_Object = MibTable
sonetVTDefaultThresholdTable = _SonetVTDefaultThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sonetVTDefaultThresholdTable.setStatus("current")
_SonetVTDefaultThresholdEntry_Object = MibTableRow
sonetVTDefaultThresholdEntry = _SonetVTDefaultThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1)
)
sonetVTDefaultThresholdEntry.setIndexNames(
    (0, "SL-SONET-SUP-PM-MIB", "sonetVTDefaultThresholdDirection"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetVTDefaultThresholdRate"),
)
if mibBuilder.loadTexts:
    sonetVTDefaultThresholdEntry.setStatus("current")


class _SonetVTDefaultThresholdDirection_Type(Integer32):
    """Custom type sonetVTDefaultThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nearEnd", 1),
          ("farEnd", 2))
    )


_SonetVTDefaultThresholdDirection_Type.__name__ = "Integer32"
_SonetVTDefaultThresholdDirection_Object = MibTableColumn
sonetVTDefaultThresholdDirection = _SonetVTDefaultThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 1),
    _SonetVTDefaultThresholdDirection_Type()
)
sonetVTDefaultThresholdDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetVTDefaultThresholdDirection.setStatus("current")


class _SonetVTDefaultThresholdRate_Type(Integer32):
    """Custom type sonetVTDefaultThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vt1dot5", 1),
          ("vtg", 2))
    )


_SonetVTDefaultThresholdRate_Type.__name__ = "Integer32"
_SonetVTDefaultThresholdRate_Object = MibTableColumn
sonetVTDefaultThresholdRate = _SonetVTDefaultThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 2),
    _SonetVTDefaultThresholdRate_Type()
)
sonetVTDefaultThresholdRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetVTDefaultThresholdRate.setStatus("current")


class _SonetVTDefaultCVThreshold_Type(Integer32):
    """Custom type sonetVTDefaultCVThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonetVTDefaultCVThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultCVThreshold_Object = MibTableColumn
sonetVTDefaultCVThreshold = _SonetVTDefaultCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 3),
    _SonetVTDefaultCVThreshold_Type()
)
sonetVTDefaultCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultCVThreshold.setStatus("current")


class _SonetVTDefaultESThreshold_Type(Integer32):
    """Custom type sonetVTDefaultESThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetVTDefaultESThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultESThreshold_Object = MibTableColumn
sonetVTDefaultESThreshold = _SonetVTDefaultESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 4),
    _SonetVTDefaultESThreshold_Type()
)
sonetVTDefaultESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultESThreshold.setStatus("current")


class _SonetVTDefaultSESThreshold_Type(Integer32):
    """Custom type sonetVTDefaultSESThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetVTDefaultSESThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultSESThreshold_Object = MibTableColumn
sonetVTDefaultSESThreshold = _SonetVTDefaultSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 5),
    _SonetVTDefaultSESThreshold_Type()
)
sonetVTDefaultSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultSESThreshold.setStatus("current")


class _SonetVTDefaultUASThreshold_Type(Integer32):
    """Custom type sonetVTDefaultUASThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonetVTDefaultUASThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultUASThreshold_Object = MibTableColumn
sonetVTDefaultUASThreshold = _SonetVTDefaultUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 6),
    _SonetVTDefaultUASThreshold_Type()
)
sonetVTDefaultUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultUASThreshold.setStatus("current")


class _SonetVTDefaultDayCVThreshold_Type(Integer32):
    """Custom type sonetVTDefaultDayCVThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonetVTDefaultDayCVThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultDayCVThreshold_Object = MibTableColumn
sonetVTDefaultDayCVThreshold = _SonetVTDefaultDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 7),
    _SonetVTDefaultDayCVThreshold_Type()
)
sonetVTDefaultDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultDayCVThreshold.setStatus("current")


class _SonetVTDefaultDayESThreshold_Type(Integer32):
    """Custom type sonetVTDefaultDayESThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonetVTDefaultDayESThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultDayESThreshold_Object = MibTableColumn
sonetVTDefaultDayESThreshold = _SonetVTDefaultDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 8),
    _SonetVTDefaultDayESThreshold_Type()
)
sonetVTDefaultDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultDayESThreshold.setStatus("current")


class _SonetVTDefaultDaySESThreshold_Type(Integer32):
    """Custom type sonetVTDefaultDaySESThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SonetVTDefaultDaySESThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultDaySESThreshold_Object = MibTableColumn
sonetVTDefaultDaySESThreshold = _SonetVTDefaultDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 9),
    _SonetVTDefaultDaySESThreshold_Type()
)
sonetVTDefaultDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultDaySESThreshold.setStatus("current")


class _SonetVTDefaultDayUASThreshold_Type(Integer32):
    """Custom type sonetVTDefaultDayUASThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SonetVTDefaultDayUASThreshold_Type.__name__ = "Integer32"
_SonetVTDefaultDayUASThreshold_Object = MibTableColumn
sonetVTDefaultDayUASThreshold = _SonetVTDefaultDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 1, 1, 10),
    _SonetVTDefaultDayUASThreshold_Type()
)
sonetVTDefaultDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDefaultDayUASThreshold.setStatus("current")
_SonetVTThresholdTable_Object = MibTable
sonetVTThresholdTable = _SonetVTThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sonetVTThresholdTable.setStatus("current")
_SonetVTThresholdEntry_Object = MibTableRow
sonetVTThresholdEntry = _SonetVTThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sonetVTThresholdEntry.setStatus("current")


class _SonetVTCurrentCVThreshold_Type(Integer32):
    """Custom type sonetVTCurrentCVThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonetVTCurrentCVThreshold_Type.__name__ = "Integer32"
_SonetVTCurrentCVThreshold_Object = MibTableColumn
sonetVTCurrentCVThreshold = _SonetVTCurrentCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 1),
    _SonetVTCurrentCVThreshold_Type()
)
sonetVTCurrentCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTCurrentCVThreshold.setStatus("current")


class _SonetVTCurrentESThreshold_Type(Integer32):
    """Custom type sonetVTCurrentESThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonetVTCurrentESThreshold_Type.__name__ = "Integer32"
_SonetVTCurrentESThreshold_Object = MibTableColumn
sonetVTCurrentESThreshold = _SonetVTCurrentESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 2),
    _SonetVTCurrentESThreshold_Type()
)
sonetVTCurrentESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTCurrentESThreshold.setStatus("current")


class _SonetVTCurrentSESThreshold_Type(Integer32):
    """Custom type sonetVTCurrentSESThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonetVTCurrentSESThreshold_Type.__name__ = "Integer32"
_SonetVTCurrentSESThreshold_Object = MibTableColumn
sonetVTCurrentSESThreshold = _SonetVTCurrentSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 3),
    _SonetVTCurrentSESThreshold_Type()
)
sonetVTCurrentSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTCurrentSESThreshold.setStatus("current")


class _SonetVTCurrentUASThreshold_Type(Integer32):
    """Custom type sonetVTCurrentUASThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonetVTCurrentUASThreshold_Type.__name__ = "Integer32"
_SonetVTCurrentUASThreshold_Object = MibTableColumn
sonetVTCurrentUASThreshold = _SonetVTCurrentUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 4),
    _SonetVTCurrentUASThreshold_Type()
)
sonetVTCurrentUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTCurrentUASThreshold.setStatus("current")


class _SonetVTDayCVThreshold_Type(Integer32):
    """Custom type sonetVTDayCVThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonetVTDayCVThreshold_Type.__name__ = "Integer32"
_SonetVTDayCVThreshold_Object = MibTableColumn
sonetVTDayCVThreshold = _SonetVTDayCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 5),
    _SonetVTDayCVThreshold_Type()
)
sonetVTDayCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDayCVThreshold.setStatus("current")


class _SonetVTDayESThreshold_Type(Integer32):
    """Custom type sonetVTDayESThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonetVTDayESThreshold_Type.__name__ = "Integer32"
_SonetVTDayESThreshold_Object = MibTableColumn
sonetVTDayESThreshold = _SonetVTDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 6),
    _SonetVTDayESThreshold_Type()
)
sonetVTDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDayESThreshold.setStatus("current")


class _SonetVTDaySESThreshold_Type(Integer32):
    """Custom type sonetVTDaySESThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonetVTDaySESThreshold_Type.__name__ = "Integer32"
_SonetVTDaySESThreshold_Object = MibTableColumn
sonetVTDaySESThreshold = _SonetVTDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 7),
    _SonetVTDaySESThreshold_Type()
)
sonetVTDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDaySESThreshold.setStatus("current")


class _SonetVTDayUASThreshold_Type(Integer32):
    """Custom type sonetVTDayUASThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonetVTDayUASThreshold_Type.__name__ = "Integer32"
_SonetVTDayUASThreshold_Object = MibTableColumn
sonetVTDayUASThreshold = _SonetVTDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 2, 1, 8),
    _SonetVTDayUASThreshold_Type()
)
sonetVTDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDayUASThreshold.setStatus("current")
_SonetVTDayTable_Object = MibTable
sonetVTDayTable = _SonetVTDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17)
)
if mibBuilder.loadTexts:
    sonetVTDayTable.setStatus("current")
_SonetVTDayEntry_Object = MibTableRow
sonetVTDayEntry = _SonetVTDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1)
)
sonetVTDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetVTDayNumber"),
)
if mibBuilder.loadTexts:
    sonetVTDayEntry.setStatus("current")


class _SonetVTDayNumber_Type(Integer32):
    """Custom type sonetVTDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_SonetVTDayNumber_Type.__name__ = "Integer32"
_SonetVTDayNumber_Object = MibTableColumn
sonetVTDayNumber = _SonetVTDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 1),
    _SonetVTDayNumber_Type()
)
sonetVTDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayNumber.setStatus("current")
_SonetVTDayStartTime_Type = DateAndTime
_SonetVTDayStartTime_Object = MibTableColumn
sonetVTDayStartTime = _SonetVTDayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 2),
    _SonetVTDayStartTime_Type()
)
sonetVTDayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayStartTime.setStatus("current")
_SonetVTDayValidData_Type = TruthValue
_SonetVTDayValidData_Object = MibTableColumn
sonetVTDayValidData = _SonetVTDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 3),
    _SonetVTDayValidData_Type()
)
sonetVTDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayValidData.setStatus("current")
_SonetVTDayFCs_Type = PerfTotalCount
_SonetVTDayFCs_Object = MibTableColumn
sonetVTDayFCs = _SonetVTDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 4),
    _SonetVTDayFCs_Type()
)
sonetVTDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayFCs.setStatus("current")
_SonetVTDayCVs_Type = PerfTotalCount
_SonetVTDayCVs_Object = MibTableColumn
sonetVTDayCVs = _SonetVTDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 5),
    _SonetVTDayCVs_Type()
)
sonetVTDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayCVs.setStatus("current")
_SonetVTDayESs_Type = PerfTotalCount
_SonetVTDayESs_Object = MibTableColumn
sonetVTDayESs = _SonetVTDayESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 6),
    _SonetVTDayESs_Type()
)
sonetVTDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayESs.setStatus("current")
_SonetVTDaySESs_Type = PerfTotalCount
_SonetVTDaySESs_Object = MibTableColumn
sonetVTDaySESs = _SonetVTDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 7),
    _SonetVTDaySESs_Type()
)
sonetVTDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDaySESs.setStatus("current")
_SonetVTDayUASs_Type = PerfTotalCount
_SonetVTDayUASs_Object = MibTableColumn
sonetVTDayUASs = _SonetVTDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 8),
    _SonetVTDayUASs_Type()
)
sonetVTDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayUASs.setStatus("current")
_SonetVTDayEBs_Type = PerfTotalCount
_SonetVTDayEBs_Object = MibTableColumn
sonetVTDayEBs = _SonetVTDayEBs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 9),
    _SonetVTDayEBs_Type()
)
sonetVTDayEBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayEBs.setStatus("current")
_SonetVTDayTcaFlag_Type = TruthValue
_SonetVTDayTcaFlag_Object = MibTableColumn
sonetVTDayTcaFlag = _SonetVTDayTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 10),
    _SonetVTDayTcaFlag_Type()
)
sonetVTDayTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetVTDayTcaFlag.setStatus("current")
_SonetVTDayReset_Type = Integer32
_SonetVTDayReset_Object = MibTableColumn
sonetVTDayReset = _SonetVTDayReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 1, 17, 1, 11),
    _SonetVTDayReset_Type()
)
sonetVTDayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetVTDayReset.setStatus("current")
_SonetSupFarEndVT_ObjectIdentity = ObjectIdentity
sonetSupFarEndVT = _SonetSupFarEndVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2)
)
_SonetFarEndVTDayTable_Object = MibTable
sonetFarEndVTDayTable = _SonetFarEndVTDayTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    sonetFarEndVTDayTable.setStatus("current")
_SonetFarEndVTDayEntry_Object = MibTableRow
sonetFarEndVTDayEntry = _SonetFarEndVTDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1)
)
sonetFarEndVTDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-SONET-SUP-PM-MIB", "sonetFarEndVTDayNumber"),
)
if mibBuilder.loadTexts:
    sonetFarEndVTDayEntry.setStatus("current")


class _SonetFarEndVTDayNumber_Type(Integer32):
    """Custom type sonetFarEndVTDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SonetFarEndVTDayNumber_Type.__name__ = "Integer32"
_SonetFarEndVTDayNumber_Object = MibTableColumn
sonetFarEndVTDayNumber = _SonetFarEndVTDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 1),
    _SonetFarEndVTDayNumber_Type()
)
sonetFarEndVTDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayNumber.setStatus("current")
_SonetFarEndVTDayStartTime_Type = DateAndTime
_SonetFarEndVTDayStartTime_Object = MibTableColumn
sonetFarEndVTDayStartTime = _SonetFarEndVTDayStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 2),
    _SonetFarEndVTDayStartTime_Type()
)
sonetFarEndVTDayStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayStartTime.setStatus("current")
_SonetFarEndVTDayValidData_Type = TruthValue
_SonetFarEndVTDayValidData_Object = MibTableColumn
sonetFarEndVTDayValidData = _SonetFarEndVTDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 3),
    _SonetFarEndVTDayValidData_Type()
)
sonetFarEndVTDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayValidData.setStatus("current")
_SonetFarEndVTDayFCs_Type = PerfTotalCount
_SonetFarEndVTDayFCs_Object = MibTableColumn
sonetFarEndVTDayFCs = _SonetFarEndVTDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 4),
    _SonetFarEndVTDayFCs_Type()
)
sonetFarEndVTDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayFCs.setStatus("current")
_SonetFarEndVTDayCVs_Type = PerfTotalCount
_SonetFarEndVTDayCVs_Object = MibTableColumn
sonetFarEndVTDayCVs = _SonetFarEndVTDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 5),
    _SonetFarEndVTDayCVs_Type()
)
sonetFarEndVTDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayCVs.setStatus("current")
_SonetFarEndVTDayESs_Type = PerfTotalCount
_SonetFarEndVTDayESs_Object = MibTableColumn
sonetFarEndVTDayESs = _SonetFarEndVTDayESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 6),
    _SonetFarEndVTDayESs_Type()
)
sonetFarEndVTDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayESs.setStatus("current")
_SonetFarEndVTDaySESs_Type = PerfTotalCount
_SonetFarEndVTDaySESs_Object = MibTableColumn
sonetFarEndVTDaySESs = _SonetFarEndVTDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 7),
    _SonetFarEndVTDaySESs_Type()
)
sonetFarEndVTDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDaySESs.setStatus("current")
_SonetFarEndVTDayUASs_Type = PerfTotalCount
_SonetFarEndVTDayUASs_Object = MibTableColumn
sonetFarEndVTDayUASs = _SonetFarEndVTDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 8),
    _SonetFarEndVTDayUASs_Type()
)
sonetFarEndVTDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayUASs.setStatus("current")
_SonetFarEndVTDayEBs_Type = PerfTotalCount
_SonetFarEndVTDayEBs_Object = MibTableColumn
sonetFarEndVTDayEBs = _SonetFarEndVTDayEBs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 9),
    _SonetFarEndVTDayEBs_Type()
)
sonetFarEndVTDayEBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayEBs.setStatus("current")
_SonetFarEndVTDayTcaFlag_Type = TruthValue
_SonetFarEndVTDayTcaFlag_Object = MibTableColumn
sonetFarEndVTDayTcaFlag = _SonetFarEndVTDayTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 10),
    _SonetFarEndVTDayTcaFlag_Type()
)
sonetFarEndVTDayTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndVTDayTcaFlag.setStatus("current")
_SonetFarEndVTDayReset_Type = Integer32
_SonetFarEndVTDayReset_Object = MibTableColumn
sonetFarEndVTDayReset = _SonetFarEndVTDayReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 3, 2, 3, 1, 11),
    _SonetFarEndVTDayReset_Type()
)
sonetFarEndVTDayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFarEndVTDayReset.setStatus("current")
sonetSectionCurrentEntry.registerAugmentions(
    ("SL-SONET-SUP-PM-MIB",
     "sonetSectionThresholdEntry")
)
sonetSectionThresholdEntry.setIndexNames(*sonetSectionCurrentEntry.getIndexNames())
sonetVTCurrentEntry.registerAugmentions(
    ("SL-SONET-SUP-PM-MIB",
     "sonetVTThresholdEntry")
)
sonetVTThresholdEntry.setIndexNames(*sonetVTCurrentEntry.getIndexNames())

# Managed Objects groups


# Notification objects

sonetThresholdCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 3, 1, 6, 3)
)
sonetThresholdCrossing.setObjects(
      *(("SL-SONET-SUP-PM-MIB", "sonetCounterId"),
        ("SL-SONET-SUP-PM-MIB", "sonetCounterValue"))
)
if mibBuilder.loadTexts:
    sonetThresholdCrossing.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-SONET-SUP-PM-MIB",
    **{"sonetSupPmMIB": sonetSupPmMIB,
       "sonetSupObjects": sonetSupObjects,
       "sonetSupConfig": sonetSupConfig,
       "sonetSupMedium": sonetSupMedium,
       "sonetSupSection": sonetSupSection,
       "sonetSectionDefaultThresholdTable": sonetSectionDefaultThresholdTable,
       "sonetSectionDefaultThresholdEntry": sonetSectionDefaultThresholdEntry,
       "sonetSectionDefaultThresholdRate": sonetSectionDefaultThresholdRate,
       "sonetSectionDefaultCVThreshold": sonetSectionDefaultCVThreshold,
       "sonetSectionDefaultESThreshold": sonetSectionDefaultESThreshold,
       "sonetSectionDefaultSESThreshold": sonetSectionDefaultSESThreshold,
       "sonetSectionDefaultSEFSThreshold": sonetSectionDefaultSEFSThreshold,
       "sonetSectionDefaultDayCVThreshold": sonetSectionDefaultDayCVThreshold,
       "sonetSectionDefaultDayESThreshold": sonetSectionDefaultDayESThreshold,
       "sonetSectionDefaultDaySESThreshold": sonetSectionDefaultDaySESThreshold,
       "sonetSectionDefaultDaySEFSThreshold": sonetSectionDefaultDaySEFSThreshold,
       "sonetSectionThresholdTable": sonetSectionThresholdTable,
       "sonetSectionThresholdEntry": sonetSectionThresholdEntry,
       "sonetSectionCurrentCVThreshold": sonetSectionCurrentCVThreshold,
       "sonetSectionCurrentESThreshold": sonetSectionCurrentESThreshold,
       "sonetSectionCurrentSESThreshold": sonetSectionCurrentSESThreshold,
       "sonetSectionCurrentSEFSThreshold": sonetSectionCurrentSEFSThreshold,
       "sonetSectionDayCVThreshold": sonetSectionDayCVThreshold,
       "sonetSectionDayESThreshold": sonetSectionDayESThreshold,
       "sonetSectionDaySESThreshold": sonetSectionDaySESThreshold,
       "sonetSectionDaySEFSThreshold": sonetSectionDaySEFSThreshold,
       "sonetSectionDayTable": sonetSectionDayTable,
       "sonetSectionDayEntry": sonetSectionDayEntry,
       "sonetSectionDayNumber": sonetSectionDayNumber,
       "sonetSectionDayStartTime": sonetSectionDayStartTime,
       "sonetSectionDayValidData": sonetSectionDayValidData,
       "sonetSectionDayCVs": sonetSectionDayCVs,
       "sonetSectionDayESs": sonetSectionDayESs,
       "sonetSectionDaySESs": sonetSectionDaySESs,
       "sonetSectionDaySEFSs": sonetSectionDaySEFSs,
       "sonetSectionDayTcaFlag": sonetSectionDayTcaFlag,
       "sonetSectionDayReset": sonetSectionDayReset,
       "sonetSupLine": sonetSupLine,
       "sonetLineDefaultThresholdTable": sonetLineDefaultThresholdTable,
       "sonetLineDefaultThresholdEntry": sonetLineDefaultThresholdEntry,
       "sonetLineDefaultThresholdDirection": sonetLineDefaultThresholdDirection,
       "sonetLineDefaultThresholdRate": sonetLineDefaultThresholdRate,
       "sonetLineDefaultCVThreshold": sonetLineDefaultCVThreshold,
       "sonetLineDefaultESThreshold": sonetLineDefaultESThreshold,
       "sonetLineDefaultSESThreshold": sonetLineDefaultSESThreshold,
       "sonetLineDefaultUASThreshold": sonetLineDefaultUASThreshold,
       "sonetLineDefaultDayCVThreshold": sonetLineDefaultDayCVThreshold,
       "sonetLineDefaultDayESThreshold": sonetLineDefaultDayESThreshold,
       "sonetLineDefaultDaySESThreshold": sonetLineDefaultDaySESThreshold,
       "sonetLineDefaultDayUASThreshold": sonetLineDefaultDayUASThreshold,
       "sonetLineThresholdTable": sonetLineThresholdTable,
       "sonetLineThresholdEntry": sonetLineThresholdEntry,
       "sonetLineThresholdDirection": sonetLineThresholdDirection,
       "sonetLineCurrentCVThreshold": sonetLineCurrentCVThreshold,
       "sonetLineCurrentESThreshold": sonetLineCurrentESThreshold,
       "sonetLineCurrentSESThreshold": sonetLineCurrentSESThreshold,
       "sonetLineCurrentUASThreshold": sonetLineCurrentUASThreshold,
       "sonetLineDayCVThreshold": sonetLineDayCVThreshold,
       "sonetLineDayESThreshold": sonetLineDayESThreshold,
       "sonetLineDaySESThreshold": sonetLineDaySESThreshold,
       "sonetLineDayUASThreshold": sonetLineDayUASThreshold,
       "sonetLineDayTable": sonetLineDayTable,
       "sonetLineDayEntry": sonetLineDayEntry,
       "sonetLineDayNumber": sonetLineDayNumber,
       "sonetLineDayStartTime": sonetLineDayStartTime,
       "sonetLineDayValidData": sonetLineDayValidData,
       "sonetLineDayCVs": sonetLineDayCVs,
       "sonetLineDayESs": sonetLineDayESs,
       "sonetLineDaySESs": sonetLineDaySESs,
       "sonetLineDayUASs": sonetLineDayUASs,
       "sonetLineDayPSC": sonetLineDayPSC,
       "sonetLineDayPSD": sonetLineDayPSD,
       "sonetLineDayFCs": sonetLineDayFCs,
       "sonetLineDayTcaFlag": sonetLineDayTcaFlag,
       "sonetLineDayReset": sonetLineDayReset,
       "sonetSupFarEndLine": sonetSupFarEndLine,
       "sonetFarEndLineDayTable": sonetFarEndLineDayTable,
       "sonetFarEndLineDayEntry": sonetFarEndLineDayEntry,
       "sonetFarEndLineDayNumber": sonetFarEndLineDayNumber,
       "sonetFarEndLineDayStartTime": sonetFarEndLineDayStartTime,
       "sonetFarEndLineDayValidData": sonetFarEndLineDayValidData,
       "sonetFarEndLineDayCVs": sonetFarEndLineDayCVs,
       "sonetFarEndLineDayESs": sonetFarEndLineDayESs,
       "sonetFarEndLineDaySESs": sonetFarEndLineDaySESs,
       "sonetFarEndLineDayUASs": sonetFarEndLineDayUASs,
       "sonetFarEndLineDayFCs": sonetFarEndLineDayFCs,
       "sonetFarEndLineDayTcaFlag": sonetFarEndLineDayTcaFlag,
       "sonetFarEndLineDayReset": sonetFarEndLineDayReset,
       "sonetTrap": sonetTrap,
       "sonetCounterId": sonetCounterId,
       "sonetCounterValue": sonetCounterValue,
       "sonetThresholdCrossing": sonetThresholdCrossing,
       "sonetSupObjectsPath": sonetSupObjectsPath,
       "sonetSupPath": sonetSupPath,
       "sonetPathDefaultThresholdTable": sonetPathDefaultThresholdTable,
       "sonetPathDefaultThresholdEntry": sonetPathDefaultThresholdEntry,
       "sonetPathDefaultThresholdDirection": sonetPathDefaultThresholdDirection,
       "sonetPathDefaultThresholdRate": sonetPathDefaultThresholdRate,
       "sonetPathDefaultCVThreshold": sonetPathDefaultCVThreshold,
       "sonetPathDefaultESThreshold": sonetPathDefaultESThreshold,
       "sonetPathDefaultSESThreshold": sonetPathDefaultSESThreshold,
       "sonetPathDefaultUASThreshold": sonetPathDefaultUASThreshold,
       "sonetPathDefaultDayCVThreshold": sonetPathDefaultDayCVThreshold,
       "sonetPathDefaultDayESThreshold": sonetPathDefaultDayESThreshold,
       "sonetPathDefaultDaySESThreshold": sonetPathDefaultDaySESThreshold,
       "sonetPathDefaultDayUASThreshold": sonetPathDefaultDayUASThreshold,
       "sonetPathThresholdTable": sonetPathThresholdTable,
       "sonetPathThresholdEntry": sonetPathThresholdEntry,
       "sonetPathThresholdDirection": sonetPathThresholdDirection,
       "sonetPathCurrentCVThreshold": sonetPathCurrentCVThreshold,
       "sonetPathCurrentESThreshold": sonetPathCurrentESThreshold,
       "sonetPathCurrentSESThreshold": sonetPathCurrentSESThreshold,
       "sonetPathCurrentUASThreshold": sonetPathCurrentUASThreshold,
       "sonetPathDayCVThreshold": sonetPathDayCVThreshold,
       "sonetPathDayESThreshold": sonetPathDayESThreshold,
       "sonetPathDaySESThreshold": sonetPathDaySESThreshold,
       "sonetPathDayUASThreshold": sonetPathDayUASThreshold,
       "sonetPathDayTable": sonetPathDayTable,
       "sonetPathDayEntry": sonetPathDayEntry,
       "sonetPathDayNumber": sonetPathDayNumber,
       "sonetPathDayStartTime": sonetPathDayStartTime,
       "sonetPathDayValidData": sonetPathDayValidData,
       "sonetPathDayCVs": sonetPathDayCVs,
       "sonetPathDayESs": sonetPathDayESs,
       "sonetPathDaySESs": sonetPathDaySESs,
       "sonetPathDayUASs": sonetPathDayUASs,
       "sonetPathDayFCs": sonetPathDayFCs,
       "sonetPathDayTcaFlag": sonetPathDayTcaFlag,
       "sonetPathDayEBs": sonetPathDayEBs,
       "sonetPathDayReset": sonetPathDayReset,
       "sonetSupFarEndPath": sonetSupFarEndPath,
       "sonetFarEndPathDayTable": sonetFarEndPathDayTable,
       "sonetFarEndPathDayEntry": sonetFarEndPathDayEntry,
       "sonetFarEndPathDayNumber": sonetFarEndPathDayNumber,
       "sonetFarEndPathDayStartTime": sonetFarEndPathDayStartTime,
       "sonetFarEndPathDayValidData": sonetFarEndPathDayValidData,
       "sonetFarEndPathDayCVs": sonetFarEndPathDayCVs,
       "sonetFarEndPathDayESs": sonetFarEndPathDayESs,
       "sonetFarEndPathDaySESs": sonetFarEndPathDaySESs,
       "sonetFarEndPathDayUASs": sonetFarEndPathDayUASs,
       "sonetFarEndPathDayFCs": sonetFarEndPathDayFCs,
       "sonetFarEndPathDayTcaFlag": sonetFarEndPathDayTcaFlag,
       "sonetFarEndPathDayEBs": sonetFarEndPathDayEBs,
       "sonetFarEndPathDayReset": sonetFarEndPathDayReset,
       "sonetSupObjectsVT": sonetSupObjectsVT,
       "sonetSupVT": sonetSupVT,
       "sonetVTDefaultThresholdTable": sonetVTDefaultThresholdTable,
       "sonetVTDefaultThresholdEntry": sonetVTDefaultThresholdEntry,
       "sonetVTDefaultThresholdDirection": sonetVTDefaultThresholdDirection,
       "sonetVTDefaultThresholdRate": sonetVTDefaultThresholdRate,
       "sonetVTDefaultCVThreshold": sonetVTDefaultCVThreshold,
       "sonetVTDefaultESThreshold": sonetVTDefaultESThreshold,
       "sonetVTDefaultSESThreshold": sonetVTDefaultSESThreshold,
       "sonetVTDefaultUASThreshold": sonetVTDefaultUASThreshold,
       "sonetVTDefaultDayCVThreshold": sonetVTDefaultDayCVThreshold,
       "sonetVTDefaultDayESThreshold": sonetVTDefaultDayESThreshold,
       "sonetVTDefaultDaySESThreshold": sonetVTDefaultDaySESThreshold,
       "sonetVTDefaultDayUASThreshold": sonetVTDefaultDayUASThreshold,
       "sonetVTThresholdTable": sonetVTThresholdTable,
       "sonetVTThresholdEntry": sonetVTThresholdEntry,
       "sonetVTCurrentCVThreshold": sonetVTCurrentCVThreshold,
       "sonetVTCurrentESThreshold": sonetVTCurrentESThreshold,
       "sonetVTCurrentSESThreshold": sonetVTCurrentSESThreshold,
       "sonetVTCurrentUASThreshold": sonetVTCurrentUASThreshold,
       "sonetVTDayCVThreshold": sonetVTDayCVThreshold,
       "sonetVTDayESThreshold": sonetVTDayESThreshold,
       "sonetVTDaySESThreshold": sonetVTDaySESThreshold,
       "sonetVTDayUASThreshold": sonetVTDayUASThreshold,
       "sonetVTDayTable": sonetVTDayTable,
       "sonetVTDayEntry": sonetVTDayEntry,
       "sonetVTDayNumber": sonetVTDayNumber,
       "sonetVTDayStartTime": sonetVTDayStartTime,
       "sonetVTDayValidData": sonetVTDayValidData,
       "sonetVTDayFCs": sonetVTDayFCs,
       "sonetVTDayCVs": sonetVTDayCVs,
       "sonetVTDayESs": sonetVTDayESs,
       "sonetVTDaySESs": sonetVTDaySESs,
       "sonetVTDayUASs": sonetVTDayUASs,
       "sonetVTDayEBs": sonetVTDayEBs,
       "sonetVTDayTcaFlag": sonetVTDayTcaFlag,
       "sonetVTDayReset": sonetVTDayReset,
       "sonetSupFarEndVT": sonetSupFarEndVT,
       "sonetFarEndVTDayTable": sonetFarEndVTDayTable,
       "sonetFarEndVTDayEntry": sonetFarEndVTDayEntry,
       "sonetFarEndVTDayNumber": sonetFarEndVTDayNumber,
       "sonetFarEndVTDayStartTime": sonetFarEndVTDayStartTime,
       "sonetFarEndVTDayValidData": sonetFarEndVTDayValidData,
       "sonetFarEndVTDayFCs": sonetFarEndVTDayFCs,
       "sonetFarEndVTDayCVs": sonetFarEndVTDayCVs,
       "sonetFarEndVTDayESs": sonetFarEndVTDayESs,
       "sonetFarEndVTDaySESs": sonetFarEndVTDaySESs,
       "sonetFarEndVTDayUASs": sonetFarEndVTDayUASs,
       "sonetFarEndVTDayEBs": sonetFarEndVTDayEBs,
       "sonetFarEndVTDayTcaFlag": sonetFarEndVTDayTcaFlag,
       "sonetFarEndVTDayReset": sonetFarEndVTDayReset}
)
