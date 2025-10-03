# SNMP MIB module (TN-PMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TN-PMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:12 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(TSapIngQueueId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "TSapIngQueueId")

(TItemDescription,
 TQueueId,
 TmnxEncapVal,
 TmnxPortID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TQueueId",
    "TmnxEncapVal",
    "TmnxPortID")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")

(TnCommand,) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCommand")


# MODULE-IDENTITY

tnPmonMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 99)
)
if mibBuilder.loadTexts:
    tnPmonMIBModule.setRevisions(
        ("2022-09-09 00:00",
         "2021-06-04 00:00",
         "2020-03-13 00:00",
         "2019-11-22 00:00",
         "2019-04-28 00:00",
         "2019-04-22 00:00",
         "2019-02-07 00:00",
         "2018-11-09 00:00",
         "2018-10-26 00:00",
         "2018-10-12 00:00",
         "2018-02-23 00:00",
         "2015-02-17 00:00",
         "2013-07-29 00:00",
         "2013-05-20 00:00",
         "2013-03-26 00:00",
         "2012-11-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmPmonPolicyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              20)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("sap", 2),
          ("eth-cfm-two-way-slm", 3),
          ("eth-cfm-two-way-dm", 4),
          ("eth-cfm-two-way-lm", 5),
          ("roe", 20))
    )



class AluWdmStatsIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2),
    )



class AluWdmStatsBinNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32),
    )



class AluWdmStatsBinStatus(TextualConvention, Integer32):
    status = "current"
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("rxValid", 2),
          ("txValid", 3),
          ("invalid", 4),
          ("dataNotAvailable", 5),
          ("partial", 6),
          ("adjusted", 7),
          ("dataLong", 8),
          ("dataComplete", 9))
    )



class AluWdmPmonStatsClearType(TextualConvention, Integer32):
    status = "current"
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("sap", 2),
          ("eth-cfm-oam-test", 3),
          ("roe", 4),
          ("roe-mapper", 5),
          ("roe-demapper", 6),
          ("emac", 7),
          ("pmac", 8),
          ("mmac", 9))
    )



# MIB Managed Objects in the order of their OIDs

_TnPmonObjs_ObjectIdentity = ObjectIdentity
tnPmonObjs = _TnPmonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99)
)
_TnPmonPolicyAttributeTotal_Type = Integer32
_TnPmonPolicyAttributeTotal_Object = MibScalar
tnPmonPolicyAttributeTotal = _TnPmonPolicyAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 1),
    _TnPmonPolicyAttributeTotal_Type()
)
tnPmonPolicyAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonPolicyAttributeTotal.setStatus("current")
_TnPmonPolicyTable_Object = MibTable
tnPmonPolicyTable = _TnPmonPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2)
)
if mibBuilder.loadTexts:
    tnPmonPolicyTable.setStatus("current")
_TnPmonPolicyEntry_Object = MibTableRow
tnPmonPolicyEntry = _TnPmonPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1)
)
tnPmonPolicyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnPmonPolicyType"),
    (0, "TN-PMON-MIB", "tnPmonPolicyId"),
)
if mibBuilder.loadTexts:
    tnPmonPolicyEntry.setStatus("current")
_TnPmonPolicyType_Type = AluWdmPmonPolicyType
_TnPmonPolicyType_Object = MibTableColumn
tnPmonPolicyType = _TnPmonPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 1),
    _TnPmonPolicyType_Type()
)
tnPmonPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonPolicyType.setStatus("current")


class _TnPmonPolicyId_Type(Integer32):
    """Custom type tnPmonPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnPmonPolicyId_Type.__name__ = "Integer32"
_TnPmonPolicyId_Object = MibTableColumn
tnPmonPolicyId = _TnPmonPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 2),
    _TnPmonPolicyId_Type()
)
tnPmonPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonPolicyId.setStatus("current")
_TnPmonPolicyRowStatus_Type = RowStatus
_TnPmonPolicyRowStatus_Object = MibTableColumn
tnPmonPolicyRowStatus = _TnPmonPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 3),
    _TnPmonPolicyRowStatus_Type()
)
tnPmonPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyRowStatus.setStatus("current")


class _TnPmonPolicyDescription_Type(TItemDescription):
    """Custom type tnPmonPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TnPmonPolicyDescription_Type.__name__ = "TItemDescription"
_TnPmonPolicyDescription_Object = MibTableColumn
tnPmonPolicyDescription = _TnPmonPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 4),
    _TnPmonPolicyDescription_Type()
)
tnPmonPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyDescription.setStatus("current")


class _TnPmonPolicyNumOfBins15Min_Type(Integer32):
    """Custom type tnPmonPolicyNumOfBins15Min based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_TnPmonPolicyNumOfBins15Min_Type.__name__ = "Integer32"
_TnPmonPolicyNumOfBins15Min_Object = MibTableColumn
tnPmonPolicyNumOfBins15Min = _TnPmonPolicyNumOfBins15Min_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 5),
    _TnPmonPolicyNumOfBins15Min_Type()
)
tnPmonPolicyNumOfBins15Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyNumOfBins15Min.setStatus("current")


class _TnPmonPolicyNumOfBins1Day_Type(Integer32):
    """Custom type tnPmonPolicyNumOfBins1Day based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnPmonPolicyNumOfBins1Day_Type.__name__ = "Integer32"
_TnPmonPolicyNumOfBins1Day_Object = MibTableColumn
tnPmonPolicyNumOfBins1Day = _TnPmonPolicyNumOfBins1Day_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 6),
    _TnPmonPolicyNumOfBins1Day_Type()
)
tnPmonPolicyNumOfBins1Day.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyNumOfBins1Day.setStatus("current")


class _TnPmonPolicyFlrInterval15Min_Type(Integer32):
    """Custom type tnPmonPolicyFlrInterval15Min based on Integer32"""
    defaultValue = 1


_TnPmonPolicyFlrInterval15Min_Type.__name__ = "Integer32"
_TnPmonPolicyFlrInterval15Min_Object = MibTableColumn
tnPmonPolicyFlrInterval15Min = _TnPmonPolicyFlrInterval15Min_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 7),
    _TnPmonPolicyFlrInterval15Min_Type()
)
tnPmonPolicyFlrInterval15Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrInterval15Min.setStatus("current")


class _TnPmonPolicyFlrInterval1Day_Type(Integer32):
    """Custom type tnPmonPolicyFlrInterval1Day based on Integer32"""
    defaultValue = 60


_TnPmonPolicyFlrInterval1Day_Type.__name__ = "Integer32"
_TnPmonPolicyFlrInterval1Day_Object = MibTableColumn
tnPmonPolicyFlrInterval1Day = _TnPmonPolicyFlrInterval1Day_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 8),
    _TnPmonPolicyFlrInterval1Day_Type()
)
tnPmonPolicyFlrInterval1Day.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrInterval1Day.setStatus("current")


class _TnPmonPolicyFlrAvailabilityInterval15Min_Type(Integer32):
    """Custom type tnPmonPolicyFlrAvailabilityInterval15Min based on Integer32"""
    defaultValue = 10


_TnPmonPolicyFlrAvailabilityInterval15Min_Type.__name__ = "Integer32"
_TnPmonPolicyFlrAvailabilityInterval15Min_Object = MibTableColumn
tnPmonPolicyFlrAvailabilityInterval15Min = _TnPmonPolicyFlrAvailabilityInterval15Min_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 9),
    _TnPmonPolicyFlrAvailabilityInterval15Min_Type()
)
tnPmonPolicyFlrAvailabilityInterval15Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrAvailabilityInterval15Min.setStatus("current")


class _TnPmonPolicyFlrAvailabilityInterval1Day_Type(Integer32):
    """Custom type tnPmonPolicyFlrAvailabilityInterval1Day based on Integer32"""
    defaultValue = 10


_TnPmonPolicyFlrAvailabilityInterval1Day_Type.__name__ = "Integer32"
_TnPmonPolicyFlrAvailabilityInterval1Day_Object = MibTableColumn
tnPmonPolicyFlrAvailabilityInterval1Day = _TnPmonPolicyFlrAvailabilityInterval1Day_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 10),
    _TnPmonPolicyFlrAvailabilityInterval1Day_Type()
)
tnPmonPolicyFlrAvailabilityInterval1Day.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrAvailabilityInterval1Day.setStatus("current")


class _TnPmonPolicyNumOfBinsContinuous_Type(Integer32):
    """Custom type tnPmonPolicyNumOfBinsContinuous based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnPmonPolicyNumOfBinsContinuous_Type.__name__ = "Integer32"
_TnPmonPolicyNumOfBinsContinuous_Object = MibTableColumn
tnPmonPolicyNumOfBinsContinuous = _TnPmonPolicyNumOfBinsContinuous_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 11),
    _TnPmonPolicyNumOfBinsContinuous_Type()
)
tnPmonPolicyNumOfBinsContinuous.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyNumOfBinsContinuous.setStatus("current")


class _TnPmonPolicyAvailFlrThreshold_Type(Integer32):
    """Custom type tnPmonPolicyAvailFlrThreshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnPmonPolicyAvailFlrThreshold_Type.__name__ = "Integer32"
_TnPmonPolicyAvailFlrThreshold_Object = MibTableColumn
tnPmonPolicyAvailFlrThreshold = _TnPmonPolicyAvailFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 12),
    _TnPmonPolicyAvailFlrThreshold_Type()
)
tnPmonPolicyAvailFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyAvailFlrThreshold.setStatus("current")


class _TnPmonPolicyAvailFlrNumOfIntervals_Type(Integer32):
    """Custom type tnPmonPolicyAvailFlrNumOfIntervals based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnPmonPolicyAvailFlrNumOfIntervals_Type.__name__ = "Integer32"
_TnPmonPolicyAvailFlrNumOfIntervals_Object = MibTableColumn
tnPmonPolicyAvailFlrNumOfIntervals = _TnPmonPolicyAvailFlrNumOfIntervals_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 13),
    _TnPmonPolicyAvailFlrNumOfIntervals_Type()
)
tnPmonPolicyAvailFlrNumOfIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyAvailFlrNumOfIntervals.setStatus("current")


class _TnPmonPolicyFramesPerDeltaT_Type(Integer32):
    """Custom type tnPmonPolicyFramesPerDeltaT based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TnPmonPolicyFramesPerDeltaT_Type.__name__ = "Integer32"
_TnPmonPolicyFramesPerDeltaT_Object = MibTableColumn
tnPmonPolicyFramesPerDeltaT = _TnPmonPolicyFramesPerDeltaT_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 14),
    _TnPmonPolicyFramesPerDeltaT_Type()
)
tnPmonPolicyFramesPerDeltaT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFramesPerDeltaT.setStatus("current")
_TnPmonClearAttributeTotal_Type = Integer32
_TnPmonClearAttributeTotal_Object = MibScalar
tnPmonClearAttributeTotal = _TnPmonClearAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 3),
    _TnPmonClearAttributeTotal_Type()
)
tnPmonClearAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonClearAttributeTotal.setStatus("current")
_TnPmonClearTable_Object = MibTable
tnPmonClearTable = _TnPmonClearTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4)
)
if mibBuilder.loadTexts:
    tnPmonClearTable.setStatus("current")
_TnPmonClearEntry_Object = MibTableRow
tnPmonClearEntry = _TnPmonClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1)
)
tnPmonClearEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnPmonClearType"),
)
if mibBuilder.loadTexts:
    tnPmonClearEntry.setStatus("current")
_TnPmonClearType_Type = AluWdmPmonStatsClearType
_TnPmonClearType_Object = MibTableColumn
tnPmonClearType = _TnPmonClearType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 1),
    _TnPmonClearType_Type()
)
tnPmonClearType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonClearType.setStatus("current")
_TnPmonClearPortId_Type = TmnxPortID
_TnPmonClearPortId_Object = MibTableColumn
tnPmonClearPortId = _TnPmonClearPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 2),
    _TnPmonClearPortId_Type()
)
tnPmonClearPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearPortId.setStatus("current")
_TnPmonClearEncapValue_Type = TmnxEncapVal
_TnPmonClearEncapValue_Object = MibTableColumn
tnPmonClearEncapValue = _TnPmonClearEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 3),
    _TnPmonClearEncapValue_Type()
)
tnPmonClearEncapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearEncapValue.setStatus("current")
_TnPmonClearTestName_Type = SnmpAdminString
_TnPmonClearTestName_Object = MibTableColumn
tnPmonClearTestName = _TnPmonClearTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 4),
    _TnPmonClearTestName_Type()
)
tnPmonClearTestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearTestName.setStatus("current")


class _TnPmonClearInterval_Type(AluWdmStatsIntervalType):
    """Custom type tnPmonClearInterval based on AluWdmStatsIntervalType"""
    defaultValue = -1


_TnPmonClearInterval_Type.__name__ = "AluWdmStatsIntervalType"
_TnPmonClearInterval_Object = MibTableColumn
tnPmonClearInterval = _TnPmonClearInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 5),
    _TnPmonClearInterval_Type()
)
tnPmonClearInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearInterval.setStatus("current")


class _TnPmonClearBin_Type(AluWdmStatsBinNumber):
    """Custom type tnPmonClearBin based on AluWdmStatsBinNumber"""
    defaultValue = -1


_TnPmonClearBin_Type.__name__ = "AluWdmStatsBinNumber"
_TnPmonClearBin_Object = MibTableColumn
tnPmonClearBin = _TnPmonClearBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 6),
    _TnPmonClearBin_Type()
)
tnPmonClearBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearBin.setStatus("current")


class _TnPmonClearRoeMapperId_Type(Integer32):
    """Custom type tnPmonClearRoeMapperId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_TnPmonClearRoeMapperId_Type.__name__ = "Integer32"
_TnPmonClearRoeMapperId_Object = MibTableColumn
tnPmonClearRoeMapperId = _TnPmonClearRoeMapperId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 7),
    _TnPmonClearRoeMapperId_Type()
)
tnPmonClearRoeMapperId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearRoeMapperId.setStatus("current")


class _TnPmonClearRoeDeMapperId_Type(Integer32):
    """Custom type tnPmonClearRoeDeMapperId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_TnPmonClearRoeDeMapperId_Type.__name__ = "Integer32"
_TnPmonClearRoeDeMapperId_Object = MibTableColumn
tnPmonClearRoeDeMapperId = _TnPmonClearRoeDeMapperId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 8),
    _TnPmonClearRoeDeMapperId_Type()
)
tnPmonClearRoeDeMapperId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearRoeDeMapperId.setStatus("current")
_TnPmonTcaAttributeTotal_Type = Integer32
_TnPmonTcaAttributeTotal_Object = MibScalar
tnPmonTcaAttributeTotal = _TnPmonTcaAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 5),
    _TnPmonTcaAttributeTotal_Type()
)
tnPmonTcaAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonTcaAttributeTotal.setStatus("current")
_TnPmonTcaTable_Object = MibTable
tnPmonTcaTable = _TnPmonTcaTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6)
)
if mibBuilder.loadTexts:
    tnPmonTcaTable.setStatus("current")
_TnPmonTcaEntry_Object = MibTableRow
tnPmonTcaEntry = _TnPmonTcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1)
)
tnPmonTcaEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnPmonPolicyType"),
    (0, "TN-PMON-MIB", "tnPmonPolicyId"),
    (0, "TN-PMON-MIB", "tnPmonTcaInterval"),
    (0, "TN-PMON-MIB", "tnPmonTcaSubgroup"),
    (0, "TN-PMON-MIB", "tnPmonTcaId"),
)
if mibBuilder.loadTexts:
    tnPmonTcaEntry.setStatus("current")
_TnPmonTcaInterval_Type = AluWdmStatsIntervalType
_TnPmonTcaInterval_Object = MibTableColumn
tnPmonTcaInterval = _TnPmonTcaInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 1),
    _TnPmonTcaInterval_Type()
)
tnPmonTcaInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonTcaInterval.setStatus("current")
_TnPmonTcaSubgroup_Type = Integer32
_TnPmonTcaSubgroup_Object = MibTableColumn
tnPmonTcaSubgroup = _TnPmonTcaSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 2),
    _TnPmonTcaSubgroup_Type()
)
tnPmonTcaSubgroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonTcaSubgroup.setStatus("current")
_TnPmonTcaId_Type = Integer32
_TnPmonTcaId_Object = MibTableColumn
tnPmonTcaId = _TnPmonTcaId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 3),
    _TnPmonTcaId_Type()
)
tnPmonTcaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonTcaId.setStatus("current")
_TnPmonTcaVariable_Type = ObjectIdentifier
_TnPmonTcaVariable_Object = MibTableColumn
tnPmonTcaVariable = _TnPmonTcaVariable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 4),
    _TnPmonTcaVariable_Type()
)
tnPmonTcaVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonTcaVariable.setStatus("current")


class _TnPmonTcaValue_Type(SnmpAdminString):
    """Custom type tnPmonTcaValue based on SnmpAdminString"""
    defaultHexValue = "00"

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TnPmonTcaValue_Type.__name__ = "SnmpAdminString"
_TnPmonTcaValue_Object = MibTableColumn
tnPmonTcaValue = _TnPmonTcaValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 5),
    _TnPmonTcaValue_Type()
)
tnPmonTcaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonTcaValue.setStatus("current")
_TnEthPortStatsAttributeTotal_Type = Integer32
_TnEthPortStatsAttributeTotal_Object = MibScalar
tnEthPortStatsAttributeTotal = _TnEthPortStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 7),
    _TnEthPortStatsAttributeTotal_Type()
)
tnEthPortStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsAttributeTotal.setStatus("current")
_TnEthPortStatsTable_Object = MibTable
tnEthPortStatsTable = _TnEthPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8)
)
if mibBuilder.loadTexts:
    tnEthPortStatsTable.setStatus("current")
_TnEthPortStatsEntry_Object = MibTableRow
tnEthPortStatsEntry = _TnEthPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1)
)
tnEthPortStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnEthPortStatsPortId"),
    (0, "TN-PMON-MIB", "tnEthPortStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthPortStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthPortStatsEntry.setStatus("current")
_TnEthPortStatsPortId_Type = TmnxPortID
_TnEthPortStatsPortId_Object = MibTableColumn
tnEthPortStatsPortId = _TnEthPortStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 1),
    _TnEthPortStatsPortId_Type()
)
tnEthPortStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsPortId.setStatus("current")
_TnEthPortStatsInterval_Type = AluWdmStatsIntervalType
_TnEthPortStatsInterval_Object = MibTableColumn
tnEthPortStatsInterval = _TnEthPortStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 2),
    _TnEthPortStatsInterval_Type()
)
tnEthPortStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsInterval.setStatus("current")
_TnEthPortStatsBin_Type = AluWdmStatsBinNumber
_TnEthPortStatsBin_Object = MibTableColumn
tnEthPortStatsBin = _TnEthPortStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 3),
    _TnEthPortStatsBin_Type()
)
tnEthPortStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsBin.setStatus("current")
_TnEthPortStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthPortStatsBinStatus_Object = MibTableColumn
tnEthPortStatsBinStatus = _TnEthPortStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 4),
    _TnEthPortStatsBinStatus_Type()
)
tnEthPortStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsBinStatus.setStatus("current")
_TnEthPortStatsStartTime_Type = DateAndTime
_TnEthPortStatsStartTime_Object = MibTableColumn
tnEthPortStatsStartTime = _TnEthPortStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 5),
    _TnEthPortStatsStartTime_Type()
)
tnEthPortStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsStartTime.setStatus("current")
_TnEthPortStatsTotalMembers_Type = Integer32
_TnEthPortStatsTotalMembers_Object = MibTableColumn
tnEthPortStatsTotalMembers = _TnEthPortStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 6),
    _TnEthPortStatsTotalMembers_Type()
)
tnEthPortStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsTotalMembers.setStatus("current")
_TnEthPortStatsIfInOctets_Type = Counter64
_TnEthPortStatsIfInOctets_Object = MibTableColumn
tnEthPortStatsIfInOctets = _TnEthPortStatsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 7),
    _TnEthPortStatsIfInOctets_Type()
)
tnEthPortStatsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInOctets.setStatus("current")
_TnEthPortStatsIfInUcastPkts_Type = Counter64
_TnEthPortStatsIfInUcastPkts_Object = MibTableColumn
tnEthPortStatsIfInUcastPkts = _TnEthPortStatsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 8),
    _TnEthPortStatsIfInUcastPkts_Type()
)
tnEthPortStatsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInUcastPkts.setStatus("current")
_TnEthPortStatsIfInDiscards_Type = Counter64
_TnEthPortStatsIfInDiscards_Object = MibTableColumn
tnEthPortStatsIfInDiscards = _TnEthPortStatsIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 9),
    _TnEthPortStatsIfInDiscards_Type()
)
tnEthPortStatsIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInDiscards.setStatus("current")
_TnEthPortStatsIfInErrors_Type = Counter64
_TnEthPortStatsIfInErrors_Object = MibTableColumn
tnEthPortStatsIfInErrors = _TnEthPortStatsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 10),
    _TnEthPortStatsIfInErrors_Type()
)
tnEthPortStatsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInErrors.setStatus("current")
_TnEthPortStatsIfInUnknownProtos_Type = Counter64
_TnEthPortStatsIfInUnknownProtos_Object = MibTableColumn
tnEthPortStatsIfInUnknownProtos = _TnEthPortStatsIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 11),
    _TnEthPortStatsIfInUnknownProtos_Type()
)
tnEthPortStatsIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInUnknownProtos.setStatus("current")
_TnEthPortStatsIfInMulticastPkts_Type = Counter64
_TnEthPortStatsIfInMulticastPkts_Object = MibTableColumn
tnEthPortStatsIfInMulticastPkts = _TnEthPortStatsIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 12),
    _TnEthPortStatsIfInMulticastPkts_Type()
)
tnEthPortStatsIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInMulticastPkts.setStatus("current")
_TnEthPortStatsIfInBroadcastPkts_Type = Counter64
_TnEthPortStatsIfInBroadcastPkts_Object = MibTableColumn
tnEthPortStatsIfInBroadcastPkts = _TnEthPortStatsIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 13),
    _TnEthPortStatsIfInBroadcastPkts_Type()
)
tnEthPortStatsIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInBroadcastPkts.setStatus("current")
_TnEthPortStatsIfOutOctets_Type = Counter64
_TnEthPortStatsIfOutOctets_Object = MibTableColumn
tnEthPortStatsIfOutOctets = _TnEthPortStatsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 14),
    _TnEthPortStatsIfOutOctets_Type()
)
tnEthPortStatsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutOctets.setStatus("current")
_TnEthPortStatsIfOutUcastPkts_Type = Counter64
_TnEthPortStatsIfOutUcastPkts_Object = MibTableColumn
tnEthPortStatsIfOutUcastPkts = _TnEthPortStatsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 15),
    _TnEthPortStatsIfOutUcastPkts_Type()
)
tnEthPortStatsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutUcastPkts.setStatus("current")
_TnEthPortStatsIfOutDiscards_Type = Counter64
_TnEthPortStatsIfOutDiscards_Object = MibTableColumn
tnEthPortStatsIfOutDiscards = _TnEthPortStatsIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 16),
    _TnEthPortStatsIfOutDiscards_Type()
)
tnEthPortStatsIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutDiscards.setStatus("current")
_TnEthPortStatsIfOutErrors_Type = Counter64
_TnEthPortStatsIfOutErrors_Object = MibTableColumn
tnEthPortStatsIfOutErrors = _TnEthPortStatsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 17),
    _TnEthPortStatsIfOutErrors_Type()
)
tnEthPortStatsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutErrors.setStatus("current")
_TnEthPortStatsIfOutMulticastPkts_Type = Counter64
_TnEthPortStatsIfOutMulticastPkts_Object = MibTableColumn
tnEthPortStatsIfOutMulticastPkts = _TnEthPortStatsIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 18),
    _TnEthPortStatsIfOutMulticastPkts_Type()
)
tnEthPortStatsIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutMulticastPkts.setStatus("current")
_TnEthPortStatsIfOutBroadcastPkts_Type = Counter64
_TnEthPortStatsIfOutBroadcastPkts_Object = MibTableColumn
tnEthPortStatsIfOutBroadcastPkts = _TnEthPortStatsIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 19),
    _TnEthPortStatsIfOutBroadcastPkts_Type()
)
tnEthPortStatsIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutBroadcastPkts.setStatus("current")
_TnEthPortStatsIfInPkts_Type = Counter64
_TnEthPortStatsIfInPkts_Object = MibTableColumn
tnEthPortStatsIfInPkts = _TnEthPortStatsIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 20),
    _TnEthPortStatsIfInPkts_Type()
)
tnEthPortStatsIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInPkts.setStatus("current")
_TnEthPortStatsIfOutPkts_Type = Counter64
_TnEthPortStatsIfOutPkts_Object = MibTableColumn
tnEthPortStatsIfOutPkts = _TnEthPortStatsIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 21),
    _TnEthPortStatsIfOutPkts_Type()
)
tnEthPortStatsIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutPkts.setStatus("current")
_TnEthPortEtherStatsDropEvents_Type = Counter64
_TnEthPortEtherStatsDropEvents_Object = MibTableColumn
tnEthPortEtherStatsDropEvents = _TnEthPortEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 22),
    _TnEthPortEtherStatsDropEvents_Type()
)
tnEthPortEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsDropEvents.setStatus("current")
_TnEthPortEtherStatsBroadcastPkts_Type = Counter64
_TnEthPortEtherStatsBroadcastPkts_Object = MibTableColumn
tnEthPortEtherStatsBroadcastPkts = _TnEthPortEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 23),
    _TnEthPortEtherStatsBroadcastPkts_Type()
)
tnEthPortEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsBroadcastPkts.setStatus("current")
_TnEthPortEtherStatsMulticastPkts_Type = Counter64
_TnEthPortEtherStatsMulticastPkts_Object = MibTableColumn
tnEthPortEtherStatsMulticastPkts = _TnEthPortEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 24),
    _TnEthPortEtherStatsMulticastPkts_Type()
)
tnEthPortEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsMulticastPkts.setStatus("current")
_TnEthPortEtherStatsCRCAlignErrors_Type = Counter64
_TnEthPortEtherStatsCRCAlignErrors_Object = MibTableColumn
tnEthPortEtherStatsCRCAlignErrors = _TnEthPortEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 25),
    _TnEthPortEtherStatsCRCAlignErrors_Type()
)
tnEthPortEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsCRCAlignErrors.setStatus("current")
_TnEthPortEtherStatsUndersizePkts_Type = Counter64
_TnEthPortEtherStatsUndersizePkts_Object = MibTableColumn
tnEthPortEtherStatsUndersizePkts = _TnEthPortEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 26),
    _TnEthPortEtherStatsUndersizePkts_Type()
)
tnEthPortEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsUndersizePkts.setStatus("current")
_TnEthPortEtherStatsOversizePkts_Type = Counter64
_TnEthPortEtherStatsOversizePkts_Object = MibTableColumn
tnEthPortEtherStatsOversizePkts = _TnEthPortEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 27),
    _TnEthPortEtherStatsOversizePkts_Type()
)
tnEthPortEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsOversizePkts.setStatus("current")
_TnEthPortEtherStatsFragments_Type = Counter64
_TnEthPortEtherStatsFragments_Object = MibTableColumn
tnEthPortEtherStatsFragments = _TnEthPortEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 28),
    _TnEthPortEtherStatsFragments_Type()
)
tnEthPortEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsFragments.setStatus("current")
_TnEthPortEtherStatsJabbers_Type = Counter64
_TnEthPortEtherStatsJabbers_Object = MibTableColumn
tnEthPortEtherStatsJabbers = _TnEthPortEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 29),
    _TnEthPortEtherStatsJabbers_Type()
)
tnEthPortEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsJabbers.setStatus("current")
_TnEthPortEtherStatsCollisions_Type = Counter64
_TnEthPortEtherStatsCollisions_Object = MibTableColumn
tnEthPortEtherStatsCollisions = _TnEthPortEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 30),
    _TnEthPortEtherStatsCollisions_Type()
)
tnEthPortEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsCollisions.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts = _TnEthPortEtherStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 31),
    _TnEthPortEtherStatsHighCapacityPkts_Type()
)
tnEthPortEtherStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts.setStatus("current")
_TnEthPortEtherStatsHighCapacityOctets_Type = Counter64
_TnEthPortEtherStatsHighCapacityOctets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityOctets = _TnEthPortEtherStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 32),
    _TnEthPortEtherStatsHighCapacityOctets_Type()
)
tnEthPortEtherStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityOctets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts64Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts64Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts64Octets = _TnEthPortEtherStatsHighCapacityPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 33),
    _TnEthPortEtherStatsHighCapacityPkts64Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts64Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts65to127Octets = _TnEthPortEtherStatsHighCapacityPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 34),
    _TnEthPortEtherStatsHighCapacityPkts65to127Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts65to127Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts128to255Octets = _TnEthPortEtherStatsHighCapacityPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 35),
    _TnEthPortEtherStatsHighCapacityPkts128to255Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts128to255Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts256to511Octets = _TnEthPortEtherStatsHighCapacityPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 36),
    _TnEthPortEtherStatsHighCapacityPkts256to511Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts256to511Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts512to1023Octets = _TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 37),
    _TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts512to1023Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts1024to1518Octets = _TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 38),
    _TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts1024to1518Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets = _TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 39),
    _TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Type()
)
tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets.setStatus("current")
_TnEthPortEgrQueueStatsAttributeTotal_Type = Integer32
_TnEthPortEgrQueueStatsAttributeTotal_Object = MibScalar
tnEthPortEgrQueueStatsAttributeTotal = _TnEthPortEgrQueueStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 9),
    _TnEthPortEgrQueueStatsAttributeTotal_Type()
)
tnEthPortEgrQueueStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsAttributeTotal.setStatus("current")
_TnEthPortEgrQueueStatsTable_Object = MibTable
tnEthPortEgrQueueStatsTable = _TnEthPortEgrQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10)
)
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsTable.setStatus("current")
_TnEthPortEgrQueueStatsEntry_Object = MibTableRow
tnEthPortEgrQueueStatsEntry = _TnEthPortEgrQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1)
)
tnEthPortEgrQueueStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnEthPortStatsPortId"),
    (0, "TN-PMON-MIB", "tnEthPortStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthPortStatsBin"),
    (0, "TN-PMON-MIB", "tnEthPortStatsQueueId"),
)
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsEntry.setStatus("current")


