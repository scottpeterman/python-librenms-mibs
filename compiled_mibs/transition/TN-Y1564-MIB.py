# SNMP MIB module (TN-Y1564-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-Y1564-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:39 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnY1564MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154)
)
if mibBuilder.loadTexts:
    tnY1564MIB.setRevisions(
        ("2014-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnY1564MIBNotifications_ObjectIdentity = ObjectIdentity
tnY1564MIBNotifications = _TnY1564MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 1)
)
_TnY1564MIBObjects_ObjectIdentity = ObjectIdentity
tnY1564MIBObjects = _TnY1564MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2)
)
_TnY1564CfgMgmt_ObjectIdentity = ObjectIdentity
tnY1564CfgMgmt = _TnY1564CfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1)
)
_TnY1564ProfileTable_Object = MibTable
tnY1564ProfileTable = _TnY1564ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnY1564ProfileTable.setStatus("current")
_TnY1564ProfileEntry_Object = MibTableRow
tnY1564ProfileEntry = _TnY1564ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1)
)
tnY1564ProfileEntry.setIndexNames(
    (1, "TN-Y1564-MIB", "tnY1564ProfileName"),
)
if mibBuilder.loadTexts:
    tnY1564ProfileEntry.setStatus("current")
_TnY1564ProfileName_Type = SnmpAdminString
_TnY1564ProfileName_Object = MibTableColumn
tnY1564ProfileName = _TnY1564ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 1),
    _TnY1564ProfileName_Type()
)
tnY1564ProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnY1564ProfileName.setStatus("current")


class _TnY1564ProfileDescription_Type(DisplayString):
    """Custom type tnY1564ProfileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnY1564ProfileDescription_Type.__name__ = "DisplayString"
_TnY1564ProfileDescription_Object = MibTableColumn
tnY1564ProfileDescription = _TnY1564ProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 2),
    _TnY1564ProfileDescription_Type()
)
tnY1564ProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564ProfileDescription.setStatus("current")
_TnY1564DuelEnded_Type = TruthValue
_TnY1564DuelEnded_Object = MibTableColumn
tnY1564DuelEnded = _TnY1564DuelEnded_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 3),
    _TnY1564DuelEnded_Type()
)
tnY1564DuelEnded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564DuelEnded.setStatus("current")
_TnY1564DstOamAware_Type = TruthValue
_TnY1564DstOamAware_Object = MibTableColumn
tnY1564DstOamAware = _TnY1564DstOamAware_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 4),
    _TnY1564DstOamAware_Type()
)
tnY1564DstOamAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564DstOamAware.setStatus("current")


class _TnY1564TrafficType_Type(Integer32):
    """Custom type tnY1564TrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("y1731Oam", 1),
          ("simCustomer", 2))
    )


_TnY1564TrafficType_Type.__name__ = "Integer32"
_TnY1564TrafficType_Object = MibTableColumn
tnY1564TrafficType = _TnY1564TrafficType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 5),
    _TnY1564TrafficType_Type()
)
tnY1564TrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564TrafficType.setStatus("current")


class _TnY1564MegLevel_Type(Integer32):
    """Custom type tnY1564MegLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2),
          ("three", 3),
          ("four", 4),
          ("five", 5),
          ("six", 6),
          ("seven", 7))
    )


_TnY1564MegLevel_Type.__name__ = "Integer32"
_TnY1564MegLevel_Object = MibTableColumn
tnY1564MegLevel = _TnY1564MegLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 6),
    _TnY1564MegLevel_Type()
)
tnY1564MegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564MegLevel.setStatus("current")


class _TnY1564FrameSize_Type(Integer32):
    """Custom type tnY1564FrameSize based on Integer32"""
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
        *(("bytes64", 1),
          ("bytes128", 2),
          ("bytes256", 3),
          ("bytes512", 4),
          ("bytes1024", 5),
          ("bytes1280", 6),
          ("bytes1518", 7),
          ("mtu", 8),
          ("userDefined", 9))
    )


_TnY1564FrameSize_Type.__name__ = "Integer32"
_TnY1564FrameSize_Object = MibTableColumn
tnY1564FrameSize = _TnY1564FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 7),
    _TnY1564FrameSize_Type()
)
tnY1564FrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564FrameSize.setStatus("current")


class _TnY1564UserFrameSize_Type(Integer32):
    """Custom type tnY1564UserFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10236),
    )