class _TnEthPortStatsQueueId_Type(TQueueId):
    """Custom type tnEthPortStatsQueueId based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnEthPortStatsQueueId_Type.__name__ = "TQueueId"
_TnEthPortStatsQueueId_Object = MibTableColumn
tnEthPortStatsQueueId = _TnEthPortStatsQueueId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 1),
    _TnEthPortStatsQueueId_Type()
)
tnEthPortStatsQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsQueueId.setStatus("current")
_TnEthPortEgrQueueStatsInProfilePktsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsInProfilePktsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfilePktsForwarded = _TnEthPortEgrQueueStatsInProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 2),
    _TnEthPortEgrQueueStatsInProfilePktsForwarded_Type()
)
tnEthPortEgrQueueStatsInProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfilePktsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfilePktsForwarded = _TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 3),
    _TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Type()
)
tnEthPortEgrQueueStatsOutOfProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfilePktsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfileOctetsForwarded = _TnEthPortEgrQueueStatsInProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 4),
    _TnEthPortEgrQueueStatsInProfileOctetsForwarded_Type()
)
tnEthPortEgrQueueStatsInProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfileOctetsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded = _TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 5),
    _TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Type()
)
tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsInProfilePktsDropped_Type = Counter64
_TnEthPortEgrQueueStatsInProfilePktsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfilePktsDropped = _TnEthPortEgrQueueStatsInProfilePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 6),
    _TnEthPortEgrQueueStatsInProfilePktsDropped_Type()
)
tnEthPortEgrQueueStatsInProfilePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfilePktsDropped.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfilePktsDropped = _TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 7),
    _TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Type()
)
tnEthPortEgrQueueStatsOutOfProfilePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfilePktsDropped.setStatus("current")
_TnEthPortEgrQueueStatsInProfileOctetsDropped_Type = Counter64
_TnEthPortEgrQueueStatsInProfileOctetsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfileOctetsDropped = _TnEthPortEgrQueueStatsInProfileOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 8),
    _TnEthPortEgrQueueStatsInProfileOctetsDropped_Type()
)
tnEthPortEgrQueueStatsInProfileOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfileOctetsDropped.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfileOctetsDropped = _TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 9),
    _TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Type()
)
tnEthPortEgrQueueStatsOutOfProfileOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfileOctetsDropped.setStatus("current")
_TnSapStatsAttributeTotal_Type = Integer32
_TnSapStatsAttributeTotal_Object = MibScalar
tnSapStatsAttributeTotal = _TnSapStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 11),
    _TnSapStatsAttributeTotal_Type()
)
tnSapStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsAttributeTotal.setStatus("current")
_TnSapStatsTable_Object = MibTable
tnSapStatsTable = _TnSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12)
)
if mibBuilder.loadTexts:
    tnSapStatsTable.setStatus("current")
_TnSapStatsEntry_Object = MibTableRow
tnSapStatsEntry = _TnSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1)
)
tnSapStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnSapStatsPortId"),
    (0, "TN-PMON-MIB", "tnSapStatsEncapVal"),
    (0, "TN-PMON-MIB", "tnSapStatsInterval"),
    (0, "TN-PMON-MIB", "tnSapStatsBin"),
)
if mibBuilder.loadTexts:
    tnSapStatsEntry.setStatus("current")
_TnSapStatsPortId_Type = TmnxPortID
_TnSapStatsPortId_Object = MibTableColumn
tnSapStatsPortId = _TnSapStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 1),
    _TnSapStatsPortId_Type()
)
tnSapStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsPortId.setStatus("current")
_TnSapStatsEncapVal_Type = TmnxEncapVal
_TnSapStatsEncapVal_Object = MibTableColumn
tnSapStatsEncapVal = _TnSapStatsEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 2),
    _TnSapStatsEncapVal_Type()
)
tnSapStatsEncapVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsEncapVal.setStatus("current")
_TnSapStatsInterval_Type = AluWdmStatsIntervalType
_TnSapStatsInterval_Object = MibTableColumn
tnSapStatsInterval = _TnSapStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 3),
    _TnSapStatsInterval_Type()
)
tnSapStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsInterval.setStatus("current")
_TnSapStatsBin_Type = AluWdmStatsBinNumber
_TnSapStatsBin_Object = MibTableColumn
tnSapStatsBin = _TnSapStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 4),
    _TnSapStatsBin_Type()
)
tnSapStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsBin.setStatus("current")
_TnSapStatsBinStatus_Type = AluWdmStatsBinStatus
_TnSapStatsBinStatus_Object = MibTableColumn
tnSapStatsBinStatus = _TnSapStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 5),
    _TnSapStatsBinStatus_Type()
)
tnSapStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsBinStatus.setStatus("current")
_TnSapStatsStartTime_Type = DateAndTime
_TnSapStatsStartTime_Object = MibTableColumn
tnSapStatsStartTime = _TnSapStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 6),
    _TnSapStatsStartTime_Type()
)
tnSapStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsStartTime.setStatus("current")
_TnSapStatsTotalMembers_Type = Integer32
_TnSapStatsTotalMembers_Object = MibTableColumn
tnSapStatsTotalMembers = _TnSapStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 7),
    _TnSapStatsTotalMembers_Type()
)
tnSapStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsTotalMembers.setStatus("current")
_TnSapStatsIngressPktsForwarded_Type = Counter64
_TnSapStatsIngressPktsForwarded_Object = MibTableColumn
tnSapStatsIngressPktsForwarded = _TnSapStatsIngressPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 8),
    _TnSapStatsIngressPktsForwarded_Type()
)
tnSapStatsIngressPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressPktsForwarded.setStatus("current")
_TnSapStatsIngressOctetsForwarded_Type = Counter64
_TnSapStatsIngressOctetsForwarded_Object = MibTableColumn
tnSapStatsIngressOctetsForwarded = _TnSapStatsIngressOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 9),
    _TnSapStatsIngressOctetsForwarded_Type()
)
tnSapStatsIngressOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressOctetsForwarded.setStatus("current")
_TnSapStatsEgressPktsForwarded_Type = Counter64
_TnSapStatsEgressPktsForwarded_Object = MibTableColumn
tnSapStatsEgressPktsForwarded = _TnSapStatsEgressPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 10),
    _TnSapStatsEgressPktsForwarded_Type()
)
tnSapStatsEgressPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsEgressPktsForwarded.setStatus("current")
_TnSapStatsEgressOctetsForwarded_Type = Counter64
_TnSapStatsEgressOctetsForwarded_Object = MibTableColumn
tnSapStatsEgressOctetsForwarded = _TnSapStatsEgressOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 11),
    _TnSapStatsEgressOctetsForwarded_Type()
)
tnSapStatsEgressOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsEgressOctetsForwarded.setStatus("current")
_TnSapStatsIngressPktsDropped_Type = Counter64
_TnSapStatsIngressPktsDropped_Object = MibTableColumn
tnSapStatsIngressPktsDropped = _TnSapStatsIngressPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 12),
    _TnSapStatsIngressPktsDropped_Type()
)
tnSapStatsIngressPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressPktsDropped.setStatus("current")
_TnSapStatsIngressOctetsDropped_Type = Counter64
_TnSapStatsIngressOctetsDropped_Object = MibTableColumn
tnSapStatsIngressOctetsDropped = _TnSapStatsIngressOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 13),
    _TnSapStatsIngressOctetsDropped_Type()
)
tnSapStatsIngressOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressOctetsDropped.setStatus("current")
_TnSapStatsIngressExtraTagPktsDropped_Type = Counter64
_TnSapStatsIngressExtraTagPktsDropped_Object = MibTableColumn
tnSapStatsIngressExtraTagPktsDropped = _TnSapStatsIngressExtraTagPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 14),
    _TnSapStatsIngressExtraTagPktsDropped_Type()
)
tnSapStatsIngressExtraTagPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressExtraTagPktsDropped.setStatus("current")
_TnSapStatsIngressExtraTagOctetsDropped_Type = Counter64
_TnSapStatsIngressExtraTagOctetsDropped_Object = MibTableColumn
tnSapStatsIngressExtraTagOctetsDropped = _TnSapStatsIngressExtraTagOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 15),
    _TnSapStatsIngressExtraTagOctetsDropped_Type()
)
tnSapStatsIngressExtraTagOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressExtraTagOctetsDropped.setStatus("current")
_TnSapMeterStatsAttributeTotal_Type = Integer32
_TnSapMeterStatsAttributeTotal_Object = MibScalar
tnSapMeterStatsAttributeTotal = _TnSapMeterStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 13),
    _TnSapMeterStatsAttributeTotal_Type()
)
tnSapMeterStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsAttributeTotal.setStatus("current")
_TnSapMeterStatsTable_Object = MibTable
tnSapMeterStatsTable = _TnSapMeterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14)
)
if mibBuilder.loadTexts:
    tnSapMeterStatsTable.setStatus("current")
_TnSapMeterStatsEntry_Object = MibTableRow
tnSapMeterStatsEntry = _TnSapMeterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1)
)
tnSapMeterStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnSapStatsPortId"),
    (0, "TN-PMON-MIB", "tnSapStatsEncapVal"),
    (0, "TN-PMON-MIB", "tnSapStatsInterval"),
    (0, "TN-PMON-MIB", "tnSapStatsBin"),
    (0, "TN-PMON-MIB", "tnSapStatsMeterId"),
)
if mibBuilder.loadTexts:
    tnSapMeterStatsEntry.setStatus("current")
_TnSapStatsMeterId_Type = TSapIngQueueId
_TnSapStatsMeterId_Object = MibTableColumn
tnSapStatsMeterId = _TnSapStatsMeterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 1),
    _TnSapStatsMeterId_Type()
)
tnSapStatsMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsMeterId.setStatus("current")
_TnSapMeterStatsInProfilePktsForwarded_Type = Counter64
_TnSapMeterStatsInProfilePktsForwarded_Object = MibTableColumn
tnSapMeterStatsInProfilePktsForwarded = _TnSapMeterStatsInProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 2),
    _TnSapMeterStatsInProfilePktsForwarded_Type()
)
tnSapMeterStatsInProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsInProfilePktsForwarded.setStatus("current")
_TnSapMeterStatsOutOfProfilePktsForwarded_Type = Counter64
_TnSapMeterStatsOutOfProfilePktsForwarded_Object = MibTableColumn
tnSapMeterStatsOutOfProfilePktsForwarded = _TnSapMeterStatsOutOfProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 3),
    _TnSapMeterStatsOutOfProfilePktsForwarded_Type()
)
tnSapMeterStatsOutOfProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsOutOfProfilePktsForwarded.setStatus("current")
_TnSapMeterStatsInProfileOctetsForwarded_Type = Counter64
_TnSapMeterStatsInProfileOctetsForwarded_Object = MibTableColumn
tnSapMeterStatsInProfileOctetsForwarded = _TnSapMeterStatsInProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 4),
    _TnSapMeterStatsInProfileOctetsForwarded_Type()
)
tnSapMeterStatsInProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsInProfileOctetsForwarded.setStatus("current")
_TnSapMeterStatsOutOfProfileOctetsForwarded_Type = Counter64
_TnSapMeterStatsOutOfProfileOctetsForwarded_Object = MibTableColumn
tnSapMeterStatsOutOfProfileOctetsForwarded = _TnSapMeterStatsOutOfProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 5),
    _TnSapMeterStatsOutOfProfileOctetsForwarded_Type()
)
tnSapMeterStatsOutOfProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsOutOfProfileOctetsForwarded.setStatus("current")
_TnEthCfmTWSlmStatsAttributeTotal_Type = Integer32
_TnEthCfmTWSlmStatsAttributeTotal_Object = MibScalar
tnEthCfmTWSlmStatsAttributeTotal = _TnEthCfmTWSlmStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 15),
    _TnEthCfmTWSlmStatsAttributeTotal_Type()
)
tnEthCfmTWSlmStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsAttributeTotal.setStatus("current")
_TnEthCfmTWSlmStatsTable_Object = MibTable
tnEthCfmTWSlmStatsTable = _TnEthCfmTWSlmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16)
)
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsTable.setStatus("current")
_TnEthCfmTWSlmStatsEntry_Object = MibTableRow
tnEthCfmTWSlmStatsEntry = _TnEthCfmTWSlmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1)
)
tnEthCfmTWSlmStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnEthCfmTWSlmStatsTestName"),
    (0, "TN-PMON-MIB", "tnEthCfmTWSlmStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthCfmTWSlmStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsEntry.setStatus("current")
_TnEthCfmTWSlmStatsTestName_Type = SnmpAdminString
_TnEthCfmTWSlmStatsTestName_Object = MibTableColumn
tnEthCfmTWSlmStatsTestName = _TnEthCfmTWSlmStatsTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 1),
    _TnEthCfmTWSlmStatsTestName_Type()
)
tnEthCfmTWSlmStatsTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsTestName.setStatus("current")
_TnEthCfmTWSlmStatsInterval_Type = AluWdmStatsIntervalType
_TnEthCfmTWSlmStatsInterval_Object = MibTableColumn
tnEthCfmTWSlmStatsInterval = _TnEthCfmTWSlmStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 2),
    _TnEthCfmTWSlmStatsInterval_Type()
)
tnEthCfmTWSlmStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsInterval.setStatus("current")
_TnEthCfmTWSlmStatsBin_Type = AluWdmStatsBinNumber
_TnEthCfmTWSlmStatsBin_Object = MibTableColumn
tnEthCfmTWSlmStatsBin = _TnEthCfmTWSlmStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 3),
    _TnEthCfmTWSlmStatsBin_Type()
)
tnEthCfmTWSlmStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsBin.setStatus("current")
_TnEthCfmTWSlmStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthCfmTWSlmStatsBinStatus_Object = MibTableColumn
tnEthCfmTWSlmStatsBinStatus = _TnEthCfmTWSlmStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 4),
    _TnEthCfmTWSlmStatsBinStatus_Type()
)
tnEthCfmTWSlmStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsBinStatus.setStatus("current")
_TnEthCfmTWSlmStatsStartTime_Type = DateAndTime
_TnEthCfmTWSlmStatsStartTime_Object = MibTableColumn
tnEthCfmTWSlmStatsStartTime = _TnEthCfmTWSlmStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 5),
    _TnEthCfmTWSlmStatsStartTime_Type()
)
tnEthCfmTWSlmStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsStartTime.setStatus("current")
_TnEthCfmTWSlmStatsTotalMembers_Type = Integer32
_TnEthCfmTWSlmStatsTotalMembers_Object = MibTableColumn
tnEthCfmTWSlmStatsTotalMembers = _TnEthCfmTWSlmStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 6),
    _TnEthCfmTWSlmStatsTotalMembers_Type()
)
tnEthCfmTWSlmStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsTotalMembers.setStatus("current")
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioMin = _TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 7),
    _TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Type()
)
tnEthCfmTWSlmStatsNearEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage = _TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 8),
    _TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Type()
)
tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioMax = _TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 9),
    _TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Type()
)
tnEthCfmTWSlmStatsNearEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioMin = _TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 10),
    _TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Type()
)
tnEthCfmTWSlmStatsFarEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage = _TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 11),
    _TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Type()
)
tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioMax = _TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 12),
    _TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Type()
)
tnEthCfmTWSlmStatsFarEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWSlmStatsNearEndHighLoss_Type = Integer32
_TnEthCfmTWSlmStatsNearEndHighLoss_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndHighLoss = _TnEthCfmTWSlmStatsNearEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 13),
    _TnEthCfmTWSlmStatsNearEndHighLoss_Type()
)
tnEthCfmTWSlmStatsNearEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndHighLoss.setStatus("current")
_TnEthCfmTWSlmStatsFarEndHighLoss_Type = Integer32
_TnEthCfmTWSlmStatsFarEndHighLoss_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndHighLoss = _TnEthCfmTWSlmStatsFarEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 14),
    _TnEthCfmTWSlmStatsFarEndHighLoss_Type()
)
tnEthCfmTWSlmStatsFarEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndHighLoss.setStatus("current")
_TnEthCfmTWSlmStatsNearEndUnavailable_Type = Integer32
_TnEthCfmTWSlmStatsNearEndUnavailable_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndUnavailable = _TnEthCfmTWSlmStatsNearEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 15),
    _TnEthCfmTWSlmStatsNearEndUnavailable_Type()
)
tnEthCfmTWSlmStatsNearEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndUnavailable.setStatus("current")
_TnEthCfmTWSlmStatsFarEndUnavailable_Type = Integer32
_TnEthCfmTWSlmStatsFarEndUnavailable_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndUnavailable = _TnEthCfmTWSlmStatsFarEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 16),
    _TnEthCfmTWSlmStatsFarEndUnavailable_Type()
)
tnEthCfmTWSlmStatsFarEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndUnavailable.setStatus("current")
_TnEthCfmTWDmStatsAttributeTotal_Type = Integer32
_TnEthCfmTWDmStatsAttributeTotal_Object = MibScalar
tnEthCfmTWDmStatsAttributeTotal = _TnEthCfmTWDmStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 17),
    _TnEthCfmTWDmStatsAttributeTotal_Type()
)
tnEthCfmTWDmStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsAttributeTotal.setStatus("current")
_TnEthCfmTWDmStatsTable_Object = MibTable
tnEthCfmTWDmStatsTable = _TnEthCfmTWDmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18)
)
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsTable.setStatus("current")
_TnEthCfmTWDmStatsEntry_Object = MibTableRow
tnEthCfmTWDmStatsEntry = _TnEthCfmTWDmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1)
)
tnEthCfmTWDmStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnEthCfmTWDmStatsTestName"),
    (0, "TN-PMON-MIB", "tnEthCfmTWDmStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthCfmTWDmStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsEntry.setStatus("current")
_TnEthCfmTWDmStatsTestName_Type = SnmpAdminString
_TnEthCfmTWDmStatsTestName_Object = MibTableColumn
tnEthCfmTWDmStatsTestName = _TnEthCfmTWDmStatsTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 1),
    _TnEthCfmTWDmStatsTestName_Type()
)
tnEthCfmTWDmStatsTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsTestName.setStatus("current")
_TnEthCfmTWDmStatsInterval_Type = AluWdmStatsIntervalType
_TnEthCfmTWDmStatsInterval_Object = MibTableColumn
tnEthCfmTWDmStatsInterval = _TnEthCfmTWDmStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 2),
    _TnEthCfmTWDmStatsInterval_Type()
)
tnEthCfmTWDmStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsInterval.setStatus("current")
_TnEthCfmTWDmStatsBin_Type = AluWdmStatsBinNumber
_TnEthCfmTWDmStatsBin_Object = MibTableColumn
tnEthCfmTWDmStatsBin = _TnEthCfmTWDmStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 3),
    _TnEthCfmTWDmStatsBin_Type()
)
tnEthCfmTWDmStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsBin.setStatus("current")
_TnEthCfmTWDmStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthCfmTWDmStatsBinStatus_Object = MibTableColumn
tnEthCfmTWDmStatsBinStatus = _TnEthCfmTWDmStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 4),
    _TnEthCfmTWDmStatsBinStatus_Type()
)
tnEthCfmTWDmStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsBinStatus.setStatus("current")
_TnEthCfmTWDmStatsStartTime_Type = DateAndTime
_TnEthCfmTWDmStatsStartTime_Object = MibTableColumn
tnEthCfmTWDmStatsStartTime = _TnEthCfmTWDmStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 5),
    _TnEthCfmTWDmStatsStartTime_Type()
)
tnEthCfmTWDmStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsStartTime.setStatus("current")
_TnEthCfmTWDmStatsTotalMembers_Type = Integer32
_TnEthCfmTWDmStatsTotalMembers_Object = MibTableColumn
tnEthCfmTWDmStatsTotalMembers = _TnEthCfmTWDmStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 6),
    _TnEthCfmTWDmStatsTotalMembers_Type()
)
tnEthCfmTWDmStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsTotalMembers.setStatus("current")
_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Type = Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Object = MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayMin = _TnEthCfmTWDmStatsRoundTripFrameDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 7),
    _TnEthCfmTWDmStatsRoundTripFrameDelayMin_Type()
)
tnEthCfmTWDmStatsRoundTripFrameDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsRoundTripFrameDelayMin.setStatus("current")
_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Type = Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Object = MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayAverage = _TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 8),
    _TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Type()
)
tnEthCfmTWDmStatsRoundTripFrameDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsRoundTripFrameDelayAverage.setStatus("current")
_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Type = Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Object = MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayMax = _TnEthCfmTWDmStatsRoundTripFrameDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 9),
    _TnEthCfmTWDmStatsRoundTripFrameDelayMax_Type()
)
tnEthCfmTWDmStatsRoundTripFrameDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsRoundTripFrameDelayMax.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationMin = _TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 10),
    _TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayVariationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayVariationMin.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage = _TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 11),
    _TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationMax = _TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 12),
    _TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayVariationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayVariationMax.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationMin = _TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 13),
    _TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayVariationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayVariationMin.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage = _TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 14),
    _TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationMax = _TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 15),
    _TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayVariationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayVariationMax.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayMin_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayMin_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayMin = _TnEthCfmTWDmStatsNearEndFrameDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 16),
    _TnEthCfmTWDmStatsNearEndFrameDelayMin_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayMin.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayAverage = _TnEthCfmTWDmStatsNearEndFrameDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 17),
    _TnEthCfmTWDmStatsNearEndFrameDelayAverage_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayAverage.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayMax_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayMax_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayMax = _TnEthCfmTWDmStatsNearEndFrameDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 18),
    _TnEthCfmTWDmStatsNearEndFrameDelayMax_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayMax.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayMin_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayMin_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayMin = _TnEthCfmTWDmStatsFarEndFrameDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 19),
    _TnEthCfmTWDmStatsFarEndFrameDelayMin_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayMin.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayAverage = _TnEthCfmTWDmStatsFarEndFrameDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 20),
    _TnEthCfmTWDmStatsFarEndFrameDelayAverage_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayAverage.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayMax_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayMax_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayMax = _TnEthCfmTWDmStatsFarEndFrameDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 21),
    _TnEthCfmTWDmStatsFarEndFrameDelayMax_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayMax.setStatus("current")
_TnEthCfmTWLmStatsAttributeTotal_Type = Integer32
_TnEthCfmTWLmStatsAttributeTotal_Object = MibScalar
tnEthCfmTWLmStatsAttributeTotal = _TnEthCfmTWLmStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 19),
    _TnEthCfmTWLmStatsAttributeTotal_Type()
)
tnEthCfmTWLmStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsAttributeTotal.setStatus("current")
_TnEthCfmTWLmStatsTable_Object = MibTable
tnEthCfmTWLmStatsTable = _TnEthCfmTWLmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20)
)
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsTable.setStatus("current")
_TnEthCfmTWLmStatsEntry_Object = MibTableRow
tnEthCfmTWLmStatsEntry = _TnEthCfmTWLmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1)
)
tnEthCfmTWLmStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnEthCfmTWLmStatsTestName"),
    (0, "TN-PMON-MIB", "tnEthCfmTWLmStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthCfmTWLmStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsEntry.setStatus("current")
_TnEthCfmTWLmStatsTestName_Type = SnmpAdminString
_TnEthCfmTWLmStatsTestName_Object = MibTableColumn
tnEthCfmTWLmStatsTestName = _TnEthCfmTWLmStatsTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 1),
    _TnEthCfmTWLmStatsTestName_Type()
)
tnEthCfmTWLmStatsTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsTestName.setStatus("current")
_TnEthCfmTWLmStatsInterval_Type = AluWdmStatsIntervalType
_TnEthCfmTWLmStatsInterval_Object = MibTableColumn
tnEthCfmTWLmStatsInterval = _TnEthCfmTWLmStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 2),
    _TnEthCfmTWLmStatsInterval_Type()
)
tnEthCfmTWLmStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsInterval.setStatus("current")
_TnEthCfmTWLmStatsBin_Type = AluWdmStatsBinNumber
_TnEthCfmTWLmStatsBin_Object = MibTableColumn
tnEthCfmTWLmStatsBin = _TnEthCfmTWLmStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 3),
    _TnEthCfmTWLmStatsBin_Type()
)
tnEthCfmTWLmStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsBin.setStatus("current")
_TnEthCfmTWLmStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthCfmTWLmStatsBinStatus_Object = MibTableColumn
tnEthCfmTWLmStatsBinStatus = _TnEthCfmTWLmStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 4),
    _TnEthCfmTWLmStatsBinStatus_Type()
)
tnEthCfmTWLmStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsBinStatus.setStatus("current")
_TnEthCfmTWLmStatsStartTime_Type = DateAndTime
_TnEthCfmTWLmStatsStartTime_Object = MibTableColumn
tnEthCfmTWLmStatsStartTime = _TnEthCfmTWLmStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 5),
    _TnEthCfmTWLmStatsStartTime_Type()
)
tnEthCfmTWLmStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsStartTime.setStatus("current")
_TnEthCfmTWLmStatsTotalMembers_Type = Integer32
_TnEthCfmTWLmStatsTotalMembers_Object = MibTableColumn
tnEthCfmTWLmStatsTotalMembers = _TnEthCfmTWLmStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 6),
    _TnEthCfmTWLmStatsTotalMembers_Type()
)
tnEthCfmTWLmStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsTotalMembers.setStatus("current")
_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioMin = _TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 7),
    _TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Type()
)
tnEthCfmTWLmStatsNearEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioAverage = _TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 8),
    _TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Type()
)
tnEthCfmTWLmStatsNearEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioMax = _TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 9),
    _TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Type()
)
tnEthCfmTWLmStatsNearEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioMin = _TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 10),
    _TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Type()
)
tnEthCfmTWLmStatsFarEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioAverage = _TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 11),
    _TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Type()
)
tnEthCfmTWLmStatsFarEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioMax = _TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 12),
    _TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Type()
)
tnEthCfmTWLmStatsFarEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWLmStatsNearEndHighLoss_Type = Integer32
_TnEthCfmTWLmStatsNearEndHighLoss_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndHighLoss = _TnEthCfmTWLmStatsNearEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 13),
    _TnEthCfmTWLmStatsNearEndHighLoss_Type()
)
tnEthCfmTWLmStatsNearEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndHighLoss.setStatus("current")
_TnEthCfmTWLmStatsFarEndHighLoss_Type = Integer32
_TnEthCfmTWLmStatsFarEndHighLoss_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndHighLoss = _TnEthCfmTWLmStatsFarEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 14),
    _TnEthCfmTWLmStatsFarEndHighLoss_Type()
)
tnEthCfmTWLmStatsFarEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndHighLoss.setStatus("current")
_TnEthCfmTWLmStatsNearEndUnavailable_Type = Integer32
_TnEthCfmTWLmStatsNearEndUnavailable_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndUnavailable = _TnEthCfmTWLmStatsNearEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 15),
    _TnEthCfmTWLmStatsNearEndUnavailable_Type()
)
tnEthCfmTWLmStatsNearEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndUnavailable.setStatus("current")
_TnEthCfmTWLmStatsFarEndUnavailable_Type = Integer32
_TnEthCfmTWLmStatsFarEndUnavailable_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndUnavailable = _TnEthCfmTWLmStatsFarEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 16),
    _TnEthCfmTWLmStatsFarEndUnavailable_Type()
)
tnEthCfmTWLmStatsFarEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndUnavailable.setStatus("current")
_TnEthCfmTWLmStatsTransmittedLMMFrame_Type = Counter64
_TnEthCfmTWLmStatsTransmittedLMMFrame_Object = MibTableColumn
tnEthCfmTWLmStatsTransmittedLMMFrame = _TnEthCfmTWLmStatsTransmittedLMMFrame_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 17),
    _TnEthCfmTWLmStatsTransmittedLMMFrame_Type()
)
tnEthCfmTWLmStatsTransmittedLMMFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsTransmittedLMMFrame.setStatus("current")
_TnEthCfmTWLmStatsReceivedLMRFrame_Type = Counter64
_TnEthCfmTWLmStatsReceivedLMRFrame_Object = MibTableColumn
tnEthCfmTWLmStatsReceivedLMRFrame = _TnEthCfmTWLmStatsReceivedLMRFrame_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 18),
    _TnEthCfmTWLmStatsReceivedLMRFrame_Type()
)
tnEthCfmTWLmStatsReceivedLMRFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsReceivedLMRFrame.setStatus("current")
_TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Type = Counter64
_TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndTransmittedDataFrame = _TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 19),
    _TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Type()
)
tnEthCfmTWLmStatsNearEndTransmittedDataFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndTransmittedDataFrame.setStatus("current")
_TnEthCfmTWLmStatsNearEndReceivedDataFrame_Type = Counter64
_TnEthCfmTWLmStatsNearEndReceivedDataFrame_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndReceivedDataFrame = _TnEthCfmTWLmStatsNearEndReceivedDataFrame_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 20),
    _TnEthCfmTWLmStatsNearEndReceivedDataFrame_Type()
)
tnEthCfmTWLmStatsNearEndReceivedDataFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndReceivedDataFrame.setStatus("current")
_TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Type = Counter64
_TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndTransmittedDataFrame = _TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 21),
    _TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Type()
)
tnEthCfmTWLmStatsFarEndTransmittedDataFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndTransmittedDataFrame.setStatus("current")
_TnEthCfmTWLmStatsFarEndReceivedDataFrame_Type = Counter64
_TnEthCfmTWLmStatsFarEndReceivedDataFrame_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndReceivedDataFrame = _TnEthCfmTWLmStatsFarEndReceivedDataFrame_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 22),
    _TnEthCfmTWLmStatsFarEndReceivedDataFrame_Type()
)
tnEthCfmTWLmStatsFarEndReceivedDataFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndReceivedDataFrame.setStatus("current")
_TnPktWanifStatsAttributeTotal_Type = Integer32
_TnPktWanifStatsAttributeTotal_Object = MibScalar
tnPktWanifStatsAttributeTotal = _TnPktWanifStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 21),
    _TnPktWanifStatsAttributeTotal_Type()
)
tnPktWanifStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsAttributeTotal.setStatus("current")
_TnPktWanifStatsTable_Object = MibTable
tnPktWanifStatsTable = _TnPktWanifStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22)
)
if mibBuilder.loadTexts:
    tnPktWanifStatsTable.setStatus("current")
_TnPktWanifStatsEntry_Object = MibTableRow
tnPktWanifStatsEntry = _TnPktWanifStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1)
)
tnPktWanifStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnPktWanifStatsPortId"),
    (0, "TN-PMON-MIB", "tnPktWanifStatsInterval"),
    (0, "TN-PMON-MIB", "tnPktWanifStatsBin"),
)
if mibBuilder.loadTexts:
    tnPktWanifStatsEntry.setStatus("current")
_TnPktWanifStatsPortId_Type = TmnxPortID
_TnPktWanifStatsPortId_Object = MibTableColumn
tnPktWanifStatsPortId = _TnPktWanifStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 1),
    _TnPktWanifStatsPortId_Type()
)
tnPktWanifStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPktWanifStatsPortId.setStatus("current")
_TnPktWanifStatsInterval_Type = AluWdmStatsIntervalType
_TnPktWanifStatsInterval_Object = MibTableColumn
tnPktWanifStatsInterval = _TnPktWanifStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 2),
    _TnPktWanifStatsInterval_Type()
)
tnPktWanifStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPktWanifStatsInterval.setStatus("current")
_TnPktWanifStatsBin_Type = AluWdmStatsBinNumber
_TnPktWanifStatsBin_Object = MibTableColumn
tnPktWanifStatsBin = _TnPktWanifStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 3),
    _TnPktWanifStatsBin_Type()
)
tnPktWanifStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPktWanifStatsBin.setStatus("current")
_TnPktWanifStatsBinStatus_Type = AluWdmStatsBinStatus
_TnPktWanifStatsBinStatus_Object = MibTableColumn
tnPktWanifStatsBinStatus = _TnPktWanifStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 4),
    _TnPktWanifStatsBinStatus_Type()
)
tnPktWanifStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsBinStatus.setStatus("current")
_TnPktWanifStatsStartTime_Type = DateAndTime
_TnPktWanifStatsStartTime_Object = MibTableColumn
tnPktWanifStatsStartTime = _TnPktWanifStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 5),
    _TnPktWanifStatsStartTime_Type()
)
tnPktWanifStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsStartTime.setStatus("current")
_TnPktWanifStatsInPackets_Type = Counter64
_TnPktWanifStatsInPackets_Object = MibTableColumn
tnPktWanifStatsInPackets = _TnPktWanifStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 6),
    _TnPktWanifStatsInPackets_Type()
)
tnPktWanifStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInPackets.setStatus("current")
_TnPktWanifStatsInOctets_Type = Counter64
_TnPktWanifStatsInOctets_Object = MibTableColumn
tnPktWanifStatsInOctets = _TnPktWanifStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 7),
    _TnPktWanifStatsInOctets_Type()
)
tnPktWanifStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInOctets.setStatus("current")
_TnPktWanifStatsInUcastPkts_Type = Counter64
_TnPktWanifStatsInUcastPkts_Object = MibTableColumn
tnPktWanifStatsInUcastPkts = _TnPktWanifStatsInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 8),
    _TnPktWanifStatsInUcastPkts_Type()
)
tnPktWanifStatsInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInUcastPkts.setStatus("current")
_TnPktWanifStatsInDiscards_Type = Counter64
_TnPktWanifStatsInDiscards_Object = MibTableColumn
tnPktWanifStatsInDiscards = _TnPktWanifStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 9),
    _TnPktWanifStatsInDiscards_Type()
)
tnPktWanifStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInDiscards.setStatus("current")
_TnPktWanifStatsInErrors_Type = Counter64
_TnPktWanifStatsInErrors_Object = MibTableColumn
tnPktWanifStatsInErrors = _TnPktWanifStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 10),
    _TnPktWanifStatsInErrors_Type()
)
tnPktWanifStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInErrors.setStatus("current")
_TnPktWanifStatsInUnknownProtos_Type = Counter64
_TnPktWanifStatsInUnknownProtos_Object = MibTableColumn
tnPktWanifStatsInUnknownProtos = _TnPktWanifStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 11),
    _TnPktWanifStatsInUnknownProtos_Type()
)
tnPktWanifStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInUnknownProtos.setStatus("current")
_TnPktWanifStatsInMulticastPkts_Type = Counter64
_TnPktWanifStatsInMulticastPkts_Object = MibTableColumn
tnPktWanifStatsInMulticastPkts = _TnPktWanifStatsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 12),
    _TnPktWanifStatsInMulticastPkts_Type()
)
tnPktWanifStatsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInMulticastPkts.setStatus("current")
_TnPktWanifStatsInBroadcastPkts_Type = Counter64
_TnPktWanifStatsInBroadcastPkts_Object = MibTableColumn
tnPktWanifStatsInBroadcastPkts = _TnPktWanifStatsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 13),
    _TnPktWanifStatsInBroadcastPkts_Type()
)
tnPktWanifStatsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsInBroadcastPkts.setStatus("current")
_TnPktWanifStatsOutPackets_Type = Counter64
_TnPktWanifStatsOutPackets_Object = MibTableColumn
tnPktWanifStatsOutPackets = _TnPktWanifStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 14),
    _TnPktWanifStatsOutPackets_Type()
)
tnPktWanifStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOutPackets.setStatus("current")
_TnPktWanifStatsOutOctets_Type = Counter64
_TnPktWanifStatsOutOctets_Object = MibTableColumn
tnPktWanifStatsOutOctets = _TnPktWanifStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 15),
    _TnPktWanifStatsOutOctets_Type()
)
tnPktWanifStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOutOctets.setStatus("current")
_TnPktWanifStatsOutUcastPkts_Type = Counter64
_TnPktWanifStatsOutUcastPkts_Object = MibTableColumn
tnPktWanifStatsOutUcastPkts = _TnPktWanifStatsOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 16),
    _TnPktWanifStatsOutUcastPkts_Type()
)
tnPktWanifStatsOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOutUcastPkts.setStatus("current")
_TnPktWanifStatsOutDiscards_Type = Counter64
_TnPktWanifStatsOutDiscards_Object = MibTableColumn
tnPktWanifStatsOutDiscards = _TnPktWanifStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 17),
    _TnPktWanifStatsOutDiscards_Type()
)
tnPktWanifStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOutDiscards.setStatus("current")
_TnPktWanifStatsOutErrors_Type = Counter64
_TnPktWanifStatsOutErrors_Object = MibTableColumn
tnPktWanifStatsOutErrors = _TnPktWanifStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 18),
    _TnPktWanifStatsOutErrors_Type()
)
tnPktWanifStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOutErrors.setStatus("current")
_TnPktWanifStatsOutMulticastPkts_Type = Counter64
_TnPktWanifStatsOutMulticastPkts_Object = MibTableColumn
tnPktWanifStatsOutMulticastPkts = _TnPktWanifStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 19),
    _TnPktWanifStatsOutMulticastPkts_Type()
)
tnPktWanifStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOutMulticastPkts.setStatus("current")
_TnPktWanifStatsOutBroadcastPkts_Type = Counter64
_TnPktWanifStatsOutBroadcastPkts_Object = MibTableColumn
tnPktWanifStatsOutBroadcastPkts = _TnPktWanifStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 20),
    _TnPktWanifStatsOutBroadcastPkts_Type()
)
tnPktWanifStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOutBroadcastPkts.setStatus("current")
_TnPktWanifStatsDropEvents_Type = Counter64
_TnPktWanifStatsDropEvents_Object = MibTableColumn
tnPktWanifStatsDropEvents = _TnPktWanifStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 21),
    _TnPktWanifStatsDropEvents_Type()
)
tnPktWanifStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsDropEvents.setStatus("current")
_TnPktWanifStatsBroadcastPkts_Type = Counter64
_TnPktWanifStatsBroadcastPkts_Object = MibTableColumn
tnPktWanifStatsBroadcastPkts = _TnPktWanifStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 22),
    _TnPktWanifStatsBroadcastPkts_Type()
)
tnPktWanifStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsBroadcastPkts.setStatus("current")
_TnPktWanifStatsMulticastPkts_Type = Counter64
_TnPktWanifStatsMulticastPkts_Object = MibTableColumn
tnPktWanifStatsMulticastPkts = _TnPktWanifStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 23),
    _TnPktWanifStatsMulticastPkts_Type()
)
tnPktWanifStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsMulticastPkts.setStatus("current")
_TnPktWanifStatsCRCAlignErrors_Type = Counter64
_TnPktWanifStatsCRCAlignErrors_Object = MibTableColumn
tnPktWanifStatsCRCAlignErrors = _TnPktWanifStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 24),
    _TnPktWanifStatsCRCAlignErrors_Type()
)
tnPktWanifStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsCRCAlignErrors.setStatus("current")
_TnPktWanifStatsUndersizePkts_Type = Counter64
_TnPktWanifStatsUndersizePkts_Object = MibTableColumn
tnPktWanifStatsUndersizePkts = _TnPktWanifStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 25),
    _TnPktWanifStatsUndersizePkts_Type()
)
tnPktWanifStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsUndersizePkts.setStatus("current")
_TnPktWanifStatsOversizePkts_Type = Counter64
_TnPktWanifStatsOversizePkts_Object = MibTableColumn
tnPktWanifStatsOversizePkts = _TnPktWanifStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 26),
    _TnPktWanifStatsOversizePkts_Type()
)
tnPktWanifStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsOversizePkts.setStatus("current")
_TnPktWanifStatsFragments_Type = Counter64
_TnPktWanifStatsFragments_Object = MibTableColumn
tnPktWanifStatsFragments = _TnPktWanifStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 27),
    _TnPktWanifStatsFragments_Type()
)
tnPktWanifStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsFragments.setStatus("current")
_TnPktWanifStatsJabbers_Type = Counter64
_TnPktWanifStatsJabbers_Object = MibTableColumn
tnPktWanifStatsJabbers = _TnPktWanifStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 28),
    _TnPktWanifStatsJabbers_Type()
)
tnPktWanifStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsJabbers.setStatus("current")
_TnPktWanifStatsCollisions_Type = Counter64
_TnPktWanifStatsCollisions_Object = MibTableColumn
tnPktWanifStatsCollisions = _TnPktWanifStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 29),
    _TnPktWanifStatsCollisions_Type()
)
tnPktWanifStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsCollisions.setStatus("current")
_TnPktWanifStatsHighCapacityPkts_Type = Counter64
_TnPktWanifStatsHighCapacityPkts_Object = MibTableColumn
tnPktWanifStatsHighCapacityPkts = _TnPktWanifStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 30),
    _TnPktWanifStatsHighCapacityPkts_Type()
)
tnPktWanifStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPkts.setStatus("current")
_TnPktWanifStatsHighCapacityOctets_Type = Counter64
_TnPktWanifStatsHighCapacityOctets_Object = MibTableColumn
tnPktWanifStatsHighCapacityOctets = _TnPktWanifStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 31),
    _TnPktWanifStatsHighCapacityOctets_Type()
)
tnPktWanifStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityOctets.setStatus("current")
_TnPktWanifStatsHighCapacityPktsSize64_Type = Counter64
_TnPktWanifStatsHighCapacityPktsSize64_Object = MibTableColumn
tnPktWanifStatsHighCapacityPktsSize64 = _TnPktWanifStatsHighCapacityPktsSize64_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 32),
    _TnPktWanifStatsHighCapacityPktsSize64_Type()
)
tnPktWanifStatsHighCapacityPktsSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPktsSize64.setStatus("current")
_TnPktWanifStatsHighCapacityPktsSize65to127_Type = Counter64
_TnPktWanifStatsHighCapacityPktsSize65to127_Object = MibTableColumn
tnPktWanifStatsHighCapacityPktsSize65to127 = _TnPktWanifStatsHighCapacityPktsSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 33),
    _TnPktWanifStatsHighCapacityPktsSize65to127_Type()
)
tnPktWanifStatsHighCapacityPktsSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPktsSize65to127.setStatus("current")
_TnPktWanifStatsHighCapacityPktsSize128to255_Type = Counter64
_TnPktWanifStatsHighCapacityPktsSize128to255_Object = MibTableColumn
tnPktWanifStatsHighCapacityPktsSize128to255 = _TnPktWanifStatsHighCapacityPktsSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 34),
    _TnPktWanifStatsHighCapacityPktsSize128to255_Type()
)
tnPktWanifStatsHighCapacityPktsSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPktsSize128to255.setStatus("current")
_TnPktWanifStatsHighCapacityPktsSize256to511_Type = Counter64
_TnPktWanifStatsHighCapacityPktsSize256to511_Object = MibTableColumn
tnPktWanifStatsHighCapacityPktsSize256to511 = _TnPktWanifStatsHighCapacityPktsSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 35),
    _TnPktWanifStatsHighCapacityPktsSize256to511_Type()
)
tnPktWanifStatsHighCapacityPktsSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPktsSize256to511.setStatus("current")
_TnPktWanifStatsHighCapacityPktsSize512to1023_Type = Counter64
_TnPktWanifStatsHighCapacityPktsSize512to1023_Object = MibTableColumn
tnPktWanifStatsHighCapacityPktsSize512to1023 = _TnPktWanifStatsHighCapacityPktsSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 36),
    _TnPktWanifStatsHighCapacityPktsSize512to1023_Type()
)
tnPktWanifStatsHighCapacityPktsSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPktsSize512to1023.setStatus("current")
_TnPktWanifStatsHighCapacityPktsSize1024to1518_Type = Counter64
_TnPktWanifStatsHighCapacityPktsSize1024to1518_Object = MibTableColumn
tnPktWanifStatsHighCapacityPktsSize1024to1518 = _TnPktWanifStatsHighCapacityPktsSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 37),
    _TnPktWanifStatsHighCapacityPktsSize1024to1518_Type()
)
tnPktWanifStatsHighCapacityPktsSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPktsSize1024to1518.setStatus("current")
_TnPktWanifStatsHighCapacityPktsSize1519toMax_Type = Counter64
_TnPktWanifStatsHighCapacityPktsSize1519toMax_Object = MibTableColumn
tnPktWanifStatsHighCapacityPktsSize1519toMax = _TnPktWanifStatsHighCapacityPktsSize1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 38),
    _TnPktWanifStatsHighCapacityPktsSize1519toMax_Type()
)
tnPktWanifStatsHighCapacityPktsSize1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsHighCapacityPktsSize1519toMax.setStatus("current")
_TnPktWanifStatsTooLongFrames_Type = Counter64
_TnPktWanifStatsTooLongFrames_Object = MibTableColumn
tnPktWanifStatsTooLongFrames = _TnPktWanifStatsTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 22, 1, 39),
    _TnPktWanifStatsTooLongFrames_Type()
)
tnPktWanifStatsTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifStatsTooLongFrames.setStatus("current")
_TnPktWanifRawCountStatsAttributeTotal_Type = Integer32
_TnPktWanifRawCountStatsAttributeTotal_Object = MibScalar
tnPktWanifRawCountStatsAttributeTotal = _TnPktWanifRawCountStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 23),
    _TnPktWanifRawCountStatsAttributeTotal_Type()
)
tnPktWanifRawCountStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsAttributeTotal.setStatus("current")
_TnPktWanifRawCountStatsTable_Object = MibTable
tnPktWanifRawCountStatsTable = _TnPktWanifRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24)
)
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsTable.setStatus("current")
_TnPktWanifRawCountStatsEntry_Object = MibTableRow
tnPktWanifRawCountStatsEntry = _TnPktWanifRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1)
)
tnPktWanifRawCountStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnPktWanifRawCountStatsPortId"),
)
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsEntry.setStatus("current")
_TnPktWanifRawCountStatsPortId_Type = TmnxPortID
_TnPktWanifRawCountStatsPortId_Object = MibTableColumn
tnPktWanifRawCountStatsPortId = _TnPktWanifRawCountStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 1),
    _TnPktWanifRawCountStatsPortId_Type()
)
tnPktWanifRawCountStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsPortId.setStatus("current")
_TnPktWanifRawCountStatsClear_Type = TnCommand
_TnPktWanifRawCountStatsClear_Object = MibTableColumn
tnPktWanifRawCountStatsClear = _TnPktWanifRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 2),
    _TnPktWanifRawCountStatsClear_Type()
)
tnPktWanifRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsClear.setStatus("current")
_TnPktWanifRawCountStatsStartTime_Type = DateAndTime
_TnPktWanifRawCountStatsStartTime_Object = MibTableColumn
tnPktWanifRawCountStatsStartTime = _TnPktWanifRawCountStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 3),
    _TnPktWanifRawCountStatsStartTime_Type()
)
tnPktWanifRawCountStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsStartTime.setStatus("current")
_TnPktWanifRawCountStatsInPackets_Type = Counter64
_TnPktWanifRawCountStatsInPackets_Object = MibTableColumn
tnPktWanifRawCountStatsInPackets = _TnPktWanifRawCountStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 4),
    _TnPktWanifRawCountStatsInPackets_Type()
)
tnPktWanifRawCountStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInPackets.setStatus("current")
_TnPktWanifRawCountStatsInOctets_Type = Counter64
_TnPktWanifRawCountStatsInOctets_Object = MibTableColumn
tnPktWanifRawCountStatsInOctets = _TnPktWanifRawCountStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 5),
    _TnPktWanifRawCountStatsInOctets_Type()
)
tnPktWanifRawCountStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInOctets.setStatus("current")
_TnPktWanifRawCountStatsInUcastPkts_Type = Counter64
_TnPktWanifRawCountStatsInUcastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsInUcastPkts = _TnPktWanifRawCountStatsInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 6),
    _TnPktWanifRawCountStatsInUcastPkts_Type()
)
tnPktWanifRawCountStatsInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInUcastPkts.setStatus("current")
_TnPktWanifRawCountStatsInDiscards_Type = Counter64
_TnPktWanifRawCountStatsInDiscards_Object = MibTableColumn
tnPktWanifRawCountStatsInDiscards = _TnPktWanifRawCountStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 7),
    _TnPktWanifRawCountStatsInDiscards_Type()
)
tnPktWanifRawCountStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInDiscards.setStatus("current")
_TnPktWanifRawCountStatsInErrors_Type = Counter64
_TnPktWanifRawCountStatsInErrors_Object = MibTableColumn
tnPktWanifRawCountStatsInErrors = _TnPktWanifRawCountStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 8),
    _TnPktWanifRawCountStatsInErrors_Type()
)
tnPktWanifRawCountStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInErrors.setStatus("current")
_TnPktWanifRawCountStatsInUnknownProtos_Type = Counter64
_TnPktWanifRawCountStatsInUnknownProtos_Object = MibTableColumn
tnPktWanifRawCountStatsInUnknownProtos = _TnPktWanifRawCountStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 9),
    _TnPktWanifRawCountStatsInUnknownProtos_Type()
)
tnPktWanifRawCountStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInUnknownProtos.setStatus("current")
_TnPktWanifRawCountStatsInMulticastPkts_Type = Counter64
_TnPktWanifRawCountStatsInMulticastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsInMulticastPkts = _TnPktWanifRawCountStatsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 10),
    _TnPktWanifRawCountStatsInMulticastPkts_Type()
)
tnPktWanifRawCountStatsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInMulticastPkts.setStatus("current")
_TnPktWanifRawCountStatsInBroadcastPkts_Type = Counter64
_TnPktWanifRawCountStatsInBroadcastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsInBroadcastPkts = _TnPktWanifRawCountStatsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 11),
    _TnPktWanifRawCountStatsInBroadcastPkts_Type()
)
tnPktWanifRawCountStatsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsInBroadcastPkts.setStatus("current")
_TnPktWanifRawCountStatsOutPackets_Type = Counter64
_TnPktWanifRawCountStatsOutPackets_Object = MibTableColumn
tnPktWanifRawCountStatsOutPackets = _TnPktWanifRawCountStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 12),
    _TnPktWanifRawCountStatsOutPackets_Type()
)
tnPktWanifRawCountStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOutPackets.setStatus("current")
_TnPktWanifRawCountStatsOutOctets_Type = Counter64
_TnPktWanifRawCountStatsOutOctets_Object = MibTableColumn
tnPktWanifRawCountStatsOutOctets = _TnPktWanifRawCountStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 13),
    _TnPktWanifRawCountStatsOutOctets_Type()
)
tnPktWanifRawCountStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOutOctets.setStatus("current")
_TnPktWanifRawCountStatsOutUcastPkts_Type = Counter64
_TnPktWanifRawCountStatsOutUcastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsOutUcastPkts = _TnPktWanifRawCountStatsOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 14),
    _TnPktWanifRawCountStatsOutUcastPkts_Type()
)
tnPktWanifRawCountStatsOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOutUcastPkts.setStatus("current")
_TnPktWanifRawCountStatsOutDiscards_Type = Counter64
_TnPktWanifRawCountStatsOutDiscards_Object = MibTableColumn
tnPktWanifRawCountStatsOutDiscards = _TnPktWanifRawCountStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 15),
    _TnPktWanifRawCountStatsOutDiscards_Type()
)
tnPktWanifRawCountStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOutDiscards.setStatus("current")
_TnPktWanifRawCountStatsOutErrors_Type = Counter64
_TnPktWanifRawCountStatsOutErrors_Object = MibTableColumn
tnPktWanifRawCountStatsOutErrors = _TnPktWanifRawCountStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 16),
    _TnPktWanifRawCountStatsOutErrors_Type()
)
tnPktWanifRawCountStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOutErrors.setStatus("current")
_TnPktWanifRawCountStatsOutMulticastPkts_Type = Counter64
_TnPktWanifRawCountStatsOutMulticastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsOutMulticastPkts = _TnPktWanifRawCountStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 17),
    _TnPktWanifRawCountStatsOutMulticastPkts_Type()
)
tnPktWanifRawCountStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOutMulticastPkts.setStatus("current")
_TnPktWanifRawCountStatsOutBroadcastPkts_Type = Counter64
_TnPktWanifRawCountStatsOutBroadcastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsOutBroadcastPkts = _TnPktWanifRawCountStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 18),
    _TnPktWanifRawCountStatsOutBroadcastPkts_Type()
)
tnPktWanifRawCountStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOutBroadcastPkts.setStatus("current")
_TnPktWanifRawCountStatsDropEvents_Type = Counter64
_TnPktWanifRawCountStatsDropEvents_Object = MibTableColumn
tnPktWanifRawCountStatsDropEvents = _TnPktWanifRawCountStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 19),
    _TnPktWanifRawCountStatsDropEvents_Type()
)
tnPktWanifRawCountStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsDropEvents.setStatus("current")
_TnPktWanifRawCountStatsBroadcastPkts_Type = Counter64
_TnPktWanifRawCountStatsBroadcastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsBroadcastPkts = _TnPktWanifRawCountStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 20),
    _TnPktWanifRawCountStatsBroadcastPkts_Type()
)
tnPktWanifRawCountStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsBroadcastPkts.setStatus("current")
_TnPktWanifRawCountStatsMulticastPkts_Type = Counter64
_TnPktWanifRawCountStatsMulticastPkts_Object = MibTableColumn
tnPktWanifRawCountStatsMulticastPkts = _TnPktWanifRawCountStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 21),
    _TnPktWanifRawCountStatsMulticastPkts_Type()
)
tnPktWanifRawCountStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsMulticastPkts.setStatus("current")
_TnPktWanifRawCountStatsCRCAlignErrors_Type = Counter64
_TnPktWanifRawCountStatsCRCAlignErrors_Object = MibTableColumn
tnPktWanifRawCountStatsCRCAlignErrors = _TnPktWanifRawCountStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 22),
    _TnPktWanifRawCountStatsCRCAlignErrors_Type()
)
tnPktWanifRawCountStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsCRCAlignErrors.setStatus("current")
_TnPktWanifRawCountStatsUndersizePkts_Type = Counter64
_TnPktWanifRawCountStatsUndersizePkts_Object = MibTableColumn
tnPktWanifRawCountStatsUndersizePkts = _TnPktWanifRawCountStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 23),
    _TnPktWanifRawCountStatsUndersizePkts_Type()
)
tnPktWanifRawCountStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsUndersizePkts.setStatus("current")
_TnPktWanifRawCountStatsOversizePkts_Type = Counter64
_TnPktWanifRawCountStatsOversizePkts_Object = MibTableColumn
tnPktWanifRawCountStatsOversizePkts = _TnPktWanifRawCountStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 24),
    _TnPktWanifRawCountStatsOversizePkts_Type()
)
tnPktWanifRawCountStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsOversizePkts.setStatus("current")
_TnPktWanifRawCountStatsFragments_Type = Counter64
_TnPktWanifRawCountStatsFragments_Object = MibTableColumn
tnPktWanifRawCountStatsFragments = _TnPktWanifRawCountStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 25),
    _TnPktWanifRawCountStatsFragments_Type()
)
tnPktWanifRawCountStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsFragments.setStatus("current")
_TnPktWanifRawCountStatsJabbers_Type = Counter64
_TnPktWanifRawCountStatsJabbers_Object = MibTableColumn
tnPktWanifRawCountStatsJabbers = _TnPktWanifRawCountStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 26),
    _TnPktWanifRawCountStatsJabbers_Type()
)
tnPktWanifRawCountStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsJabbers.setStatus("current")
_TnPktWanifRawCountStatsCollisions_Type = Counter64
_TnPktWanifRawCountStatsCollisions_Object = MibTableColumn
tnPktWanifRawCountStatsCollisions = _TnPktWanifRawCountStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 27),
    _TnPktWanifRawCountStatsCollisions_Type()
)
tnPktWanifRawCountStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsCollisions.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPkts_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPkts_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPkts = _TnPktWanifRawCountStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 28),
    _TnPktWanifRawCountStatsHighCapacityPkts_Type()
)
tnPktWanifRawCountStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPkts.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityOctets_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityOctets_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityOctets = _TnPktWanifRawCountStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 29),
    _TnPktWanifRawCountStatsHighCapacityOctets_Type()
)
tnPktWanifRawCountStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityOctets.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPktsSize64_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize64_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize64 = _TnPktWanifRawCountStatsHighCapacityPktsSize64_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 30),
    _TnPktWanifRawCountStatsHighCapacityPktsSize64_Type()
)
tnPktWanifRawCountStatsHighCapacityPktsSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPktsSize64.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize65to127 = _TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 31),
    _TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Type()
)
tnPktWanifRawCountStatsHighCapacityPktsSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPktsSize65to127.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize128to255 = _TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 32),
    _TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Type()
)
tnPktWanifRawCountStatsHighCapacityPktsSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPktsSize128to255.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize256to511 = _TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 33),
    _TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Type()
)
tnPktWanifRawCountStatsHighCapacityPktsSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPktsSize256to511.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize512to1023 = _TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 34),
    _TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Type()
)
tnPktWanifRawCountStatsHighCapacityPktsSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPktsSize512to1023.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518 = _TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 35),
    _TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Type()
)
tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518.setStatus("current")
_TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Type = Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Object = MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax = _TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 36),
    _TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Type()
)
tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax.setStatus("current")
_TnPktWanifRawCountStatsTooLongFrames_Type = Counter64
_TnPktWanifRawCountStatsTooLongFrames_Object = MibTableColumn
tnPktWanifRawCountStatsTooLongFrames = _TnPktWanifRawCountStatsTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 24, 1, 37),
    _TnPktWanifRawCountStatsTooLongFrames_Type()
)
tnPktWanifRawCountStatsTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPktWanifRawCountStatsTooLongFrames.setStatus("current")
_TnRoeStatsAttributeTotal_Type = Integer32
_TnRoeStatsAttributeTotal_Object = MibScalar
tnRoeStatsAttributeTotal = _TnRoeStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 25),
    _TnRoeStatsAttributeTotal_Type()
)
tnRoeStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeStatsAttributeTotal.setStatus("current")
_TnRoeStatsTable_Object = MibTable
tnRoeStatsTable = _TnRoeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26)
)
if mibBuilder.loadTexts:
    tnRoeStatsTable.setStatus("current")
_TnRoeStatsEntry_Object = MibTableRow
tnRoeStatsEntry = _TnRoeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1)
)
tnRoeStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnRoeStatsPortId"),
    (0, "TN-PMON-MIB", "tnRoeStatsInterval"),
    (0, "TN-PMON-MIB", "tnRoeStatsBin"),
)
if mibBuilder.loadTexts:
    tnRoeStatsEntry.setStatus("current")
_TnRoeStatsPortId_Type = TmnxPortID
_TnRoeStatsPortId_Object = MibTableColumn
tnRoeStatsPortId = _TnRoeStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 1),
    _TnRoeStatsPortId_Type()
)
tnRoeStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeStatsPortId.setStatus("current")
_TnRoeStatsInterval_Type = AluWdmStatsIntervalType
_TnRoeStatsInterval_Object = MibTableColumn
tnRoeStatsInterval = _TnRoeStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 2),
    _TnRoeStatsInterval_Type()
)
tnRoeStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeStatsInterval.setStatus("current")
_TnRoeStatsBin_Type = AluWdmStatsBinNumber
_TnRoeStatsBin_Object = MibTableColumn
tnRoeStatsBin = _TnRoeStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 3),
    _TnRoeStatsBin_Type()
)
tnRoeStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeStatsBin.setStatus("current")
_TnRoeStatsBinStatus_Type = AluWdmStatsBinStatus
_TnRoeStatsBinStatus_Object = MibTableColumn
tnRoeStatsBinStatus = _TnRoeStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 4),
    _TnRoeStatsBinStatus_Type()
)
tnRoeStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeStatsBinStatus.setStatus("current")
_TnRoeStatsStartTime_Type = DateAndTime
_TnRoeStatsStartTime_Object = MibTableColumn
tnRoeStatsStartTime = _TnRoeStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 5),
    _TnRoeStatsStartTime_Type()
)
tnRoeStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeStatsStartTime.setStatus("current")
_TnRoeStatsTotalMembers_Type = Integer32
_TnRoeStatsTotalMembers_Object = MibTableColumn
tnRoeStatsTotalMembers = _TnRoeStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 6),
    _TnRoeStatsTotalMembers_Type()
)
tnRoeStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeStatsTotalMembers.setStatus("current")
_TnRoeStatsDecapPktsDropped_Type = Counter64
_TnRoeStatsDecapPktsDropped_Object = MibTableColumn
tnRoeStatsDecapPktsDropped = _TnRoeStatsDecapPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 8),
    _TnRoeStatsDecapPktsDropped_Type()
)
tnRoeStatsDecapPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeStatsDecapPktsDropped.setStatus("current")
_TnRoeStatsDecapPktMiss_Type = Counter64
_TnRoeStatsDecapPktMiss_Object = MibTableColumn
tnRoeStatsDecapPktMiss = _TnRoeStatsDecapPktMiss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 26, 1, 9),
    _TnRoeStatsDecapPktMiss_Type()
)
tnRoeStatsDecapPktMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeStatsDecapPktMiss.setStatus("current")
_TnRoeMapperStatsAttributeTotal_Type = Integer32
_TnRoeMapperStatsAttributeTotal_Object = MibScalar
tnRoeMapperStatsAttributeTotal = _TnRoeMapperStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 27),
    _TnRoeMapperStatsAttributeTotal_Type()
)
tnRoeMapperStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsAttributeTotal.setStatus("current")
_TnRoeMapperStatsTable_Object = MibTable
tnRoeMapperStatsTable = _TnRoeMapperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28)
)
if mibBuilder.loadTexts:
    tnRoeMapperStatsTable.setStatus("current")
_TnRoeMapperStatsEntry_Object = MibTableRow
tnRoeMapperStatsEntry = _TnRoeMapperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1)
)
tnRoeMapperStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnRoeMapperStatsPortId"),
    (0, "TN-PMON-MIB", "tnRoeMapperStatsMapperID"),
    (0, "TN-PMON-MIB", "tnRoeMapperStatsInterval"),
    (0, "TN-PMON-MIB", "tnRoeMapperStatsBin"),
)
if mibBuilder.loadTexts:
    tnRoeMapperStatsEntry.setStatus("current")
_TnRoeMapperStatsPortId_Type = TmnxPortID
_TnRoeMapperStatsPortId_Object = MibTableColumn
tnRoeMapperStatsPortId = _TnRoeMapperStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 1),
    _TnRoeMapperStatsPortId_Type()
)
tnRoeMapperStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperStatsPortId.setStatus("current")


class _TnRoeMapperStatsMapperID_Type(Integer32):
    """Custom type tnRoeMapperStatsMapperID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeMapperStatsMapperID_Type.__name__ = "Integer32"
_TnRoeMapperStatsMapperID_Object = MibTableColumn
tnRoeMapperStatsMapperID = _TnRoeMapperStatsMapperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 2),
    _TnRoeMapperStatsMapperID_Type()
)
tnRoeMapperStatsMapperID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperStatsMapperID.setStatus("current")
_TnRoeMapperStatsInterval_Type = AluWdmStatsIntervalType
_TnRoeMapperStatsInterval_Object = MibTableColumn
tnRoeMapperStatsInterval = _TnRoeMapperStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 3),
    _TnRoeMapperStatsInterval_Type()
)
tnRoeMapperStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperStatsInterval.setStatus("current")
_TnRoeMapperStatsBin_Type = AluWdmStatsBinNumber
_TnRoeMapperStatsBin_Object = MibTableColumn
tnRoeMapperStatsBin = _TnRoeMapperStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 4),
    _TnRoeMapperStatsBin_Type()
)
tnRoeMapperStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperStatsBin.setStatus("current")
_TnRoeMapperStatsBinStatus_Type = AluWdmStatsBinStatus
_TnRoeMapperStatsBinStatus_Object = MibTableColumn
tnRoeMapperStatsBinStatus = _TnRoeMapperStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 5),
    _TnRoeMapperStatsBinStatus_Type()
)
tnRoeMapperStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsBinStatus.setStatus("current")
_TnRoeMapperStatsStartTime_Type = DateAndTime
_TnRoeMapperStatsStartTime_Object = MibTableColumn
tnRoeMapperStatsStartTime = _TnRoeMapperStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 6),
    _TnRoeMapperStatsStartTime_Type()
)
tnRoeMapperStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsStartTime.setStatus("current")
_TnRoeMapperStatsTotalMembers_Type = Integer32
_TnRoeMapperStatsTotalMembers_Object = MibTableColumn
tnRoeMapperStatsTotalMembers = _TnRoeMapperStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 7),
    _TnRoeMapperStatsTotalMembers_Type()
)
tnRoeMapperStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsTotalMembers.setStatus("current")
_TnRoeMapperStatsTxpackets_Type = Counter64
_TnRoeMapperStatsTxpackets_Object = MibTableColumn
tnRoeMapperStatsTxpackets = _TnRoeMapperStatsTxpackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 13),
    _TnRoeMapperStatsTxpackets_Type()
)
tnRoeMapperStatsTxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsTxpackets.setStatus("current")
_TnRoeMapperStatsTxbytes_Type = Counter64
_TnRoeMapperStatsTxbytes_Object = MibTableColumn
tnRoeMapperStatsTxbytes = _TnRoeMapperStatsTxbytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 14),
    _TnRoeMapperStatsTxbytes_Type()
)
tnRoeMapperStatsTxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsTxbytes.setStatus("current")
_TnRoeMapperStatsTxDropPackets_Type = Counter64
_TnRoeMapperStatsTxDropPackets_Object = MibTableColumn
tnRoeMapperStatsTxDropPackets = _TnRoeMapperStatsTxDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 15),
    _TnRoeMapperStatsTxDropPackets_Type()
)
tnRoeMapperStatsTxDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsTxDropPackets.setStatus("current")
_TnRoeMapperStatsEncapQueueOverrun_Type = Counter64
_TnRoeMapperStatsEncapQueueOverrun_Object = MibTableColumn
tnRoeMapperStatsEncapQueueOverrun = _TnRoeMapperStatsEncapQueueOverrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 16),
    _TnRoeMapperStatsEncapQueueOverrun_Type()
)
tnRoeMapperStatsEncapQueueOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsEncapQueueOverrun.setStatus("current")
_TnRoeMapperStatsGSMTimeSlotMismatch_Type = Counter64
_TnRoeMapperStatsGSMTimeSlotMismatch_Object = MibTableColumn
tnRoeMapperStatsGSMTimeSlotMismatch = _TnRoeMapperStatsGSMTimeSlotMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 28, 1, 17),
    _TnRoeMapperStatsGSMTimeSlotMismatch_Type()
)
tnRoeMapperStatsGSMTimeSlotMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperStatsGSMTimeSlotMismatch.setStatus("current")
_TnRoeDeMapperStatsAttributeTotal_Type = Integer32
_TnRoeDeMapperStatsAttributeTotal_Object = MibScalar
tnRoeDeMapperStatsAttributeTotal = _TnRoeDeMapperStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 29),
    _TnRoeDeMapperStatsAttributeTotal_Type()
)
tnRoeDeMapperStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsAttributeTotal.setStatus("current")
_TnRoeDeMapperStatsTable_Object = MibTable
tnRoeDeMapperStatsTable = _TnRoeDeMapperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30)
)
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsTable.setStatus("current")
_TnRoeDeMapperStatsEntry_Object = MibTableRow
tnRoeDeMapperStatsEntry = _TnRoeDeMapperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1)
)
tnRoeDeMapperStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnRoeDeMapperStatsPortId"),
    (0, "TN-PMON-MIB", "tnRoeDeMapperStatsDeMapperID"),
    (0, "TN-PMON-MIB", "tnRoeDeMapperStatsInterval"),
    (0, "TN-PMON-MIB", "tnRoeDeMapperStatsBin"),
)
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsEntry.setStatus("current")
_TnRoeDeMapperStatsPortId_Type = TmnxPortID
_TnRoeDeMapperStatsPortId_Object = MibTableColumn
tnRoeDeMapperStatsPortId = _TnRoeDeMapperStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 1),
    _TnRoeDeMapperStatsPortId_Type()
)
tnRoeDeMapperStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsPortId.setStatus("current")