_TnY1564UserFrameSize_Type.__name__ = "Integer32"
_TnY1564UserFrameSize_Object = MibTableColumn
tnY1564UserFrameSize = _TnY1564UserFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 8),
    _TnY1564UserFrameSize_Type()
)
tnY1564UserFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564UserFrameSize.setStatus("current")
_TnY1564DwellTime_Type = Integer32
_TnY1564DwellTime_Object = MibTableColumn
tnY1564DwellTime = _TnY1564DwellTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 9),
    _TnY1564DwellTime_Type()
)
tnY1564DwellTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564DwellTime.setStatus("current")


class _TnY1564SacFLR_Type(Integer32):
    """Custom type tnY1564SacFLR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TnY1564SacFLR_Type.__name__ = "Integer32"
_TnY1564SacFLR_Object = MibTableColumn
tnY1564SacFLR = _TnY1564SacFLR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 10),
    _TnY1564SacFLR_Type()
)
tnY1564SacFLR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564SacFLR.setStatus("current")


class _TnY1564SacFTD_Type(Integer32):
    """Custom type tnY1564SacFTD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnY1564SacFTD_Type.__name__ = "Integer32"
_TnY1564SacFTD_Object = MibTableColumn
tnY1564SacFTD = _TnY1564SacFTD_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 11),
    _TnY1564SacFTD_Type()
)
tnY1564SacFTD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564SacFTD.setStatus("current")


class _TnY1564SacFDV_Type(Integer32):
    """Custom type tnY1564SacFDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnY1564SacFDV_Type.__name__ = "Integer32"
_TnY1564SacFDV_Object = MibTableColumn
tnY1564SacFDV = _TnY1564SacFDV_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 12),
    _TnY1564SacFDV_Type()
)
tnY1564SacFDV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564SacFDV.setStatus("current")
_TnY1564CirEnable_Type = TruthValue
_TnY1564CirEnable_Object = MibTableColumn
tnY1564CirEnable = _TnY1564CirEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 13),
    _TnY1564CirEnable_Type()
)
tnY1564CirEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564CirEnable.setStatus("current")


class _TnY1564CirStepDuration_Type(Integer32):
    """Custom type tnY1564CirStepDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TnY1564CirStepDuration_Type.__name__ = "Integer32"
_TnY1564CirStepDuration_Object = MibTableColumn
tnY1564CirStepDuration = _TnY1564CirStepDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 14),
    _TnY1564CirStepDuration_Type()
)
tnY1564CirStepDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564CirStepDuration.setStatus("current")


class _TnY1564CirDmInterval_Type(Integer32):
    """Custom type tnY1564CirDmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_TnY1564CirDmInterval_Type.__name__ = "Integer32"
_TnY1564CirDmInterval_Object = MibTableColumn
tnY1564CirDmInterval = _TnY1564CirDmInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 15),
    _TnY1564CirDmInterval_Type()
)
tnY1564CirDmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564CirDmInterval.setStatus("current")


class _TnY1564CirStepCount_Type(Integer32):
    """Custom type tnY1564CirStepCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnY1564CirStepCount_Type.__name__ = "Integer32"
_TnY1564CirStepCount_Object = MibTableColumn
tnY1564CirStepCount = _TnY1564CirStepCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 16),
    _TnY1564CirStepCount_Type()
)
tnY1564CirStepCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564CirStepCount.setStatus("current")
_TnY1564EirEnable_Type = TruthValue
_TnY1564EirEnable_Object = MibTableColumn
tnY1564EirEnable = _TnY1564EirEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 17),
    _TnY1564EirEnable_Type()
)
tnY1564EirEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564EirEnable.setStatus("current")