class _TnRoeDeMapperStatsDeMapperID_Type(Integer32):
    """Custom type tnRoeDeMapperStatsDeMapperID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeDeMapperStatsDeMapperID_Type.__name__ = "Integer32"
_TnRoeDeMapperStatsDeMapperID_Object = MibTableColumn
tnRoeDeMapperStatsDeMapperID = _TnRoeDeMapperStatsDeMapperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 2),
    _TnRoeDeMapperStatsDeMapperID_Type()
)
tnRoeDeMapperStatsDeMapperID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsDeMapperID.setStatus("current")
_TnRoeDeMapperStatsInterval_Type = AluWdmStatsIntervalType
_TnRoeDeMapperStatsInterval_Object = MibTableColumn
tnRoeDeMapperStatsInterval = _TnRoeDeMapperStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 3),
    _TnRoeDeMapperStatsInterval_Type()
)
tnRoeDeMapperStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsInterval.setStatus("current")
_TnRoeDeMapperStatsBin_Type = AluWdmStatsBinNumber
_TnRoeDeMapperStatsBin_Object = MibTableColumn
tnRoeDeMapperStatsBin = _TnRoeDeMapperStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 4),
    _TnRoeDeMapperStatsBin_Type()
)
tnRoeDeMapperStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsBin.setStatus("current")
_TnRoeDeMapperStatsBinStatus_Type = AluWdmStatsBinStatus
_TnRoeDeMapperStatsBinStatus_Object = MibTableColumn
tnRoeDeMapperStatsBinStatus = _TnRoeDeMapperStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 5),
    _TnRoeDeMapperStatsBinStatus_Type()
)
tnRoeDeMapperStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsBinStatus.setStatus("current")
_TnRoeDeMapperStatsStartTime_Type = DateAndTime
_TnRoeDeMapperStatsStartTime_Object = MibTableColumn
tnRoeDeMapperStatsStartTime = _TnRoeDeMapperStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 6),
    _TnRoeDeMapperStatsStartTime_Type()
)
tnRoeDeMapperStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsStartTime.setStatus("current")
_TnRoeDeMapperStatsTotalMembers_Type = Integer32
_TnRoeDeMapperStatsTotalMembers_Object = MibTableColumn
tnRoeDeMapperStatsTotalMembers = _TnRoeDeMapperStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 7),
    _TnRoeDeMapperStatsTotalMembers_Type()
)
tnRoeDeMapperStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsTotalMembers.setStatus("current")
_TnRoeDeMapperStatsRxpackets_Type = Counter64
_TnRoeDeMapperStatsRxpackets_Object = MibTableColumn
tnRoeDeMapperStatsRxpackets = _TnRoeDeMapperStatsRxpackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 14),
    _TnRoeDeMapperStatsRxpackets_Type()
)
tnRoeDeMapperStatsRxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsRxpackets.setStatus("current")
_TnRoeDeMapperStatsRxbytes_Type = Counter64
_TnRoeDeMapperStatsRxbytes_Object = MibTableColumn
tnRoeDeMapperStatsRxbytes = _TnRoeDeMapperStatsRxbytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 15),
    _TnRoeDeMapperStatsRxbytes_Type()
)
tnRoeDeMapperStatsRxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsRxbytes.setStatus("current")
_TnRoeDeMapperStatsDecapQueueOverrun_Type = Counter64
_TnRoeDeMapperStatsDecapQueueOverrun_Object = MibTableColumn
tnRoeDeMapperStatsDecapQueueOverrun = _TnRoeDeMapperStatsDecapQueueOverrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 16),
    _TnRoeDeMapperStatsDecapQueueOverrun_Type()
)
tnRoeDeMapperStatsDecapQueueOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsDecapQueueOverrun.setStatus("current")
_TnRoeDeMapperStatsQueueUnderrun_Type = Counter64
_TnRoeDeMapperStatsQueueUnderrun_Object = MibTableColumn
tnRoeDeMapperStatsQueueUnderrun = _TnRoeDeMapperStatsQueueUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 17),
    _TnRoeDeMapperStatsQueueUnderrun_Type()
)
tnRoeDeMapperStatsQueueUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsQueueUnderrun.setStatus("current")
_TnRoeDeMapperStatsDecapPacketMissing_Type = Counter64
_TnRoeDeMapperStatsDecapPacketMissing_Object = MibTableColumn
tnRoeDeMapperStatsDecapPacketMissing = _TnRoeDeMapperStatsDecapPacketMissing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 18),
    _TnRoeDeMapperStatsDecapPacketMissing_Type()
)
tnRoeDeMapperStatsDecapPacketMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsDecapPacketMissing.setStatus("current")
_TnRoeDeMapperStatsDecapPacketSizeMismatch_Type = Counter64
_TnRoeDeMapperStatsDecapPacketSizeMismatch_Object = MibTableColumn
tnRoeDeMapperStatsDecapPacketSizeMismatch = _TnRoeDeMapperStatsDecapPacketSizeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 30, 1, 19),
    _TnRoeDeMapperStatsDecapPacketSizeMismatch_Type()
)
tnRoeDeMapperStatsDecapPacketSizeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperStatsDecapPacketSizeMismatch.setStatus("current")
_TnEMACStatsAttributeTotal_Type = Integer32
_TnEMACStatsAttributeTotal_Object = MibScalar
tnEMACStatsAttributeTotal = _TnEMACStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 31),
    _TnEMACStatsAttributeTotal_Type()
)
tnEMACStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsAttributeTotal.setStatus("current")
_TnEMACStatsTable_Object = MibTable
tnEMACStatsTable = _TnEMACStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32)
)
if mibBuilder.loadTexts:
    tnEMACStatsTable.setStatus("current")
_TnEMACStatsEntry_Object = MibTableRow
tnEMACStatsEntry = _TnEMACStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1)
)
tnEMACStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnEMACStatsPortId"),
    (0, "TN-PMON-MIB", "tnEMACStatsInterval"),
    (0, "TN-PMON-MIB", "tnEMACStatsBin"),
)
if mibBuilder.loadTexts:
    tnEMACStatsEntry.setStatus("current")
_TnEMACStatsPortId_Type = TmnxPortID
_TnEMACStatsPortId_Object = MibTableColumn
tnEMACStatsPortId = _TnEMACStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 1),
    _TnEMACStatsPortId_Type()
)
tnEMACStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEMACStatsPortId.setStatus("current")
_TnEMACStatsInterval_Type = AluWdmStatsIntervalType
_TnEMACStatsInterval_Object = MibTableColumn
tnEMACStatsInterval = _TnEMACStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 2),
    _TnEMACStatsInterval_Type()
)
tnEMACStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEMACStatsInterval.setStatus("current")
_TnEMACStatsBin_Type = AluWdmStatsBinNumber
_TnEMACStatsBin_Object = MibTableColumn
tnEMACStatsBin = _TnEMACStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 3),
    _TnEMACStatsBin_Type()
)
tnEMACStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEMACStatsBin.setStatus("current")
_TnEMACStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEMACStatsBinStatus_Object = MibTableColumn
tnEMACStatsBinStatus = _TnEMACStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 4),
    _TnEMACStatsBinStatus_Type()
)
tnEMACStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsBinStatus.setStatus("current")
_TnEMACStatsStartTime_Type = DateAndTime
_TnEMACStatsStartTime_Object = MibTableColumn
tnEMACStatsStartTime = _TnEMACStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 5),
    _TnEMACStatsStartTime_Type()
)
tnEMACStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsStartTime.setStatus("current")
_TnEMACStatsTotalMembers_Type = Integer32
_TnEMACStatsTotalMembers_Object = MibTableColumn
tnEMACStatsTotalMembers = _TnEMACStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 6),
    _TnEMACStatsTotalMembers_Type()
)
tnEMACStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsTotalMembers.setStatus("current")
_TnEMACStatsIfInOctets_Type = Counter64
_TnEMACStatsIfInOctets_Object = MibTableColumn
tnEMACStatsIfInOctets = _TnEMACStatsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 7),
    _TnEMACStatsIfInOctets_Type()
)
tnEMACStatsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInOctets.setStatus("current")
_TnEMACStatsIfInUcastPkts_Type = Counter64
_TnEMACStatsIfInUcastPkts_Object = MibTableColumn
tnEMACStatsIfInUcastPkts = _TnEMACStatsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 8),
    _TnEMACStatsIfInUcastPkts_Type()
)
tnEMACStatsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInUcastPkts.setStatus("current")
_TnEMACStatsIfInDiscards_Type = Counter64
_TnEMACStatsIfInDiscards_Object = MibTableColumn
tnEMACStatsIfInDiscards = _TnEMACStatsIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 9),
    _TnEMACStatsIfInDiscards_Type()
)
tnEMACStatsIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInDiscards.setStatus("current")
_TnEMACStatsIfInErrors_Type = Counter64
_TnEMACStatsIfInErrors_Object = MibTableColumn
tnEMACStatsIfInErrors = _TnEMACStatsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 10),
    _TnEMACStatsIfInErrors_Type()
)
tnEMACStatsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInErrors.setStatus("current")
_TnEMACStatsIfInUnknownProtos_Type = Counter64
_TnEMACStatsIfInUnknownProtos_Object = MibTableColumn
tnEMACStatsIfInUnknownProtos = _TnEMACStatsIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 11),
    _TnEMACStatsIfInUnknownProtos_Type()
)
tnEMACStatsIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInUnknownProtos.setStatus("current")
_TnEMACStatsIfInMulticastPkts_Type = Counter64
_TnEMACStatsIfInMulticastPkts_Object = MibTableColumn
tnEMACStatsIfInMulticastPkts = _TnEMACStatsIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 12),
    _TnEMACStatsIfInMulticastPkts_Type()
)
tnEMACStatsIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInMulticastPkts.setStatus("current")
_TnEMACStatsIfInBroadcastPkts_Type = Counter64
_TnEMACStatsIfInBroadcastPkts_Object = MibTableColumn
tnEMACStatsIfInBroadcastPkts = _TnEMACStatsIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 13),
    _TnEMACStatsIfInBroadcastPkts_Type()
)
tnEMACStatsIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInBroadcastPkts.setStatus("current")
_TnEMACStatsIfOutOctets_Type = Counter64
_TnEMACStatsIfOutOctets_Object = MibTableColumn
tnEMACStatsIfOutOctets = _TnEMACStatsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 14),
    _TnEMACStatsIfOutOctets_Type()
)
tnEMACStatsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfOutOctets.setStatus("current")
_TnEMACStatsIfOutUcastPkts_Type = Counter64
_TnEMACStatsIfOutUcastPkts_Object = MibTableColumn
tnEMACStatsIfOutUcastPkts = _TnEMACStatsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 15),
    _TnEMACStatsIfOutUcastPkts_Type()
)
tnEMACStatsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfOutUcastPkts.setStatus("current")
_TnEMACStatsIfOutDiscards_Type = Counter64
_TnEMACStatsIfOutDiscards_Object = MibTableColumn
tnEMACStatsIfOutDiscards = _TnEMACStatsIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 16),
    _TnEMACStatsIfOutDiscards_Type()
)
tnEMACStatsIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfOutDiscards.setStatus("current")
_TnEMACStatsIfOutErrors_Type = Counter64
_TnEMACStatsIfOutErrors_Object = MibTableColumn
tnEMACStatsIfOutErrors = _TnEMACStatsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 17),
    _TnEMACStatsIfOutErrors_Type()
)
tnEMACStatsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfOutErrors.setStatus("current")
_TnEMACStatsIfOutMulticastPkts_Type = Counter64
_TnEMACStatsIfOutMulticastPkts_Object = MibTableColumn
tnEMACStatsIfOutMulticastPkts = _TnEMACStatsIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 18),
    _TnEMACStatsIfOutMulticastPkts_Type()
)
tnEMACStatsIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfOutMulticastPkts.setStatus("current")
_TnEMACStatsIfOutBroadcastPkts_Type = Counter64
_TnEMACStatsIfOutBroadcastPkts_Object = MibTableColumn
tnEMACStatsIfOutBroadcastPkts = _TnEMACStatsIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 19),
    _TnEMACStatsIfOutBroadcastPkts_Type()
)
tnEMACStatsIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfOutBroadcastPkts.setStatus("current")
_TnEMACStatsIfInPkts_Type = Counter64
_TnEMACStatsIfInPkts_Object = MibTableColumn
tnEMACStatsIfInPkts = _TnEMACStatsIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 20),
    _TnEMACStatsIfInPkts_Type()
)
tnEMACStatsIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfInPkts.setStatus("current")
_TnEMACStatsIfOutPkts_Type = Counter64
_TnEMACStatsIfOutPkts_Object = MibTableColumn
tnEMACStatsIfOutPkts = _TnEMACStatsIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 21),
    _TnEMACStatsIfOutPkts_Type()
)
tnEMACStatsIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsIfOutPkts.setStatus("current")
_TnEMACStatsDropEvents_Type = Counter64
_TnEMACStatsDropEvents_Object = MibTableColumn
tnEMACStatsDropEvents = _TnEMACStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 22),
    _TnEMACStatsDropEvents_Type()
)
tnEMACStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsDropEvents.setStatus("current")
_TnEMACStatsBroadcastPkts_Type = Counter64
_TnEMACStatsBroadcastPkts_Object = MibTableColumn
tnEMACStatsBroadcastPkts = _TnEMACStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 23),
    _TnEMACStatsBroadcastPkts_Type()
)
tnEMACStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsBroadcastPkts.setStatus("current")
_TnEMACStatsMulticastPkts_Type = Counter64
_TnEMACStatsMulticastPkts_Object = MibTableColumn
tnEMACStatsMulticastPkts = _TnEMACStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 24),
    _TnEMACStatsMulticastPkts_Type()
)
tnEMACStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsMulticastPkts.setStatus("current")
_TnEMACStatsCRCAlignErrors_Type = Counter64
_TnEMACStatsCRCAlignErrors_Object = MibTableColumn
tnEMACStatsCRCAlignErrors = _TnEMACStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 25),
    _TnEMACStatsCRCAlignErrors_Type()
)
tnEMACStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsCRCAlignErrors.setStatus("current")
_TnEMACStatsUndersizePkts_Type = Counter64
_TnEMACStatsUndersizePkts_Object = MibTableColumn
tnEMACStatsUndersizePkts = _TnEMACStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 26),
    _TnEMACStatsUndersizePkts_Type()
)
tnEMACStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsUndersizePkts.setStatus("current")
_TnEMACStatsOversizePkts_Type = Counter64
_TnEMACStatsOversizePkts_Object = MibTableColumn
tnEMACStatsOversizePkts = _TnEMACStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 27),
    _TnEMACStatsOversizePkts_Type()
)
tnEMACStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsOversizePkts.setStatus("current")
_TnEMACStatsFragments_Type = Counter64
_TnEMACStatsFragments_Object = MibTableColumn
tnEMACStatsFragments = _TnEMACStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 28),
    _TnEMACStatsFragments_Type()
)
tnEMACStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsFragments.setStatus("current")
_TnEMACStatsJabbers_Type = Counter64
_TnEMACStatsJabbers_Object = MibTableColumn
tnEMACStatsJabbers = _TnEMACStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 29),
    _TnEMACStatsJabbers_Type()
)
tnEMACStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsJabbers.setStatus("current")
_TnEMACStatsCollisions_Type = Counter64
_TnEMACStatsCollisions_Object = MibTableColumn
tnEMACStatsCollisions = _TnEMACStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 30),
    _TnEMACStatsCollisions_Type()
)
tnEMACStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsCollisions.setStatus("current")
_TnEMACStatsHighCapacityPkts_Type = Counter64
_TnEMACStatsHighCapacityPkts_Object = MibTableColumn
tnEMACStatsHighCapacityPkts = _TnEMACStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 31),
    _TnEMACStatsHighCapacityPkts_Type()
)
tnEMACStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts.setStatus("current")
_TnEMACStatsHighCapacityOctets_Type = Counter64
_TnEMACStatsHighCapacityOctets_Object = MibTableColumn
tnEMACStatsHighCapacityOctets = _TnEMACStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 32),
    _TnEMACStatsHighCapacityOctets_Type()
)
tnEMACStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityOctets.setStatus("current")
_TnEMACStatsHighCapacityPkts64Octets_Type = Counter64
_TnEMACStatsHighCapacityPkts64Octets_Object = MibTableColumn
tnEMACStatsHighCapacityPkts64Octets = _TnEMACStatsHighCapacityPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 33),
    _TnEMACStatsHighCapacityPkts64Octets_Type()
)
tnEMACStatsHighCapacityPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts64Octets.setStatus("current")
_TnEMACStatsHighCapacityPkts65to127Octets_Type = Counter64
_TnEMACStatsHighCapacityPkts65to127Octets_Object = MibTableColumn
tnEMACStatsHighCapacityPkts65to127Octets = _TnEMACStatsHighCapacityPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 34),
    _TnEMACStatsHighCapacityPkts65to127Octets_Type()
)
tnEMACStatsHighCapacityPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts65to127Octets.setStatus("current")
_TnEMACStatsHighCapacityPkts128to255Octets_Type = Counter64
_TnEMACStatsHighCapacityPkts128to255Octets_Object = MibTableColumn
tnEMACStatsHighCapacityPkts128to255Octets = _TnEMACStatsHighCapacityPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 35),
    _TnEMACStatsHighCapacityPkts128to255Octets_Type()
)
tnEMACStatsHighCapacityPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts128to255Octets.setStatus("current")
_TnEMACStatsHighCapacityPkts256to511Octets_Type = Counter64
_TnEMACStatsHighCapacityPkts256to511Octets_Object = MibTableColumn
tnEMACStatsHighCapacityPkts256to511Octets = _TnEMACStatsHighCapacityPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 36),
    _TnEMACStatsHighCapacityPkts256to511Octets_Type()
)
tnEMACStatsHighCapacityPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts256to511Octets.setStatus("current")
_TnEMACStatsHighCapacityPkts512to1023Octets_Type = Counter64
_TnEMACStatsHighCapacityPkts512to1023Octets_Object = MibTableColumn
tnEMACStatsHighCapacityPkts512to1023Octets = _TnEMACStatsHighCapacityPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 37),
    _TnEMACStatsHighCapacityPkts512to1023Octets_Type()
)
tnEMACStatsHighCapacityPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts512to1023Octets.setStatus("current")
_TnEMACStatsHighCapacityPkts1024to1518Octets_Type = Counter64
_TnEMACStatsHighCapacityPkts1024to1518Octets_Object = MibTableColumn
tnEMACStatsHighCapacityPkts1024to1518Octets = _TnEMACStatsHighCapacityPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 38),
    _TnEMACStatsHighCapacityPkts1024to1518Octets_Type()
)
tnEMACStatsHighCapacityPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts1024to1518Octets.setStatus("current")
_TnEMACStatsHighCapacityPkts1519toMaxOctets_Type = Counter64
_TnEMACStatsHighCapacityPkts1519toMaxOctets_Object = MibTableColumn
tnEMACStatsHighCapacityPkts1519toMaxOctets = _TnEMACStatsHighCapacityPkts1519toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 32, 1, 39),
    _TnEMACStatsHighCapacityPkts1519toMaxOctets_Type()
)
tnEMACStatsHighCapacityPkts1519toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEMACStatsHighCapacityPkts1519toMaxOctets.setStatus("current")
_TnPMACStatsAttributeTotal_Type = Integer32
_TnPMACStatsAttributeTotal_Object = MibScalar
tnPMACStatsAttributeTotal = _TnPMACStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 33),
    _TnPMACStatsAttributeTotal_Type()
)
tnPMACStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsAttributeTotal.setStatus("current")
_TnPMACStatsTable_Object = MibTable
tnPMACStatsTable = _TnPMACStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34)
)
if mibBuilder.loadTexts:
    tnPMACStatsTable.setStatus("current")
_TnPMACStatsEntry_Object = MibTableRow
tnPMACStatsEntry = _TnPMACStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1)
)
tnPMACStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnPMACStatsPortId"),
    (0, "TN-PMON-MIB", "tnPMACStatsInterval"),
    (0, "TN-PMON-MIB", "tnPMACStatsBin"),
)
if mibBuilder.loadTexts:
    tnPMACStatsEntry.setStatus("current")
_TnPMACStatsPortId_Type = TmnxPortID
_TnPMACStatsPortId_Object = MibTableColumn
tnPMACStatsPortId = _TnPMACStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 1),
    _TnPMACStatsPortId_Type()
)
tnPMACStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPMACStatsPortId.setStatus("current")
_TnPMACStatsInterval_Type = AluWdmStatsIntervalType
_TnPMACStatsInterval_Object = MibTableColumn
tnPMACStatsInterval = _TnPMACStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 2),
    _TnPMACStatsInterval_Type()
)
tnPMACStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPMACStatsInterval.setStatus("current")
_TnPMACStatsBin_Type = AluWdmStatsBinNumber
_TnPMACStatsBin_Object = MibTableColumn
tnPMACStatsBin = _TnPMACStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 3),
    _TnPMACStatsBin_Type()
)
tnPMACStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPMACStatsBin.setStatus("current")
_TnPMACStatsBinStatus_Type = AluWdmStatsBinStatus
_TnPMACStatsBinStatus_Object = MibTableColumn
tnPMACStatsBinStatus = _TnPMACStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 4),
    _TnPMACStatsBinStatus_Type()
)
tnPMACStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsBinStatus.setStatus("current")
_TnPMACStatsStartTime_Type = DateAndTime
_TnPMACStatsStartTime_Object = MibTableColumn
tnPMACStatsStartTime = _TnPMACStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 5),
    _TnPMACStatsStartTime_Type()
)
tnPMACStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsStartTime.setStatus("current")
_TnPMACStatsTotalMembers_Type = Integer32
_TnPMACStatsTotalMembers_Object = MibTableColumn
tnPMACStatsTotalMembers = _TnPMACStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 6),
    _TnPMACStatsTotalMembers_Type()
)
tnPMACStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsTotalMembers.setStatus("current")
_TnPMACStatsIfInOctets_Type = Counter64
_TnPMACStatsIfInOctets_Object = MibTableColumn
tnPMACStatsIfInOctets = _TnPMACStatsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 7),
    _TnPMACStatsIfInOctets_Type()
)
tnPMACStatsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInOctets.setStatus("current")
_TnPMACStatsIfInUcastPkts_Type = Counter64
_TnPMACStatsIfInUcastPkts_Object = MibTableColumn
tnPMACStatsIfInUcastPkts = _TnPMACStatsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 8),
    _TnPMACStatsIfInUcastPkts_Type()
)
tnPMACStatsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInUcastPkts.setStatus("current")
_TnPMACStatsIfInDiscards_Type = Counter64
_TnPMACStatsIfInDiscards_Object = MibTableColumn
tnPMACStatsIfInDiscards = _TnPMACStatsIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 9),
    _TnPMACStatsIfInDiscards_Type()
)
tnPMACStatsIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInDiscards.setStatus("current")
_TnPMACStatsIfInErrors_Type = Counter64
_TnPMACStatsIfInErrors_Object = MibTableColumn
tnPMACStatsIfInErrors = _TnPMACStatsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 10),
    _TnPMACStatsIfInErrors_Type()
)
tnPMACStatsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInErrors.setStatus("current")
_TnPMACStatsIfInUnknownProtos_Type = Counter64
_TnPMACStatsIfInUnknownProtos_Object = MibTableColumn
tnPMACStatsIfInUnknownProtos = _TnPMACStatsIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 11),
    _TnPMACStatsIfInUnknownProtos_Type()
)
tnPMACStatsIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInUnknownProtos.setStatus("current")
_TnPMACStatsIfInMulticastPkts_Type = Counter64
_TnPMACStatsIfInMulticastPkts_Object = MibTableColumn
tnPMACStatsIfInMulticastPkts = _TnPMACStatsIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 12),
    _TnPMACStatsIfInMulticastPkts_Type()
)
tnPMACStatsIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInMulticastPkts.setStatus("current")
_TnPMACStatsIfInBroadcastPkts_Type = Counter64
_TnPMACStatsIfInBroadcastPkts_Object = MibTableColumn
tnPMACStatsIfInBroadcastPkts = _TnPMACStatsIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 13),
    _TnPMACStatsIfInBroadcastPkts_Type()
)
tnPMACStatsIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInBroadcastPkts.setStatus("current")
_TnPMACStatsIfOutOctets_Type = Counter64
_TnPMACStatsIfOutOctets_Object = MibTableColumn
tnPMACStatsIfOutOctets = _TnPMACStatsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 14),
    _TnPMACStatsIfOutOctets_Type()
)
tnPMACStatsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfOutOctets.setStatus("current")
_TnPMACStatsIfOutUcastPkts_Type = Counter64
_TnPMACStatsIfOutUcastPkts_Object = MibTableColumn
tnPMACStatsIfOutUcastPkts = _TnPMACStatsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 15),
    _TnPMACStatsIfOutUcastPkts_Type()
)
tnPMACStatsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfOutUcastPkts.setStatus("current")
_TnPMACStatsIfOutDiscards_Type = Counter64
_TnPMACStatsIfOutDiscards_Object = MibTableColumn
tnPMACStatsIfOutDiscards = _TnPMACStatsIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 16),
    _TnPMACStatsIfOutDiscards_Type()
)
tnPMACStatsIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfOutDiscards.setStatus("current")
_TnPMACStatsIfOutErrors_Type = Counter64
_TnPMACStatsIfOutErrors_Object = MibTableColumn
tnPMACStatsIfOutErrors = _TnPMACStatsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 17),
    _TnPMACStatsIfOutErrors_Type()
)
tnPMACStatsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfOutErrors.setStatus("current")
_TnPMACStatsIfOutMulticastPkts_Type = Counter64
_TnPMACStatsIfOutMulticastPkts_Object = MibTableColumn
tnPMACStatsIfOutMulticastPkts = _TnPMACStatsIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 18),
    _TnPMACStatsIfOutMulticastPkts_Type()
)
tnPMACStatsIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfOutMulticastPkts.setStatus("current")
_TnPMACStatsIfOutBroadcastPkts_Type = Counter64
_TnPMACStatsIfOutBroadcastPkts_Object = MibTableColumn
tnPMACStatsIfOutBroadcastPkts = _TnPMACStatsIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 19),
    _TnPMACStatsIfOutBroadcastPkts_Type()
)
tnPMACStatsIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfOutBroadcastPkts.setStatus("current")
_TnPMACStatsIfInPkts_Type = Counter64
_TnPMACStatsIfInPkts_Object = MibTableColumn
tnPMACStatsIfInPkts = _TnPMACStatsIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 20),
    _TnPMACStatsIfInPkts_Type()
)
tnPMACStatsIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfInPkts.setStatus("current")
_TnPMACStatsIfOutPkts_Type = Counter64
_TnPMACStatsIfOutPkts_Object = MibTableColumn
tnPMACStatsIfOutPkts = _TnPMACStatsIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 21),
    _TnPMACStatsIfOutPkts_Type()
)
tnPMACStatsIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsIfOutPkts.setStatus("current")
_TnPMACStatsDropEvents_Type = Counter64
_TnPMACStatsDropEvents_Object = MibTableColumn
tnPMACStatsDropEvents = _TnPMACStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 22),
    _TnPMACStatsDropEvents_Type()
)
tnPMACStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsDropEvents.setStatus("current")
_TnPMACStatsBroadcastPkts_Type = Counter64
_TnPMACStatsBroadcastPkts_Object = MibTableColumn
tnPMACStatsBroadcastPkts = _TnPMACStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 23),
    _TnPMACStatsBroadcastPkts_Type()
)
tnPMACStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsBroadcastPkts.setStatus("current")
_TnPMACStatsMulticastPkts_Type = Counter64
_TnPMACStatsMulticastPkts_Object = MibTableColumn
tnPMACStatsMulticastPkts = _TnPMACStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 24),
    _TnPMACStatsMulticastPkts_Type()
)
tnPMACStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsMulticastPkts.setStatus("current")
_TnPMACStatsCRCAlignErrors_Type = Counter64
_TnPMACStatsCRCAlignErrors_Object = MibTableColumn
tnPMACStatsCRCAlignErrors = _TnPMACStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 25),
    _TnPMACStatsCRCAlignErrors_Type()
)
tnPMACStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsCRCAlignErrors.setStatus("current")
_TnPMACStatsUndersizePkts_Type = Counter64
_TnPMACStatsUndersizePkts_Object = MibTableColumn
tnPMACStatsUndersizePkts = _TnPMACStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 26),
    _TnPMACStatsUndersizePkts_Type()
)
tnPMACStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsUndersizePkts.setStatus("current")
_TnPMACStatsOversizePkts_Type = Counter64
_TnPMACStatsOversizePkts_Object = MibTableColumn
tnPMACStatsOversizePkts = _TnPMACStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 27),
    _TnPMACStatsOversizePkts_Type()
)
tnPMACStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsOversizePkts.setStatus("current")
_TnPMACStatsFragments_Type = Counter64
_TnPMACStatsFragments_Object = MibTableColumn
tnPMACStatsFragments = _TnPMACStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 28),
    _TnPMACStatsFragments_Type()
)
tnPMACStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsFragments.setStatus("current")
_TnPMACStatsJabbers_Type = Counter64
_TnPMACStatsJabbers_Object = MibTableColumn
tnPMACStatsJabbers = _TnPMACStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 29),
    _TnPMACStatsJabbers_Type()
)
tnPMACStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsJabbers.setStatus("current")
_TnPMACStatsCollisions_Type = Counter64
_TnPMACStatsCollisions_Object = MibTableColumn
tnPMACStatsCollisions = _TnPMACStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 30),
    _TnPMACStatsCollisions_Type()
)
tnPMACStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsCollisions.setStatus("current")
_TnPMACStatsHighCapacityPkts_Type = Counter64
_TnPMACStatsHighCapacityPkts_Object = MibTableColumn
tnPMACStatsHighCapacityPkts = _TnPMACStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 31),
    _TnPMACStatsHighCapacityPkts_Type()
)
tnPMACStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts.setStatus("current")
_TnPMACStatsHighCapacityOctets_Type = Counter64
_TnPMACStatsHighCapacityOctets_Object = MibTableColumn
tnPMACStatsHighCapacityOctets = _TnPMACStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 32),
    _TnPMACStatsHighCapacityOctets_Type()
)
tnPMACStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityOctets.setStatus("current")
_TnPMACStatsHighCapacityPkts64Octets_Type = Counter64
_TnPMACStatsHighCapacityPkts64Octets_Object = MibTableColumn
tnPMACStatsHighCapacityPkts64Octets = _TnPMACStatsHighCapacityPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 33),
    _TnPMACStatsHighCapacityPkts64Octets_Type()
)
tnPMACStatsHighCapacityPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts64Octets.setStatus("current")
_TnPMACStatsHighCapacityPkts65to127Octets_Type = Counter64
_TnPMACStatsHighCapacityPkts65to127Octets_Object = MibTableColumn
tnPMACStatsHighCapacityPkts65to127Octets = _TnPMACStatsHighCapacityPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 34),
    _TnPMACStatsHighCapacityPkts65to127Octets_Type()
)
tnPMACStatsHighCapacityPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts65to127Octets.setStatus("current")
_TnPMACStatsHighCapacityPkts128to255Octets_Type = Counter64
_TnPMACStatsHighCapacityPkts128to255Octets_Object = MibTableColumn
tnPMACStatsHighCapacityPkts128to255Octets = _TnPMACStatsHighCapacityPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 35),
    _TnPMACStatsHighCapacityPkts128to255Octets_Type()
)
tnPMACStatsHighCapacityPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts128to255Octets.setStatus("current")
_TnPMACStatsHighCapacityPkts256to511Octets_Type = Counter64
_TnPMACStatsHighCapacityPkts256to511Octets_Object = MibTableColumn
tnPMACStatsHighCapacityPkts256to511Octets = _TnPMACStatsHighCapacityPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 36),
    _TnPMACStatsHighCapacityPkts256to511Octets_Type()
)
tnPMACStatsHighCapacityPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts256to511Octets.setStatus("current")
_TnPMACStatsHighCapacityPkts512to1023Octets_Type = Counter64
_TnPMACStatsHighCapacityPkts512to1023Octets_Object = MibTableColumn
tnPMACStatsHighCapacityPkts512to1023Octets = _TnPMACStatsHighCapacityPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 37),
    _TnPMACStatsHighCapacityPkts512to1023Octets_Type()
)
tnPMACStatsHighCapacityPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts512to1023Octets.setStatus("current")
_TnPMACStatsHighCapacityPkts1024to1518Octets_Type = Counter64
_TnPMACStatsHighCapacityPkts1024to1518Octets_Object = MibTableColumn
tnPMACStatsHighCapacityPkts1024to1518Octets = _TnPMACStatsHighCapacityPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 38),
    _TnPMACStatsHighCapacityPkts1024to1518Octets_Type()
)
tnPMACStatsHighCapacityPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts1024to1518Octets.setStatus("current")
_TnPMACStatsHighCapacityPkts1519toMaxOctets_Type = Counter64
_TnPMACStatsHighCapacityPkts1519toMaxOctets_Object = MibTableColumn
tnPMACStatsHighCapacityPkts1519toMaxOctets = _TnPMACStatsHighCapacityPkts1519toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 34, 1, 39),
    _TnPMACStatsHighCapacityPkts1519toMaxOctets_Type()
)
tnPMACStatsHighCapacityPkts1519toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPMACStatsHighCapacityPkts1519toMaxOctets.setStatus("current")
_TnMMACStatsAttributeTotal_Type = Integer32
_TnMMACStatsAttributeTotal_Object = MibScalar
tnMMACStatsAttributeTotal = _TnMMACStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 35),
    _TnMMACStatsAttributeTotal_Type()
)
tnMMACStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsAttributeTotal.setStatus("current")
_TnMMACStatsTable_Object = MibTable
tnMMACStatsTable = _TnMMACStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36)
)
if mibBuilder.loadTexts:
    tnMMACStatsTable.setStatus("current")
_TnMMACStatsEntry_Object = MibTableRow
tnMMACStatsEntry = _TnMMACStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1)
)
tnMMACStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnMMACStatsPortId"),
    (0, "TN-PMON-MIB", "tnMMACStatsInterval"),
    (0, "TN-PMON-MIB", "tnMMACStatsBin"),
)
if mibBuilder.loadTexts:
    tnMMACStatsEntry.setStatus("current")
_TnMMACStatsPortId_Type = TmnxPortID
_TnMMACStatsPortId_Object = MibTableColumn
tnMMACStatsPortId = _TnMMACStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 1),
    _TnMMACStatsPortId_Type()
)
tnMMACStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMMACStatsPortId.setStatus("current")
_TnMMACStatsInterval_Type = AluWdmStatsIntervalType
_TnMMACStatsInterval_Object = MibTableColumn
tnMMACStatsInterval = _TnMMACStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 2),
    _TnMMACStatsInterval_Type()
)
tnMMACStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMMACStatsInterval.setStatus("current")
_TnMMACStatsBin_Type = AluWdmStatsBinNumber
_TnMMACStatsBin_Object = MibTableColumn
tnMMACStatsBin = _TnMMACStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 3),
    _TnMMACStatsBin_Type()
)
tnMMACStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMMACStatsBin.setStatus("current")
_TnMMACStatsBinStatus_Type = AluWdmStatsBinStatus
_TnMMACStatsBinStatus_Object = MibTableColumn
tnMMACStatsBinStatus = _TnMMACStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 4),
    _TnMMACStatsBinStatus_Type()
)
tnMMACStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsBinStatus.setStatus("current")
_TnMMACStatsStartTime_Type = DateAndTime
_TnMMACStatsStartTime_Object = MibTableColumn
tnMMACStatsStartTime = _TnMMACStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 5),
    _TnMMACStatsStartTime_Type()
)
tnMMACStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsStartTime.setStatus("current")
_TnMMACStatsTotalMembers_Type = Integer32
_TnMMACStatsTotalMembers_Object = MibTableColumn
tnMMACStatsTotalMembers = _TnMMACStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 6),
    _TnMMACStatsTotalMembers_Type()
)
tnMMACStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsTotalMembers.setStatus("current")
_TnMMACStatsFrameAssErrorCount_Type = Counter64
_TnMMACStatsFrameAssErrorCount_Object = MibTableColumn
tnMMACStatsFrameAssErrorCount = _TnMMACStatsFrameAssErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 7),
    _TnMMACStatsFrameAssErrorCount_Type()
)
tnMMACStatsFrameAssErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsFrameAssErrorCount.setStatus("current")
_TnMMACStatsFrameSmdErrorCount_Type = Counter64
_TnMMACStatsFrameSmdErrorCount_Object = MibTableColumn
tnMMACStatsFrameSmdErrorCount = _TnMMACStatsFrameSmdErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 8),
    _TnMMACStatsFrameSmdErrorCount_Type()
)
tnMMACStatsFrameSmdErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsFrameSmdErrorCount.setStatus("current")
_TnMMACStatsFrameAssOkCount_Type = Counter64
_TnMMACStatsFrameAssOkCount_Object = MibTableColumn
tnMMACStatsFrameAssOkCount = _TnMMACStatsFrameAssOkCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 9),
    _TnMMACStatsFrameAssOkCount_Type()
)
tnMMACStatsFrameAssOkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsFrameAssOkCount.setStatus("current")
_TnMMACStatsFragCountRx_Type = Counter64
_TnMMACStatsFragCountRx_Object = MibTableColumn
tnMMACStatsFragCountRx = _TnMMACStatsFragCountRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 10),
    _TnMMACStatsFragCountRx_Type()
)
tnMMACStatsFragCountRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsFragCountRx.setStatus("current")
_TnMMACStatsFragCountTx_Type = Counter64
_TnMMACStatsFragCountTx_Object = MibTableColumn
tnMMACStatsFragCountTx = _TnMMACStatsFragCountTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 11),
    _TnMMACStatsFragCountTx_Type()
)
tnMMACStatsFragCountTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsFragCountTx.setStatus("current")
_TnMMACStatsHoldCount_Type = Counter64
_TnMMACStatsHoldCount_Object = MibTableColumn
tnMMACStatsHoldCount = _TnMMACStatsHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 36, 1, 12),
    _TnMMACStatsHoldCount_Type()
)
tnMMACStatsHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMMACStatsHoldCount.setStatus("current")
_TnRoeMapperRawCountStatsAttributeTotal_Type = Integer32
_TnRoeMapperRawCountStatsAttributeTotal_Object = MibScalar
tnRoeMapperRawCountStatsAttributeTotal = _TnRoeMapperRawCountStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 37),
    _TnRoeMapperRawCountStatsAttributeTotal_Type()
)
tnRoeMapperRawCountStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawCountStatsAttributeTotal.setStatus("current")
_TnRoeMapperRawCountStatsTable_Object = MibTable
tnRoeMapperRawCountStatsTable = _TnRoeMapperRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38)
)
if mibBuilder.loadTexts:
    tnRoeMapperRawCountStatsTable.setStatus("current")
_TnRoeMapperRawCountStatsEntry_Object = MibTableRow
tnRoeMapperRawCountStatsEntry = _TnRoeMapperRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1)
)
tnRoeMapperRawCountStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnRoeMapperRawCountStatsPortId"),
)
if mibBuilder.loadTexts:
    tnRoeMapperRawCountStatsEntry.setStatus("current")
_TnRoeMapperRawCountStatsPortId_Type = TmnxPortID
_TnRoeMapperRawCountStatsPortId_Object = MibTableColumn
tnRoeMapperRawCountStatsPortId = _TnRoeMapperRawCountStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 1),
    _TnRoeMapperRawCountStatsPortId_Type()
)
tnRoeMapperRawCountStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperRawCountStatsPortId.setStatus("current")


class _TnRoeMapperRawStatsMapperID_Type(Integer32):
    """Custom type tnRoeMapperRawStatsMapperID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeMapperRawStatsMapperID_Type.__name__ = "Integer32"
_TnRoeMapperRawStatsMapperID_Object = MibTableColumn
tnRoeMapperRawStatsMapperID = _TnRoeMapperRawStatsMapperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 2),
    _TnRoeMapperRawStatsMapperID_Type()
)
tnRoeMapperRawStatsMapperID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperRawStatsMapperID.setStatus("current")
_TnRoeMapperRawCountStatsClear_Type = TnCommand
_TnRoeMapperRawCountStatsClear_Object = MibTableColumn
tnRoeMapperRawCountStatsClear = _TnRoeMapperRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 3),
    _TnRoeMapperRawCountStatsClear_Type()
)
tnRoeMapperRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperRawCountStatsClear.setStatus("current")
_TnRoeMapperRawCountStatsStartTime_Type = DateAndTime
_TnRoeMapperRawCountStatsStartTime_Object = MibTableColumn
tnRoeMapperRawCountStatsStartTime = _TnRoeMapperRawCountStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 4),
    _TnRoeMapperRawCountStatsStartTime_Type()
)
tnRoeMapperRawCountStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawCountStatsStartTime.setStatus("current")
_TnRoeMapperRawCountStatsInPackets_Type = Counter64
_TnRoeMapperRawCountStatsInPackets_Object = MibTableColumn
tnRoeMapperRawCountStatsInPackets = _TnRoeMapperRawCountStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 5),
    _TnRoeMapperRawCountStatsInPackets_Type()
)
tnRoeMapperRawCountStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawCountStatsInPackets.setStatus("current")
_TnRoeMapperRawTxpackets_Type = Counter64
_TnRoeMapperRawTxpackets_Object = MibTableColumn
tnRoeMapperRawTxpackets = _TnRoeMapperRawTxpackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 6),
    _TnRoeMapperRawTxpackets_Type()
)
tnRoeMapperRawTxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawTxpackets.setStatus("current")
_TnRoeMapperRawTxbytes_Type = Counter64
_TnRoeMapperRawTxbytes_Object = MibTableColumn
tnRoeMapperRawTxbytes = _TnRoeMapperRawTxbytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 7),
    _TnRoeMapperRawTxbytes_Type()
)
tnRoeMapperRawTxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawTxbytes.setStatus("current")
_TnRoeMapperRawTxDropPackets_Type = Counter64
_TnRoeMapperRawTxDropPackets_Object = MibTableColumn
tnRoeMapperRawTxDropPackets = _TnRoeMapperRawTxDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 8),
    _TnRoeMapperRawTxDropPackets_Type()
)
tnRoeMapperRawTxDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawTxDropPackets.setStatus("current")
_TnRoeMapperRawEncapQueueOverrun_Type = Counter64
_TnRoeMapperRawEncapQueueOverrun_Object = MibTableColumn
tnRoeMapperRawEncapQueueOverrun = _TnRoeMapperRawEncapQueueOverrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 9),
    _TnRoeMapperRawEncapQueueOverrun_Type()
)
tnRoeMapperRawEncapQueueOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawEncapQueueOverrun.setStatus("current")
_TnRoeMapperRawGSMTimeSlotMismatch_Type = Counter64
_TnRoeMapperRawGSMTimeSlotMismatch_Object = MibTableColumn
tnRoeMapperRawGSMTimeSlotMismatch = _TnRoeMapperRawGSMTimeSlotMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 38, 1, 10),
    _TnRoeMapperRawGSMTimeSlotMismatch_Type()
)
tnRoeMapperRawGSMTimeSlotMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperRawGSMTimeSlotMismatch.setStatus("current")
_TnRoeDeMapperRawCountStatsAttributeTotal_Type = Integer32
_TnRoeDeMapperRawCountStatsAttributeTotal_Object = MibScalar
tnRoeDeMapperRawCountStatsAttributeTotal = _TnRoeDeMapperRawCountStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 39),
    _TnRoeDeMapperRawCountStatsAttributeTotal_Type()
)
tnRoeDeMapperRawCountStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawCountStatsAttributeTotal.setStatus("current")
_TnRoeDeMapperRawCountStatsTable_Object = MibTable
tnRoeDeMapperRawCountStatsTable = _TnRoeDeMapperRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40)
)
if mibBuilder.loadTexts:
    tnRoeDeMapperRawCountStatsTable.setStatus("current")