class _TnY1564EirDuration_Type(Integer32):
    """Custom type tnY1564EirDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TnY1564EirDuration_Type.__name__ = "Integer32"
_TnY1564EirDuration_Object = MibTableColumn
tnY1564EirDuration = _TnY1564EirDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 18),
    _TnY1564EirDuration_Type()
)
tnY1564EirDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564EirDuration.setStatus("current")


class _TnY1564EirDmInterval_Type(Integer32):
    """Custom type tnY1564EirDmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_TnY1564EirDmInterval_Type.__name__ = "Integer32"
_TnY1564EirDmInterval_Object = MibTableColumn
tnY1564EirDmInterval = _TnY1564EirDmInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 19),
    _TnY1564EirDmInterval_Type()
)
tnY1564EirDmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564EirDmInterval.setStatus("current")
_TnY1564TrafficPolicingEnable_Type = TruthValue
_TnY1564TrafficPolicingEnable_Object = MibTableColumn
tnY1564TrafficPolicingEnable = _TnY1564TrafficPolicingEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 20),
    _TnY1564TrafficPolicingEnable_Type()
)
tnY1564TrafficPolicingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564TrafficPolicingEnable.setStatus("current")


class _TnY1564TrafficPolicingDuration_Type(Integer32):
    """Custom type tnY1564TrafficPolicingDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TnY1564TrafficPolicingDuration_Type.__name__ = "Integer32"
_TnY1564TrafficPolicingDuration_Object = MibTableColumn
tnY1564TrafficPolicingDuration = _TnY1564TrafficPolicingDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 21),
    _TnY1564TrafficPolicingDuration_Type()
)
tnY1564TrafficPolicingDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564TrafficPolicingDuration.setStatus("current")


class _TnY1564TrafficPolicingDmInterval_Type(Integer32):
    """Custom type tnY1564TrafficPolicingDmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_TnY1564TrafficPolicingDmInterval_Type.__name__ = "Integer32"
_TnY1564TrafficPolicingDmInterval_Object = MibTableColumn
tnY1564TrafficPolicingDmInterval = _TnY1564TrafficPolicingDmInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 22),
    _TnY1564TrafficPolicingDmInterval_Type()
)
tnY1564TrafficPolicingDmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564TrafficPolicingDmInterval.setStatus("current")
_TnY1564PerfTestEnable_Type = TruthValue
_TnY1564PerfTestEnable_Object = MibTableColumn
tnY1564PerfTestEnable = _TnY1564PerfTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 23),
    _TnY1564PerfTestEnable_Type()
)
tnY1564PerfTestEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564PerfTestEnable.setStatus("current")


class _TnY1564PerfTestDuration_Type(Integer32):
    """Custom type tnY1564PerfTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mins15", 1),
          ("hours2", 2),
          ("hours24", 3),
          ("userDefined", 4))
    )


_TnY1564PerfTestDuration_Type.__name__ = "Integer32"
_TnY1564PerfTestDuration_Object = MibTableColumn
tnY1564PerfTestDuration = _TnY1564PerfTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 24),
    _TnY1564PerfTestDuration_Type()
)
tnY1564PerfTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564PerfTestDuration.setStatus("current")


class _TnY1564PerfTestUserDuration_Type(Integer32):
    """Custom type tnY1564PerfTestUserDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_TnY1564PerfTestUserDuration_Type.__name__ = "Integer32"
_TnY1564PerfTestUserDuration_Object = MibTableColumn
tnY1564PerfTestUserDuration = _TnY1564PerfTestUserDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 25),
    _TnY1564PerfTestUserDuration_Type()
)
tnY1564PerfTestUserDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564PerfTestUserDuration.setStatus("current")