_TnRoeDeMapperRawCountStatsEntry_Object = MibTableRow
tnRoeDeMapperRawCountStatsEntry = _TnRoeDeMapperRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1)
)
tnRoeDeMapperRawCountStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnRoeDeMapperRawCountStatsPortId"),
)
if mibBuilder.loadTexts:
    tnRoeDeMapperRawCountStatsEntry.setStatus("current")
_TnRoeDeMapperRawCountStatsPortId_Type = TmnxPortID
_TnRoeDeMapperRawCountStatsPortId_Object = MibTableColumn
tnRoeDeMapperRawCountStatsPortId = _TnRoeDeMapperRawCountStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 1),
    _TnRoeDeMapperRawCountStatsPortId_Type()
)
tnRoeDeMapperRawCountStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawCountStatsPortId.setStatus("current")


class _TnRoeDeMapperRawStatsDeMapperID_Type(Integer32):
    """Custom type tnRoeDeMapperRawStatsDeMapperID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeDeMapperRawStatsDeMapperID_Type.__name__ = "Integer32"
_TnRoeDeMapperRawStatsDeMapperID_Object = MibTableColumn
tnRoeDeMapperRawStatsDeMapperID = _TnRoeDeMapperRawStatsDeMapperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 2),
    _TnRoeDeMapperRawStatsDeMapperID_Type()
)
tnRoeDeMapperRawStatsDeMapperID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawStatsDeMapperID.setStatus("current")
_TnRoeDeMapperRawCountStatsClear_Type = TnCommand
_TnRoeDeMapperRawCountStatsClear_Object = MibTableColumn
tnRoeDeMapperRawCountStatsClear = _TnRoeDeMapperRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 3),
    _TnRoeDeMapperRawCountStatsClear_Type()
)
tnRoeDeMapperRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawCountStatsClear.setStatus("current")
_TnRoeDeMapperRawStatsStartTime_Type = DateAndTime
_TnRoeDeMapperRawStatsStartTime_Object = MibTableColumn
tnRoeDeMapperRawStatsStartTime = _TnRoeDeMapperRawStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 4),
    _TnRoeDeMapperRawStatsStartTime_Type()
)
tnRoeDeMapperRawStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawStatsStartTime.setStatus("current")
_TnRoeDeMapperRawRxpackets_Type = Counter64
_TnRoeDeMapperRawRxpackets_Object = MibTableColumn
tnRoeDeMapperRawRxpackets = _TnRoeDeMapperRawRxpackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 5),
    _TnRoeDeMapperRawRxpackets_Type()
)
tnRoeDeMapperRawRxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawRxpackets.setStatus("current")
_TnRoeDeMapperRawRxbytes_Type = Counter64
_TnRoeDeMapperRawRxbytes_Object = MibTableColumn
tnRoeDeMapperRawRxbytes = _TnRoeDeMapperRawRxbytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 6),
    _TnRoeDeMapperRawRxbytes_Type()
)
tnRoeDeMapperRawRxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawRxbytes.setStatus("current")
_TnRoeDeMapperRawDecapQueueOverrun_Type = Counter64
_TnRoeDeMapperRawDecapQueueOverrun_Object = MibTableColumn
tnRoeDeMapperRawDecapQueueOverrun = _TnRoeDeMapperRawDecapQueueOverrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 7),
    _TnRoeDeMapperRawDecapQueueOverrun_Type()
)
tnRoeDeMapperRawDecapQueueOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawDecapQueueOverrun.setStatus("current")
_TnRoeDeMapperRawQueueUnderrun_Type = Counter64
_TnRoeDeMapperRawQueueUnderrun_Object = MibTableColumn
tnRoeDeMapperRawQueueUnderrun = _TnRoeDeMapperRawQueueUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 8),
    _TnRoeDeMapperRawQueueUnderrun_Type()
)
tnRoeDeMapperRawQueueUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawQueueUnderrun.setStatus("current")
_TnRoeDeMapperRawDecapPacketMissing_Type = Counter64
_TnRoeDeMapperRawDecapPacketMissing_Object = MibTableColumn
tnRoeDeMapperRawDecapPacketMissing = _TnRoeDeMapperRawDecapPacketMissing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 9),
    _TnRoeDeMapperRawDecapPacketMissing_Type()
)
tnRoeDeMapperRawDecapPacketMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawDecapPacketMissing.setStatus("current")
_TnRoeDeMapperRawDecapPacketSizeMismatch_Type = Counter64
_TnRoeDeMapperRawDecapPacketSizeMismatch_Object = MibTableColumn
tnRoeDeMapperRawDecapPacketSizeMismatch = _TnRoeDeMapperRawDecapPacketSizeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 40, 1, 10),
    _TnRoeDeMapperRawDecapPacketSizeMismatch_Type()
)
tnRoeDeMapperRawDecapPacketSizeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperRawDecapPacketSizeMismatch.setStatus("current")
_TnRoeRawCountStatsAttributeTotal_Type = Integer32
_TnRoeRawCountStatsAttributeTotal_Object = MibScalar
tnRoeRawCountStatsAttributeTotal = _TnRoeRawCountStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 41),
    _TnRoeRawCountStatsAttributeTotal_Type()
)
tnRoeRawCountStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeRawCountStatsAttributeTotal.setStatus("current")
_TnRoeRawCountStatsTable_Object = MibTable
tnRoeRawCountStatsTable = _TnRoeRawCountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 42)
)
if mibBuilder.loadTexts:
    tnRoeRawCountStatsTable.setStatus("current")
_TnRoeRawCountStatsEntry_Object = MibTableRow
tnRoeRawCountStatsEntry = _TnRoeRawCountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 42, 1)
)
tnRoeRawCountStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnRoeRawStatsPortId"),
)
if mibBuilder.loadTexts:
    tnRoeRawCountStatsEntry.setStatus("current")
_TnRoeRawStatsPortId_Type = TmnxPortID
_TnRoeRawStatsPortId_Object = MibTableColumn
tnRoeRawStatsPortId = _TnRoeRawStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 42, 1, 1),
    _TnRoeRawStatsPortId_Type()
)
tnRoeRawStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeRawStatsPortId.setStatus("current")
_TnRoeRawCountStatsClear_Type = TnCommand
_TnRoeRawCountStatsClear_Object = MibTableColumn
tnRoeRawCountStatsClear = _TnRoeRawCountStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 42, 1, 2),
    _TnRoeRawCountStatsClear_Type()
)
tnRoeRawCountStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeRawCountStatsClear.setStatus("current")
_TnRoeRawStatsStartTime_Type = DateAndTime
_TnRoeRawStatsStartTime_Object = MibTableColumn
tnRoeRawStatsStartTime = _TnRoeRawStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 42, 1, 3),
    _TnRoeRawStatsStartTime_Type()
)
tnRoeRawStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeRawStatsStartTime.setStatus("current")
_TnRoeRawDecapPktsDropped_Type = Counter64
_TnRoeRawDecapPktsDropped_Object = MibTableColumn
tnRoeRawDecapPktsDropped = _TnRoeRawDecapPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 42, 1, 4),
    _TnRoeRawDecapPktsDropped_Type()
)
tnRoeRawDecapPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeRawDecapPktsDropped.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-PMON-MIB",
    **{"AluWdmPmonPolicyType": AluWdmPmonPolicyType,
       "AluWdmStatsIntervalType": AluWdmStatsIntervalType,
       "AluWdmStatsBinNumber": AluWdmStatsBinNumber,
       "AluWdmStatsBinStatus": AluWdmStatsBinStatus,
       "AluWdmPmonStatsClearType": AluWdmPmonStatsClearType,
       "tnPmonMIBModule": tnPmonMIBModule,
       "tnPmonObjs": tnPmonObjs,
       "tnPmonPolicyAttributeTotal": tnPmonPolicyAttributeTotal,
       "tnPmonPolicyTable": tnPmonPolicyTable,
       "tnPmonPolicyEntry": tnPmonPolicyEntry,
       "tnPmonPolicyType": tnPmonPolicyType,
       "tnPmonPolicyId": tnPmonPolicyId,
       "tnPmonPolicyRowStatus": tnPmonPolicyRowStatus,
       "tnPmonPolicyDescription": tnPmonPolicyDescription,
       "tnPmonPolicyNumOfBins15Min": tnPmonPolicyNumOfBins15Min,
       "tnPmonPolicyNumOfBins1Day": tnPmonPolicyNumOfBins1Day,
       "tnPmonPolicyFlrInterval15Min": tnPmonPolicyFlrInterval15Min,
       "tnPmonPolicyFlrInterval1Day": tnPmonPolicyFlrInterval1Day,
       "tnPmonPolicyFlrAvailabilityInterval15Min": tnPmonPolicyFlrAvailabilityInterval15Min,
       "tnPmonPolicyFlrAvailabilityInterval1Day": tnPmonPolicyFlrAvailabilityInterval1Day,
       "tnPmonPolicyNumOfBinsContinuous": tnPmonPolicyNumOfBinsContinuous,
       "tnPmonPolicyAvailFlrThreshold": tnPmonPolicyAvailFlrThreshold,
       "tnPmonPolicyAvailFlrNumOfIntervals": tnPmonPolicyAvailFlrNumOfIntervals,
       "tnPmonPolicyFramesPerDeltaT": tnPmonPolicyFramesPerDeltaT,
       "tnPmonClearAttributeTotal": tnPmonClearAttributeTotal,
       "tnPmonClearTable": tnPmonClearTable,
       "tnPmonClearEntry": tnPmonClearEntry,
       "tnPmonClearType": tnPmonClearType,
       "tnPmonClearPortId": tnPmonClearPortId,
       "tnPmonClearEncapValue": tnPmonClearEncapValue,
       "tnPmonClearTestName": tnPmonClearTestName,
       "tnPmonClearInterval": tnPmonClearInterval,
       "tnPmonClearBin": tnPmonClearBin,
       "tnPmonClearRoeMapperId": tnPmonClearRoeMapperId,
       "tnPmonClearRoeDeMapperId": tnPmonClearRoeDeMapperId,
       "tnPmonTcaAttributeTotal": tnPmonTcaAttributeTotal,
       "tnPmonTcaTable": tnPmonTcaTable,
       "tnPmonTcaEntry": tnPmonTcaEntry,
       "tnPmonTcaInterval": tnPmonTcaInterval,
       "tnPmonTcaSubgroup": tnPmonTcaSubgroup,
       "tnPmonTcaId": tnPmonTcaId,
       "tnPmonTcaVariable": tnPmonTcaVariable,
       "tnPmonTcaValue": tnPmonTcaValue,
       "tnEthPortStatsAttributeTotal": tnEthPortStatsAttributeTotal,
       "tnEthPortStatsTable": tnEthPortStatsTable,
       "tnEthPortStatsEntry": tnEthPortStatsEntry,
       "tnEthPortStatsPortId": tnEthPortStatsPortId,
       "tnEthPortStatsInterval": tnEthPortStatsInterval,
       "tnEthPortStatsBin": tnEthPortStatsBin,
       "tnEthPortStatsBinStatus": tnEthPortStatsBinStatus,
       "tnEthPortStatsStartTime": tnEthPortStatsStartTime,
       "tnEthPortStatsTotalMembers": tnEthPortStatsTotalMembers,
       "tnEthPortStatsIfInOctets": tnEthPortStatsIfInOctets,
       "tnEthPortStatsIfInUcastPkts": tnEthPortStatsIfInUcastPkts,
       "tnEthPortStatsIfInDiscards": tnEthPortStatsIfInDiscards,
       "tnEthPortStatsIfInErrors": tnEthPortStatsIfInErrors,
       "tnEthPortStatsIfInUnknownProtos": tnEthPortStatsIfInUnknownProtos,
       "tnEthPortStatsIfInMulticastPkts": tnEthPortStatsIfInMulticastPkts,
       "tnEthPortStatsIfInBroadcastPkts": tnEthPortStatsIfInBroadcastPkts,
       "tnEthPortStatsIfOutOctets": tnEthPortStatsIfOutOctets,
       "tnEthPortStatsIfOutUcastPkts": tnEthPortStatsIfOutUcastPkts,
       "tnEthPortStatsIfOutDiscards": tnEthPortStatsIfOutDiscards,
       "tnEthPortStatsIfOutErrors": tnEthPortStatsIfOutErrors,
       "tnEthPortStatsIfOutMulticastPkts": tnEthPortStatsIfOutMulticastPkts,
       "tnEthPortStatsIfOutBroadcastPkts": tnEthPortStatsIfOutBroadcastPkts,
       "tnEthPortStatsIfInPkts": tnEthPortStatsIfInPkts,
       "tnEthPortStatsIfOutPkts": tnEthPortStatsIfOutPkts,
       "tnEthPortEtherStatsDropEvents": tnEthPortEtherStatsDropEvents,
       "tnEthPortEtherStatsBroadcastPkts": tnEthPortEtherStatsBroadcastPkts,
       "tnEthPortEtherStatsMulticastPkts": tnEthPortEtherStatsMulticastPkts,
       "tnEthPortEtherStatsCRCAlignErrors": tnEthPortEtherStatsCRCAlignErrors,
       "tnEthPortEtherStatsUndersizePkts": tnEthPortEtherStatsUndersizePkts,
       "tnEthPortEtherStatsOversizePkts": tnEthPortEtherStatsOversizePkts,
       "tnEthPortEtherStatsFragments": tnEthPortEtherStatsFragments,
       "tnEthPortEtherStatsJabbers": tnEthPortEtherStatsJabbers,
       "tnEthPortEtherStatsCollisions": tnEthPortEtherStatsCollisions,
       "tnEthPortEtherStatsHighCapacityPkts": tnEthPortEtherStatsHighCapacityPkts,
       "tnEthPortEtherStatsHighCapacityOctets": tnEthPortEtherStatsHighCapacityOctets,
       "tnEthPortEtherStatsHighCapacityPkts64Octets": tnEthPortEtherStatsHighCapacityPkts64Octets,
       "tnEthPortEtherStatsHighCapacityPkts65to127Octets": tnEthPortEtherStatsHighCapacityPkts65to127Octets,
       "tnEthPortEtherStatsHighCapacityPkts128to255Octets": tnEthPortEtherStatsHighCapacityPkts128to255Octets,
       "tnEthPortEtherStatsHighCapacityPkts256to511Octets": tnEthPortEtherStatsHighCapacityPkts256to511Octets,
       "tnEthPortEtherStatsHighCapacityPkts512to1023Octets": tnEthPortEtherStatsHighCapacityPkts512to1023Octets,
       "tnEthPortEtherStatsHighCapacityPkts1024to1518Octets": tnEthPortEtherStatsHighCapacityPkts1024to1518Octets,
       "tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets": tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets,
       "tnEthPortEgrQueueStatsAttributeTotal": tnEthPortEgrQueueStatsAttributeTotal,
       "tnEthPortEgrQueueStatsTable": tnEthPortEgrQueueStatsTable,
       "tnEthPortEgrQueueStatsEntry": tnEthPortEgrQueueStatsEntry,
       "tnEthPortStatsQueueId": tnEthPortStatsQueueId,
       "tnEthPortEgrQueueStatsInProfilePktsForwarded": tnEthPortEgrQueueStatsInProfilePktsForwarded,
       "tnEthPortEgrQueueStatsOutOfProfilePktsForwarded": tnEthPortEgrQueueStatsOutOfProfilePktsForwarded,
       "tnEthPortEgrQueueStatsInProfileOctetsForwarded": tnEthPortEgrQueueStatsInProfileOctetsForwarded,
       "tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded": tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded,
       "tnEthPortEgrQueueStatsInProfilePktsDropped": tnEthPortEgrQueueStatsInProfilePktsDropped,
       "tnEthPortEgrQueueStatsOutOfProfilePktsDropped": tnEthPortEgrQueueStatsOutOfProfilePktsDropped,
       "tnEthPortEgrQueueStatsInProfileOctetsDropped": tnEthPortEgrQueueStatsInProfileOctetsDropped,
       "tnEthPortEgrQueueStatsOutOfProfileOctetsDropped": tnEthPortEgrQueueStatsOutOfProfileOctetsDropped,
       "tnSapStatsAttributeTotal": tnSapStatsAttributeTotal,
       "tnSapStatsTable": tnSapStatsTable,
       "tnSapStatsEntry": tnSapStatsEntry,
       "tnSapStatsPortId": tnSapStatsPortId,
       "tnSapStatsEncapVal": tnSapStatsEncapVal,
       "tnSapStatsInterval": tnSapStatsInterval,
       "tnSapStatsBin": tnSapStatsBin,
       "tnSapStatsBinStatus": tnSapStatsBinStatus,
       "tnSapStatsStartTime": tnSapStatsStartTime,
       "tnSapStatsTotalMembers": tnSapStatsTotalMembers,
       "tnSapStatsIngressPktsForwarded": tnSapStatsIngressPktsForwarded,
       "tnSapStatsIngressOctetsForwarded": tnSapStatsIngressOctetsForwarded,
       "tnSapStatsEgressPktsForwarded": tnSapStatsEgressPktsForwarded,
       "tnSapStatsEgressOctetsForwarded": tnSapStatsEgressOctetsForwarded,
       "tnSapStatsIngressPktsDropped": tnSapStatsIngressPktsDropped,
       "tnSapStatsIngressOctetsDropped": tnSapStatsIngressOctetsDropped,
       "tnSapStatsIngressExtraTagPktsDropped": tnSapStatsIngressExtraTagPktsDropped,
       "tnSapStatsIngressExtraTagOctetsDropped": tnSapStatsIngressExtraTagOctetsDropped,
       "tnSapMeterStatsAttributeTotal": tnSapMeterStatsAttributeTotal,
       "tnSapMeterStatsTable": tnSapMeterStatsTable,
       "tnSapMeterStatsEntry": tnSapMeterStatsEntry,
       "tnSapStatsMeterId": tnSapStatsMeterId,
       "tnSapMeterStatsInProfilePktsForwarded": tnSapMeterStatsInProfilePktsForwarded,
       "tnSapMeterStatsOutOfProfilePktsForwarded": tnSapMeterStatsOutOfProfilePktsForwarded,
       "tnSapMeterStatsInProfileOctetsForwarded": tnSapMeterStatsInProfileOctetsForwarded,
       "tnSapMeterStatsOutOfProfileOctetsForwarded": tnSapMeterStatsOutOfProfileOctetsForwarded,
       "tnEthCfmTWSlmStatsAttributeTotal": tnEthCfmTWSlmStatsAttributeTotal,
       "tnEthCfmTWSlmStatsTable": tnEthCfmTWSlmStatsTable,
       "tnEthCfmTWSlmStatsEntry": tnEthCfmTWSlmStatsEntry,
       "tnEthCfmTWSlmStatsTestName": tnEthCfmTWSlmStatsTestName,
       "tnEthCfmTWSlmStatsInterval": tnEthCfmTWSlmStatsInterval,
       "tnEthCfmTWSlmStatsBin": tnEthCfmTWSlmStatsBin,
       "tnEthCfmTWSlmStatsBinStatus": tnEthCfmTWSlmStatsBinStatus,
       "tnEthCfmTWSlmStatsStartTime": tnEthCfmTWSlmStatsStartTime,
       "tnEthCfmTWSlmStatsTotalMembers": tnEthCfmTWSlmStatsTotalMembers,
       "tnEthCfmTWSlmStatsNearEndFrameLossRatioMin": tnEthCfmTWSlmStatsNearEndFrameLossRatioMin,
       "tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage": tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage,
       "tnEthCfmTWSlmStatsNearEndFrameLossRatioMax": tnEthCfmTWSlmStatsNearEndFrameLossRatioMax,
       "tnEthCfmTWSlmStatsFarEndFrameLossRatioMin": tnEthCfmTWSlmStatsFarEndFrameLossRatioMin,
       "tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage": tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage,
       "tnEthCfmTWSlmStatsFarEndFrameLossRatioMax": tnEthCfmTWSlmStatsFarEndFrameLossRatioMax,
       "tnEthCfmTWSlmStatsNearEndHighLoss": tnEthCfmTWSlmStatsNearEndHighLoss,
       "tnEthCfmTWSlmStatsFarEndHighLoss": tnEthCfmTWSlmStatsFarEndHighLoss,
       "tnEthCfmTWSlmStatsNearEndUnavailable": tnEthCfmTWSlmStatsNearEndUnavailable,
       "tnEthCfmTWSlmStatsFarEndUnavailable": tnEthCfmTWSlmStatsFarEndUnavailable,
       "tnEthCfmTWDmStatsAttributeTotal": tnEthCfmTWDmStatsAttributeTotal,
       "tnEthCfmTWDmStatsTable": tnEthCfmTWDmStatsTable,
       "tnEthCfmTWDmStatsEntry": tnEthCfmTWDmStatsEntry,
       "tnEthCfmTWDmStatsTestName": tnEthCfmTWDmStatsTestName,
       "tnEthCfmTWDmStatsInterval": tnEthCfmTWDmStatsInterval,
       "tnEthCfmTWDmStatsBin": tnEthCfmTWDmStatsBin,
       "tnEthCfmTWDmStatsBinStatus": tnEthCfmTWDmStatsBinStatus,
       "tnEthCfmTWDmStatsStartTime": tnEthCfmTWDmStatsStartTime,
       "tnEthCfmTWDmStatsTotalMembers": tnEthCfmTWDmStatsTotalMembers,
       "tnEthCfmTWDmStatsRoundTripFrameDelayMin": tnEthCfmTWDmStatsRoundTripFrameDelayMin,
       "tnEthCfmTWDmStatsRoundTripFrameDelayAverage": tnEthCfmTWDmStatsRoundTripFrameDelayAverage,
       "tnEthCfmTWDmStatsRoundTripFrameDelayMax": tnEthCfmTWDmStatsRoundTripFrameDelayMax,
       "tnEthCfmTWDmStatsNearEndFrameDelayVariationMin": tnEthCfmTWDmStatsNearEndFrameDelayVariationMin,
       "tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage": tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage,
       "tnEthCfmTWDmStatsNearEndFrameDelayVariationMax": tnEthCfmTWDmStatsNearEndFrameDelayVariationMax,
       "tnEthCfmTWDmStatsFarEndFrameDelayVariationMin": tnEthCfmTWDmStatsFarEndFrameDelayVariationMin,
       "tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage": tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage,
       "tnEthCfmTWDmStatsFarEndFrameDelayVariationMax": tnEthCfmTWDmStatsFarEndFrameDelayVariationMax,
       "tnEthCfmTWDmStatsNearEndFrameDelayMin": tnEthCfmTWDmStatsNearEndFrameDelayMin,
       "tnEthCfmTWDmStatsNearEndFrameDelayAverage": tnEthCfmTWDmStatsNearEndFrameDelayAverage,
       "tnEthCfmTWDmStatsNearEndFrameDelayMax": tnEthCfmTWDmStatsNearEndFrameDelayMax,
       "tnEthCfmTWDmStatsFarEndFrameDelayMin": tnEthCfmTWDmStatsFarEndFrameDelayMin,
       "tnEthCfmTWDmStatsFarEndFrameDelayAverage": tnEthCfmTWDmStatsFarEndFrameDelayAverage,
       "tnEthCfmTWDmStatsFarEndFrameDelayMax": tnEthCfmTWDmStatsFarEndFrameDelayMax,
       "tnEthCfmTWLmStatsAttributeTotal": tnEthCfmTWLmStatsAttributeTotal,
       "tnEthCfmTWLmStatsTable": tnEthCfmTWLmStatsTable,
       "tnEthCfmTWLmStatsEntry": tnEthCfmTWLmStatsEntry,
       "tnEthCfmTWLmStatsTestName": tnEthCfmTWLmStatsTestName,
       "tnEthCfmTWLmStatsInterval": tnEthCfmTWLmStatsInterval,
       "tnEthCfmTWLmStatsBin": tnEthCfmTWLmStatsBin,
       "tnEthCfmTWLmStatsBinStatus": tnEthCfmTWLmStatsBinStatus,
       "tnEthCfmTWLmStatsStartTime": tnEthCfmTWLmStatsStartTime,
       "tnEthCfmTWLmStatsTotalMembers": tnEthCfmTWLmStatsTotalMembers,
       "tnEthCfmTWLmStatsNearEndFrameLossRatioMin": tnEthCfmTWLmStatsNearEndFrameLossRatioMin,
       "tnEthCfmTWLmStatsNearEndFrameLossRatioAverage": tnEthCfmTWLmStatsNearEndFrameLossRatioAverage,
       "tnEthCfmTWLmStatsNearEndFrameLossRatioMax": tnEthCfmTWLmStatsNearEndFrameLossRatioMax,
       "tnEthCfmTWLmStatsFarEndFrameLossRatioMin": tnEthCfmTWLmStatsFarEndFrameLossRatioMin,
       "tnEthCfmTWLmStatsFarEndFrameLossRatioAverage": tnEthCfmTWLmStatsFarEndFrameLossRatioAverage,
       "tnEthCfmTWLmStatsFarEndFrameLossRatioMax": tnEthCfmTWLmStatsFarEndFrameLossRatioMax,
       "tnEthCfmTWLmStatsNearEndHighLoss": tnEthCfmTWLmStatsNearEndHighLoss,
       "tnEthCfmTWLmStatsFarEndHighLoss": tnEthCfmTWLmStatsFarEndHighLoss,
       "tnEthCfmTWLmStatsNearEndUnavailable": tnEthCfmTWLmStatsNearEndUnavailable,
       "tnEthCfmTWLmStatsFarEndUnavailable": tnEthCfmTWLmStatsFarEndUnavailable,
       "tnEthCfmTWLmStatsTransmittedLMMFrame": tnEthCfmTWLmStatsTransmittedLMMFrame,
       "tnEthCfmTWLmStatsReceivedLMRFrame": tnEthCfmTWLmStatsReceivedLMRFrame,
       "tnEthCfmTWLmStatsNearEndTransmittedDataFrame": tnEthCfmTWLmStatsNearEndTransmittedDataFrame,
       "tnEthCfmTWLmStatsNearEndReceivedDataFrame": tnEthCfmTWLmStatsNearEndReceivedDataFrame,
       "tnEthCfmTWLmStatsFarEndTransmittedDataFrame": tnEthCfmTWLmStatsFarEndTransmittedDataFrame,
       "tnEthCfmTWLmStatsFarEndReceivedDataFrame": tnEthCfmTWLmStatsFarEndReceivedDataFrame,
       "tnPktWanifStatsAttributeTotal": tnPktWanifStatsAttributeTotal,
       "tnPktWanifStatsTable": tnPktWanifStatsTable,
       "tnPktWanifStatsEntry": tnPktWanifStatsEntry,
       "tnPktWanifStatsPortId": tnPktWanifStatsPortId,
       "tnPktWanifStatsInterval": tnPktWanifStatsInterval,
       "tnPktWanifStatsBin": tnPktWanifStatsBin,
       "tnPktWanifStatsBinStatus": tnPktWanifStatsBinStatus,
       "tnPktWanifStatsStartTime": tnPktWanifStatsStartTime,
       "tnPktWanifStatsInPackets": tnPktWanifStatsInPackets,
       "tnPktWanifStatsInOctets": tnPktWanifStatsInOctets,
       "tnPktWanifStatsInUcastPkts": tnPktWanifStatsInUcastPkts,
       "tnPktWanifStatsInDiscards": tnPktWanifStatsInDiscards,
       "tnPktWanifStatsInErrors": tnPktWanifStatsInErrors,
       "tnPktWanifStatsInUnknownProtos": tnPktWanifStatsInUnknownProtos,
       "tnPktWanifStatsInMulticastPkts": tnPktWanifStatsInMulticastPkts,
       "tnPktWanifStatsInBroadcastPkts": tnPktWanifStatsInBroadcastPkts,
       "tnPktWanifStatsOutPackets": tnPktWanifStatsOutPackets,
       "tnPktWanifStatsOutOctets": tnPktWanifStatsOutOctets,
       "tnPktWanifStatsOutUcastPkts": tnPktWanifStatsOutUcastPkts,
       "tnPktWanifStatsOutDiscards": tnPktWanifStatsOutDiscards,
       "tnPktWanifStatsOutErrors": tnPktWanifStatsOutErrors,
       "tnPktWanifStatsOutMulticastPkts": tnPktWanifStatsOutMulticastPkts,
       "tnPktWanifStatsOutBroadcastPkts": tnPktWanifStatsOutBroadcastPkts,
       "tnPktWanifStatsDropEvents": tnPktWanifStatsDropEvents,
       "tnPktWanifStatsBroadcastPkts": tnPktWanifStatsBroadcastPkts,
       "tnPktWanifStatsMulticastPkts": tnPktWanifStatsMulticastPkts,
       "tnPktWanifStatsCRCAlignErrors": tnPktWanifStatsCRCAlignErrors,
       "tnPktWanifStatsUndersizePkts": tnPktWanifStatsUndersizePkts,
       "tnPktWanifStatsOversizePkts": tnPktWanifStatsOversizePkts,
       "tnPktWanifStatsFragments": tnPktWanifStatsFragments,
       "tnPktWanifStatsJabbers": tnPktWanifStatsJabbers,
       "tnPktWanifStatsCollisions": tnPktWanifStatsCollisions,
       "tnPktWanifStatsHighCapacityPkts": tnPktWanifStatsHighCapacityPkts,
       "tnPktWanifStatsHighCapacityOctets": tnPktWanifStatsHighCapacityOctets,
       "tnPktWanifStatsHighCapacityPktsSize64": tnPktWanifStatsHighCapacityPktsSize64,
       "tnPktWanifStatsHighCapacityPktsSize65to127": tnPktWanifStatsHighCapacityPktsSize65to127,
       "tnPktWanifStatsHighCapacityPktsSize128to255": tnPktWanifStatsHighCapacityPktsSize128to255,
       "tnPktWanifStatsHighCapacityPktsSize256to511": tnPktWanifStatsHighCapacityPktsSize256to511,
       "tnPktWanifStatsHighCapacityPktsSize512to1023": tnPktWanifStatsHighCapacityPktsSize512to1023,
       "tnPktWanifStatsHighCapacityPktsSize1024to1518": tnPktWanifStatsHighCapacityPktsSize1024to1518,
       "tnPktWanifStatsHighCapacityPktsSize1519toMax": tnPktWanifStatsHighCapacityPktsSize1519toMax,
       "tnPktWanifStatsTooLongFrames": tnPktWanifStatsTooLongFrames,
       "tnPktWanifRawCountStatsAttributeTotal": tnPktWanifRawCountStatsAttributeTotal,
       "tnPktWanifRawCountStatsTable": tnPktWanifRawCountStatsTable,
       "tnPktWanifRawCountStatsEntry": tnPktWanifRawCountStatsEntry,
       "tnPktWanifRawCountStatsPortId": tnPktWanifRawCountStatsPortId,
       "tnPktWanifRawCountStatsClear": tnPktWanifRawCountStatsClear,
       "tnPktWanifRawCountStatsStartTime": tnPktWanifRawCountStatsStartTime,
       "tnPktWanifRawCountStatsInPackets": tnPktWanifRawCountStatsInPackets,
       "tnPktWanifRawCountStatsInOctets": tnPktWanifRawCountStatsInOctets,
       "tnPktWanifRawCountStatsInUcastPkts": tnPktWanifRawCountStatsInUcastPkts,
       "tnPktWanifRawCountStatsInDiscards": tnPktWanifRawCountStatsInDiscards,
       "tnPktWanifRawCountStatsInErrors": tnPktWanifRawCountStatsInErrors,
       "tnPktWanifRawCountStatsInUnknownProtos": tnPktWanifRawCountStatsInUnknownProtos,
       "tnPktWanifRawCountStatsInMulticastPkts": tnPktWanifRawCountStatsInMulticastPkts,
       "tnPktWanifRawCountStatsInBroadcastPkts": tnPktWanifRawCountStatsInBroadcastPkts,
       "tnPktWanifRawCountStatsOutPackets": tnPktWanifRawCountStatsOutPackets,
       "tnPktWanifRawCountStatsOutOctets": tnPktWanifRawCountStatsOutOctets,
       "tnPktWanifRawCountStatsOutUcastPkts": tnPktWanifRawCountStatsOutUcastPkts,
       "tnPktWanifRawCountStatsOutDiscards": tnPktWanifRawCountStatsOutDiscards,
       "tnPktWanifRawCountStatsOutErrors": tnPktWanifRawCountStatsOutErrors,
       "tnPktWanifRawCountStatsOutMulticastPkts": tnPktWanifRawCountStatsOutMulticastPkts,
       "tnPktWanifRawCountStatsOutBroadcastPkts": tnPktWanifRawCountStatsOutBroadcastPkts,
       "tnPktWanifRawCountStatsDropEvents": tnPktWanifRawCountStatsDropEvents,
       "tnPktWanifRawCountStatsBroadcastPkts": tnPktWanifRawCountStatsBroadcastPkts,
       "tnPktWanifRawCountStatsMulticastPkts": tnPktWanifRawCountStatsMulticastPkts,
       "tnPktWanifRawCountStatsCRCAlignErrors": tnPktWanifRawCountStatsCRCAlignErrors,
       "tnPktWanifRawCountStatsUndersizePkts": tnPktWanifRawCountStatsUndersizePkts,
       "tnPktWanifRawCountStatsOversizePkts": tnPktWanifRawCountStatsOversizePkts,
       "tnPktWanifRawCountStatsFragments": tnPktWanifRawCountStatsFragments,
       "tnPktWanifRawCountStatsJabbers": tnPktWanifRawCountStatsJabbers,
       "tnPktWanifRawCountStatsCollisions": tnPktWanifRawCountStatsCollisions,
       "tnPktWanifRawCountStatsHighCapacityPkts": tnPktWanifRawCountStatsHighCapacityPkts,
       "tnPktWanifRawCountStatsHighCapacityOctets": tnPktWanifRawCountStatsHighCapacityOctets,
       "tnPktWanifRawCountStatsHighCapacityPktsSize64": tnPktWanifRawCountStatsHighCapacityPktsSize64,
       "tnPktWanifRawCountStatsHighCapacityPktsSize65to127": tnPktWanifRawCountStatsHighCapacityPktsSize65to127,
       "tnPktWanifRawCountStatsHighCapacityPktsSize128to255": tnPktWanifRawCountStatsHighCapacityPktsSize128to255,
       "tnPktWanifRawCountStatsHighCapacityPktsSize256to511": tnPktWanifRawCountStatsHighCapacityPktsSize256to511,
       "tnPktWanifRawCountStatsHighCapacityPktsSize512to1023": tnPktWanifRawCountStatsHighCapacityPktsSize512to1023,
       "tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518": tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518,
       "tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax": tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax,
       "tnPktWanifRawCountStatsTooLongFrames": tnPktWanifRawCountStatsTooLongFrames,
       "tnRoeStatsAttributeTotal": tnRoeStatsAttributeTotal,
       "tnRoeStatsTable": tnRoeStatsTable,
       "tnRoeStatsEntry": tnRoeStatsEntry,
       "tnRoeStatsPortId": tnRoeStatsPortId,
       "tnRoeStatsInterval": tnRoeStatsInterval,
       "tnRoeStatsBin": tnRoeStatsBin,
       "tnRoeStatsBinStatus": tnRoeStatsBinStatus,
       "tnRoeStatsStartTime": tnRoeStatsStartTime,
       "tnRoeStatsTotalMembers": tnRoeStatsTotalMembers,
       "tnRoeStatsDecapPktsDropped": tnRoeStatsDecapPktsDropped,
       "tnRoeStatsDecapPktMiss": tnRoeStatsDecapPktMiss,
       "tnRoeMapperStatsAttributeTotal": tnRoeMapperStatsAttributeTotal,
       "tnRoeMapperStatsTable": tnRoeMapperStatsTable,
       "tnRoeMapperStatsEntry": tnRoeMapperStatsEntry,
       "tnRoeMapperStatsPortId": tnRoeMapperStatsPortId,
       "tnRoeMapperStatsMapperID": tnRoeMapperStatsMapperID,
       "tnRoeMapperStatsInterval": tnRoeMapperStatsInterval,
       "tnRoeMapperStatsBin": tnRoeMapperStatsBin,
       "tnRoeMapperStatsBinStatus": tnRoeMapperStatsBinStatus,
       "tnRoeMapperStatsStartTime": tnRoeMapperStatsStartTime,
       "tnRoeMapperStatsTotalMembers": tnRoeMapperStatsTotalMembers,
       "tnRoeMapperStatsTxpackets": tnRoeMapperStatsTxpackets,
       "tnRoeMapperStatsTxbytes": tnRoeMapperStatsTxbytes,
       "tnRoeMapperStatsTxDropPackets": tnRoeMapperStatsTxDropPackets,
       "tnRoeMapperStatsEncapQueueOverrun": tnRoeMapperStatsEncapQueueOverrun,
       "tnRoeMapperStatsGSMTimeSlotMismatch": tnRoeMapperStatsGSMTimeSlotMismatch,
       "tnRoeDeMapperStatsAttributeTotal": tnRoeDeMapperStatsAttributeTotal,
       "tnRoeDeMapperStatsTable": tnRoeDeMapperStatsTable,
       "tnRoeDeMapperStatsEntry": tnRoeDeMapperStatsEntry,
       "tnRoeDeMapperStatsPortId": tnRoeDeMapperStatsPortId,
       "tnRoeDeMapperStatsDeMapperID": tnRoeDeMapperStatsDeMapperID,
       "tnRoeDeMapperStatsInterval": tnRoeDeMapperStatsInterval,
       "tnRoeDeMapperStatsBin": tnRoeDeMapperStatsBin,
       "tnRoeDeMapperStatsBinStatus": tnRoeDeMapperStatsBinStatus,
       "tnRoeDeMapperStatsStartTime": tnRoeDeMapperStatsStartTime,
       "tnRoeDeMapperStatsTotalMembers": tnRoeDeMapperStatsTotalMembers,
       "tnRoeDeMapperStatsRxpackets": tnRoeDeMapperStatsRxpackets,
       "tnRoeDeMapperStatsRxbytes": tnRoeDeMapperStatsRxbytes,
       "tnRoeDeMapperStatsDecapQueueOverrun": tnRoeDeMapperStatsDecapQueueOverrun,
       "tnRoeDeMapperStatsQueueUnderrun": tnRoeDeMapperStatsQueueUnderrun,
       "tnRoeDeMapperStatsDecapPacketMissing": tnRoeDeMapperStatsDecapPacketMissing,
       "tnRoeDeMapperStatsDecapPacketSizeMismatch": tnRoeDeMapperStatsDecapPacketSizeMismatch,
       "tnEMACStatsAttributeTotal": tnEMACStatsAttributeTotal,
       "tnEMACStatsTable": tnEMACStatsTable,
       "tnEMACStatsEntry": tnEMACStatsEntry,
       "tnEMACStatsPortId": tnEMACStatsPortId,
       "tnEMACStatsInterval": tnEMACStatsInterval,
       "tnEMACStatsBin": tnEMACStatsBin,
       "tnEMACStatsBinStatus": tnEMACStatsBinStatus,
       "tnEMACStatsStartTime": tnEMACStatsStartTime,
       "tnEMACStatsTotalMembers": tnEMACStatsTotalMembers,
       "tnEMACStatsIfInOctets": tnEMACStatsIfInOctets,
       "tnEMACStatsIfInUcastPkts": tnEMACStatsIfInUcastPkts,
       "tnEMACStatsIfInDiscards": tnEMACStatsIfInDiscards,
       "tnEMACStatsIfInErrors": tnEMACStatsIfInErrors,
       "tnEMACStatsIfInUnknownProtos": tnEMACStatsIfInUnknownProtos,
       "tnEMACStatsIfInMulticastPkts": tnEMACStatsIfInMulticastPkts,
       "tnEMACStatsIfInBroadcastPkts": tnEMACStatsIfInBroadcastPkts,
       "tnEMACStatsIfOutOctets": tnEMACStatsIfOutOctets,
       "tnEMACStatsIfOutUcastPkts": tnEMACStatsIfOutUcastPkts,
       "tnEMACStatsIfOutDiscards": tnEMACStatsIfOutDiscards,
       "tnEMACStatsIfOutErrors": tnEMACStatsIfOutErrors,
       "tnEMACStatsIfOutMulticastPkts": tnEMACStatsIfOutMulticastPkts,
       "tnEMACStatsIfOutBroadcastPkts": tnEMACStatsIfOutBroadcastPkts,
       "tnEMACStatsIfInPkts": tnEMACStatsIfInPkts,
       "tnEMACStatsIfOutPkts": tnEMACStatsIfOutPkts,
       "tnEMACStatsDropEvents": tnEMACStatsDropEvents,
       "tnEMACStatsBroadcastPkts": tnEMACStatsBroadcastPkts,
       "tnEMACStatsMulticastPkts": tnEMACStatsMulticastPkts,
       "tnEMACStatsCRCAlignErrors": tnEMACStatsCRCAlignErrors,
       "tnEMACStatsUndersizePkts": tnEMACStatsUndersizePkts,
       "tnEMACStatsOversizePkts": tnEMACStatsOversizePkts,
       "tnEMACStatsFragments": tnEMACStatsFragments,
       "tnEMACStatsJabbers": tnEMACStatsJabbers,
       "tnEMACStatsCollisions": tnEMACStatsCollisions,
       "tnEMACStatsHighCapacityPkts": tnEMACStatsHighCapacityPkts,
       "tnEMACStatsHighCapacityOctets": tnEMACStatsHighCapacityOctets,
       "tnEMACStatsHighCapacityPkts64Octets": tnEMACStatsHighCapacityPkts64Octets,
       "tnEMACStatsHighCapacityPkts65to127Octets": tnEMACStatsHighCapacityPkts65to127Octets,
       "tnEMACStatsHighCapacityPkts128to255Octets": tnEMACStatsHighCapacityPkts128to255Octets,
       "tnEMACStatsHighCapacityPkts256to511Octets": tnEMACStatsHighCapacityPkts256to511Octets,
       "tnEMACStatsHighCapacityPkts512to1023Octets": tnEMACStatsHighCapacityPkts512to1023Octets,
       "tnEMACStatsHighCapacityPkts1024to1518Octets": tnEMACStatsHighCapacityPkts1024to1518Octets,
       "tnEMACStatsHighCapacityPkts1519toMaxOctets": tnEMACStatsHighCapacityPkts1519toMaxOctets,
       "tnPMACStatsAttributeTotal": tnPMACStatsAttributeTotal,
       "tnPMACStatsTable": tnPMACStatsTable,
       "tnPMACStatsEntry": tnPMACStatsEntry,
       "tnPMACStatsPortId": tnPMACStatsPortId,
       "tnPMACStatsInterval": tnPMACStatsInterval,
       "tnPMACStatsBin": tnPMACStatsBin,
       "tnPMACStatsBinStatus": tnPMACStatsBinStatus,
       "tnPMACStatsStartTime": tnPMACStatsStartTime,
       "tnPMACStatsTotalMembers": tnPMACStatsTotalMembers,
       "tnPMACStatsIfInOctets": tnPMACStatsIfInOctets,
       "tnPMACStatsIfInUcastPkts": tnPMACStatsIfInUcastPkts,
       "tnPMACStatsIfInDiscards": tnPMACStatsIfInDiscards,
       "tnPMACStatsIfInErrors": tnPMACStatsIfInErrors,
       "tnPMACStatsIfInUnknownProtos": tnPMACStatsIfInUnknownProtos,
       "tnPMACStatsIfInMulticastPkts": tnPMACStatsIfInMulticastPkts,
       "tnPMACStatsIfInBroadcastPkts": tnPMACStatsIfInBroadcastPkts,
       "tnPMACStatsIfOutOctets": tnPMACStatsIfOutOctets,
       "tnPMACStatsIfOutUcastPkts": tnPMACStatsIfOutUcastPkts,
       "tnPMACStatsIfOutDiscards": tnPMACStatsIfOutDiscards,
       "tnPMACStatsIfOutErrors": tnPMACStatsIfOutErrors,
       "tnPMACStatsIfOutMulticastPkts": tnPMACStatsIfOutMulticastPkts,
       "tnPMACStatsIfOutBroadcastPkts": tnPMACStatsIfOutBroadcastPkts,
       "tnPMACStatsIfInPkts": tnPMACStatsIfInPkts,
       "tnPMACStatsIfOutPkts": tnPMACStatsIfOutPkts,
       "tnPMACStatsDropEvents": tnPMACStatsDropEvents,
       "tnPMACStatsBroadcastPkts": tnPMACStatsBroadcastPkts,
       "tnPMACStatsMulticastPkts": tnPMACStatsMulticastPkts,
       "tnPMACStatsCRCAlignErrors": tnPMACStatsCRCAlignErrors,
       "tnPMACStatsUndersizePkts": tnPMACStatsUndersizePkts,
       "tnPMACStatsOversizePkts": tnPMACStatsOversizePkts,
       "tnPMACStatsFragments": tnPMACStatsFragments,
       "tnPMACStatsJabbers": tnPMACStatsJabbers,
       "tnPMACStatsCollisions": tnPMACStatsCollisions,
       "tnPMACStatsHighCapacityPkts": tnPMACStatsHighCapacityPkts,
       "tnPMACStatsHighCapacityOctets": tnPMACStatsHighCapacityOctets,
       "tnPMACStatsHighCapacityPkts64Octets": tnPMACStatsHighCapacityPkts64Octets,
       "tnPMACStatsHighCapacityPkts65to127Octets": tnPMACStatsHighCapacityPkts65to127Octets,
       "tnPMACStatsHighCapacityPkts128to255Octets": tnPMACStatsHighCapacityPkts128to255Octets,
       "tnPMACStatsHighCapacityPkts256to511Octets": tnPMACStatsHighCapacityPkts256to511Octets,
       "tnPMACStatsHighCapacityPkts512to1023Octets": tnPMACStatsHighCapacityPkts512to1023Octets,
       "tnPMACStatsHighCapacityPkts1024to1518Octets": tnPMACStatsHighCapacityPkts1024to1518Octets,
       "tnPMACStatsHighCapacityPkts1519toMaxOctets": tnPMACStatsHighCapacityPkts1519toMaxOctets,
       "tnMMACStatsAttributeTotal": tnMMACStatsAttributeTotal,
       "tnMMACStatsTable": tnMMACStatsTable,
       "tnMMACStatsEntry": tnMMACStatsEntry,
       "tnMMACStatsPortId": tnMMACStatsPortId,
       "tnMMACStatsInterval": tnMMACStatsInterval,
       "tnMMACStatsBin": tnMMACStatsBin,
       "tnMMACStatsBinStatus": tnMMACStatsBinStatus,
       "tnMMACStatsStartTime": tnMMACStatsStartTime,
       "tnMMACStatsTotalMembers": tnMMACStatsTotalMembers,
       "tnMMACStatsFrameAssErrorCount": tnMMACStatsFrameAssErrorCount,
       "tnMMACStatsFrameSmdErrorCount": tnMMACStatsFrameSmdErrorCount,
       "tnMMACStatsFrameAssOkCount": tnMMACStatsFrameAssOkCount,
       "tnMMACStatsFragCountRx": tnMMACStatsFragCountRx,
       "tnMMACStatsFragCountTx": tnMMACStatsFragCountTx,
       "tnMMACStatsHoldCount": tnMMACStatsHoldCount,
       "tnRoeMapperRawCountStatsAttributeTotal": tnRoeMapperRawCountStatsAttributeTotal,
       "tnRoeMapperRawCountStatsTable": tnRoeMapperRawCountStatsTable,
       "tnRoeMapperRawCountStatsEntry": tnRoeMapperRawCountStatsEntry,
       "tnRoeMapperRawCountStatsPortId": tnRoeMapperRawCountStatsPortId,
       "tnRoeMapperRawStatsMapperID": tnRoeMapperRawStatsMapperID,
       "tnRoeMapperRawCountStatsClear": tnRoeMapperRawCountStatsClear,
       "tnRoeMapperRawCountStatsStartTime": tnRoeMapperRawCountStatsStartTime,
       "tnRoeMapperRawCountStatsInPackets": tnRoeMapperRawCountStatsInPackets,
       "tnRoeMapperRawTxpackets": tnRoeMapperRawTxpackets,
       "tnRoeMapperRawTxbytes": tnRoeMapperRawTxbytes,
       "tnRoeMapperRawTxDropPackets": tnRoeMapperRawTxDropPackets,
       "tnRoeMapperRawEncapQueueOverrun": tnRoeMapperRawEncapQueueOverrun,
       "tnRoeMapperRawGSMTimeSlotMismatch": tnRoeMapperRawGSMTimeSlotMismatch,
       "tnRoeDeMapperRawCountStatsAttributeTotal": tnRoeDeMapperRawCountStatsAttributeTotal,
       "tnRoeDeMapperRawCountStatsTable": tnRoeDeMapperRawCountStatsTable,
       "tnRoeDeMapperRawCountStatsEntry": tnRoeDeMapperRawCountStatsEntry,
       "tnRoeDeMapperRawCountStatsPortId": tnRoeDeMapperRawCountStatsPortId,
       "tnRoeDeMapperRawStatsDeMapperID": tnRoeDeMapperRawStatsDeMapperID,
       "tnRoeDeMapperRawCountStatsClear": tnRoeDeMapperRawCountStatsClear,
       "tnRoeDeMapperRawStatsStartTime": tnRoeDeMapperRawStatsStartTime,
       "tnRoeDeMapperRawRxpackets": tnRoeDeMapperRawRxpackets,
       "tnRoeDeMapperRawRxbytes": tnRoeDeMapperRawRxbytes,
       "tnRoeDeMapperRawDecapQueueOverrun": tnRoeDeMapperRawDecapQueueOverrun,
       "tnRoeDeMapperRawQueueUnderrun": tnRoeDeMapperRawQueueUnderrun,
       "tnRoeDeMapperRawDecapPacketMissing": tnRoeDeMapperRawDecapPacketMissing,
       "tnRoeDeMapperRawDecapPacketSizeMismatch": tnRoeDeMapperRawDecapPacketSizeMismatch,
       "tnRoeRawCountStatsAttributeTotal": tnRoeRawCountStatsAttributeTotal,
       "tnRoeRawCountStatsTable": tnRoeRawCountStatsTable,
       "tnRoeRawCountStatsEntry": tnRoeRawCountStatsEntry,
       "tnRoeRawStatsPortId": tnRoeRawStatsPortId,
       "tnRoeRawCountStatsClear": tnRoeRawCountStatsClear,
       "tnRoeRawStatsStartTime": tnRoeRawStatsStartTime,
       "tnRoeRawDecapPktsDropped": tnRoeRawDecapPktsDropped}
)