class _TnY1564PerfTestDmInterval_Type(Integer32):
    """Custom type tnY1564PerfTestDmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_TnY1564PerfTestDmInterval_Type.__name__ = "Integer32"
_TnY1564PerfTestDmInterval_Object = MibTableColumn
tnY1564PerfTestDmInterval = _TnY1564PerfTestDmInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 26),
    _TnY1564PerfTestDmInterval_Type()
)
tnY1564PerfTestDmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564PerfTestDmInterval.setStatus("current")
_TnY1564ProfileStatus_Type = RowStatus
_TnY1564ProfileStatus_Object = MibTableColumn
tnY1564ProfileStatus = _TnY1564ProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 1, 1, 1, 27),
    _TnY1564ProfileStatus_Type()
)
tnY1564ProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnY1564ProfileStatus.setStatus("current")
_TnY1564ReportMgmt_ObjectIdentity = ObjectIdentity
tnY1564ReportMgmt = _TnY1564ReportMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2)
)
_TnY1564ReportTable_Object = MibTable
tnY1564ReportTable = _TnY1564ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnY1564ReportTable.setStatus("current")
_TnY1564ReportEntry_Object = MibTableRow
tnY1564ReportEntry = _TnY1564ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1)
)
tnY1564ReportEntry.setIndexNames(
    (1, "TN-Y1564-MIB", "tnY1564ReportName"),
)
if mibBuilder.loadTexts:
    tnY1564ReportEntry.setStatus("current")
_TnY1564ReportName_Type = SnmpAdminString
_TnY1564ReportName_Object = MibTableColumn
tnY1564ReportName = _TnY1564ReportName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1, 1),
    _TnY1564ReportName_Type()
)
tnY1564ReportName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnY1564ReportName.setStatus("current")


class _TnY1564ReportDscr_Type(DisplayString):
    """Custom type tnY1564ReportDscr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnY1564ReportDscr_Type.__name__ = "DisplayString"
_TnY1564ReportDscr_Object = MibTableColumn
tnY1564ReportDscr = _TnY1564ReportDscr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1, 2),
    _TnY1564ReportDscr_Type()
)
tnY1564ReportDscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnY1564ReportDscr.setStatus("current")


class _TnY1564ReportTime_Type(DisplayString):
    """Custom type tnY1564ReportTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )
    fixed_length = 26


_TnY1564ReportTime_Type.__name__ = "DisplayString"
_TnY1564ReportTime_Object = MibTableColumn
tnY1564ReportTime = _TnY1564ReportTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1, 3),
    _TnY1564ReportTime_Type()
)
tnY1564ReportTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnY1564ReportTime.setStatus("current")
_TnY1564ReportTftpAddrType_Type = InetAddressType
_TnY1564ReportTftpAddrType_Object = MibTableColumn
tnY1564ReportTftpAddrType = _TnY1564ReportTftpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1, 4),
    _TnY1564ReportTftpAddrType_Type()
)
tnY1564ReportTftpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnY1564ReportTftpAddrType.setStatus("current")
_TnY1564ReportTftpAddr_Type = InetAddress
_TnY1564ReportTftpAddr_Object = MibTableColumn
tnY1564ReportTftpAddr = _TnY1564ReportTftpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1, 5),
    _TnY1564ReportTftpAddr_Type()
)
tnY1564ReportTftpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnY1564ReportTftpAddr.setStatus("current")


class _TnY1564ReportTestStatus_Type(Integer32):
    """Custom type tnY1564ReportTestStatus based on Integer32"""
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
        *(("inactive", 1),
          ("executing", 2),
          ("cancelling", 3),
          ("cancelled", 4),
          ("passed", 5),
          ("failed", 6))
    )


_TnY1564ReportTestStatus_Type.__name__ = "Integer32"
_TnY1564ReportTestStatus_Object = MibTableColumn
tnY1564ReportTestStatus = _TnY1564ReportTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1, 6),
    _TnY1564ReportTestStatus_Type()
)
tnY1564ReportTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnY1564ReportTestStatus.setStatus("current")


class _TnY1564ReportAction_Type(Integer32):
    """Custom type tnY1564ReportAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("cancelTest", 2),
          ("saveReport", 3),
          ("deleteReport", 4))
    )


_TnY1564ReportAction_Type.__name__ = "Integer32"
_TnY1564ReportAction_Object = MibTableColumn
tnY1564ReportAction = _TnY1564ReportAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 2, 2, 1, 1, 7),
    _TnY1564ReportAction_Type()
)
tnY1564ReportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnY1564ReportAction.setStatus("current")
_TnY1564MIBConformance_ObjectIdentity = ObjectIdentity
tnY1564MIBConformance = _TnY1564MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 154, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-Y1564-MIB",
    **{"tnY1564MIB": tnY1564MIB,
       "tnY1564MIBNotifications": tnY1564MIBNotifications,
       "tnY1564MIBObjects": tnY1564MIBObjects,
       "tnY1564CfgMgmt": tnY1564CfgMgmt,
       "tnY1564ProfileTable": tnY1564ProfileTable,
       "tnY1564ProfileEntry": tnY1564ProfileEntry,
       "tnY1564ProfileName": tnY1564ProfileName,
       "tnY1564ProfileDescription": tnY1564ProfileDescription,
       "tnY1564DuelEnded": tnY1564DuelEnded,
       "tnY1564DstOamAware": tnY1564DstOamAware,
       "tnY1564TrafficType": tnY1564TrafficType,
       "tnY1564MegLevel": tnY1564MegLevel,
       "tnY1564FrameSize": tnY1564FrameSize,
       "tnY1564UserFrameSize": tnY1564UserFrameSize,
       "tnY1564DwellTime": tnY1564DwellTime,
       "tnY1564SacFLR": tnY1564SacFLR,
       "tnY1564SacFTD": tnY1564SacFTD,
       "tnY1564SacFDV": tnY1564SacFDV,
       "tnY1564CirEnable": tnY1564CirEnable,
       "tnY1564CirStepDuration": tnY1564CirStepDuration,
       "tnY1564CirDmInterval": tnY1564CirDmInterval,
       "tnY1564CirStepCount": tnY1564CirStepCount,
       "tnY1564EirEnable": tnY1564EirEnable,
       "tnY1564EirDuration": tnY1564EirDuration,
       "tnY1564EirDmInterval": tnY1564EirDmInterval,
       "tnY1564TrafficPolicingEnable": tnY1564TrafficPolicingEnable,
       "tnY1564TrafficPolicingDuration": tnY1564TrafficPolicingDuration,
       "tnY1564TrafficPolicingDmInterval": tnY1564TrafficPolicingDmInterval,
       "tnY1564PerfTestEnable": tnY1564PerfTestEnable,
       "tnY1564PerfTestDuration": tnY1564PerfTestDuration,
       "tnY1564PerfTestUserDuration": tnY1564PerfTestUserDuration,
       "tnY1564PerfTestDmInterval": tnY1564PerfTestDmInterval,
       "tnY1564ProfileStatus": tnY1564ProfileStatus,
       "tnY1564ReportMgmt": tnY1564ReportMgmt,
       "tnY1564ReportTable": tnY1564ReportTable,
       "tnY1564ReportEntry": tnY1564ReportEntry,
       "tnY1564ReportName": tnY1564ReportName,
       "tnY1564ReportDscr": tnY1564ReportDscr,
       "tnY1564ReportTime": tnY1564ReportTime,
       "tnY1564ReportTftpAddrType": tnY1564ReportTftpAddrType,
       "tnY1564ReportTftpAddr": tnY1564ReportTftpAddr,
       "tnY1564ReportTestStatus": tnY1564ReportTestStatus,
       "tnY1564ReportAction": tnY1564ReportAction,
       "tnY1564MIBConformance": tnY1564MIBConformance}
)
