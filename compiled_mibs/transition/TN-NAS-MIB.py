# SNMP MIB module (TN-NAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-NAS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:06 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

tnNASMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125)
)
if mibBuilder.loadTexts:
    tnNASMIB.setRevisions(
        ("2012-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnNASAdminStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("forceAuthorized", 1),
          ("portBased802dot1x", 2),
          ("forceUnauthorized", 3),
          ("macBasedAuth", 4),
          ("single802dot1x", 5),
          ("multi802dot1x", 6))
    )



# MIB Managed Objects in the order of their OIDs

_TnNASMIBNotifications_ObjectIdentity = ObjectIdentity
tnNASMIBNotifications = _TnNASMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 0)
)
_TnNASMIBObjects_ObjectIdentity = ObjectIdentity
tnNASMIBObjects = _TnNASMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1)
)
_TnNASSysMgmt_ObjectIdentity = ObjectIdentity
tnNASSysMgmt = _TnNASSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1)
)


class _TnNASSysReAuthEnabled_Type(Integer32):
    """Custom type tnNASSysReAuthEnabled based on Integer32"""
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


_TnNASSysReAuthEnabled_Type.__name__ = "Integer32"
_TnNASSysReAuthEnabled_Object = MibScalar
tnNASSysReAuthEnabled = _TnNASSysReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 1),
    _TnNASSysReAuthEnabled_Type()
)
tnNASSysReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysReAuthEnabled.setStatus("current")


class _TnNASSysReAuthPeriod_Type(Integer32):
    """Custom type tnNASSysReAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TnNASSysReAuthPeriod_Type.__name__ = "Integer32"
_TnNASSysReAuthPeriod_Object = MibScalar
tnNASSysReAuthPeriod = _TnNASSysReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 2),
    _TnNASSysReAuthPeriod_Type()
)
tnNASSysReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysReAuthPeriod.setStatus("current")


class _TnNASSysEAPOLTimeout_Type(Integer32):
    """Custom type tnNASSysEAPOLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNASSysEAPOLTimeout_Type.__name__ = "Integer32"
_TnNASSysEAPOLTimeout_Object = MibScalar
tnNASSysEAPOLTimeout = _TnNASSysEAPOLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 3),
    _TnNASSysEAPOLTimeout_Type()
)
tnNASSysEAPOLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysEAPOLTimeout.setStatus("current")


class _TnNASSysAgingPeriod_Type(Unsigned32):
    """Custom type tnNASSysAgingPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_TnNASSysAgingPeriod_Type.__name__ = "Unsigned32"
_TnNASSysAgingPeriod_Object = MibScalar
tnNASSysAgingPeriod = _TnNASSysAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 4),
    _TnNASSysAgingPeriod_Type()
)
tnNASSysAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysAgingPeriod.setStatus("current")


class _TnNASSysHoldTime_Type(Unsigned32):
    """Custom type tnNASSysHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_TnNASSysHoldTime_Type.__name__ = "Unsigned32"
_TnNASSysHoldTime_Object = MibScalar
tnNASSysHoldTime = _TnNASSysHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 5),
    _TnNASSysHoldTime_Type()
)
tnNASSysHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysHoldTime.setStatus("current")


class _TnNASSysRadiusAssignedQosEnable_Type(Integer32):
    """Custom type tnNASSysRadiusAssignedQosEnable based on Integer32"""
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


_TnNASSysRadiusAssignedQosEnable_Type.__name__ = "Integer32"
_TnNASSysRadiusAssignedQosEnable_Object = MibScalar
tnNASSysRadiusAssignedQosEnable = _TnNASSysRadiusAssignedQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 6),
    _TnNASSysRadiusAssignedQosEnable_Type()
)
tnNASSysRadiusAssignedQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysRadiusAssignedQosEnable.setStatus("current")


class _TnNASSysRadiusAssignedVlanEnable_Type(Integer32):
    """Custom type tnNASSysRadiusAssignedVlanEnable based on Integer32"""
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


_TnNASSysRadiusAssignedVlanEnable_Type.__name__ = "Integer32"
_TnNASSysRadiusAssignedVlanEnable_Object = MibScalar
tnNASSysRadiusAssignedVlanEnable = _TnNASSysRadiusAssignedVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 7),
    _TnNASSysRadiusAssignedVlanEnable_Type()
)
tnNASSysRadiusAssignedVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysRadiusAssignedVlanEnable.setStatus("current")


class _TnNASSysGuestVlanEnable_Type(Integer32):
    """Custom type tnNASSysGuestVlanEnable based on Integer32"""
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


_TnNASSysGuestVlanEnable_Type.__name__ = "Integer32"
_TnNASSysGuestVlanEnable_Object = MibScalar
tnNASSysGuestVlanEnable = _TnNASSysGuestVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 8),
    _TnNASSysGuestVlanEnable_Type()
)
tnNASSysGuestVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysGuestVlanEnable.setStatus("current")
_TnNASSysGuestVlanId_Type = VlanId
_TnNASSysGuestVlanId_Object = MibScalar
tnNASSysGuestVlanId = _TnNASSysGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 9),
    _TnNASSysGuestVlanId_Type()
)
tnNASSysGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysGuestVlanId.setStatus("current")


class _TnNASSysMaxReAuthCount_Type(Integer32):
    """Custom type tnNASSysMaxReAuthCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnNASSysMaxReAuthCount_Type.__name__ = "Integer32"
_TnNASSysMaxReAuthCount_Object = MibScalar
tnNASSysMaxReAuthCount = _TnNASSysMaxReAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 10),
    _TnNASSysMaxReAuthCount_Type()
)
tnNASSysMaxReAuthCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysMaxReAuthCount.setStatus("current")


class _TnNASSysAllowGuestVlanIFEAPOLSeen_Type(Integer32):
    """Custom type tnNASSysAllowGuestVlanIFEAPOLSeen based on Integer32"""
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


_TnNASSysAllowGuestVlanIFEAPOLSeen_Type.__name__ = "Integer32"
_TnNASSysAllowGuestVlanIFEAPOLSeen_Object = MibScalar
tnNASSysAllowGuestVlanIFEAPOLSeen = _TnNASSysAllowGuestVlanIFEAPOLSeen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 1, 11),
    _TnNASSysAllowGuestVlanIFEAPOLSeen_Type()
)
tnNASSysAllowGuestVlanIFEAPOLSeen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSysAllowGuestVlanIFEAPOLSeen.setStatus("current")
_TnNASPortMgmt_ObjectIdentity = ObjectIdentity
tnNASPortMgmt = _TnNASPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2)
)
_TnNASPortCfgTable_Object = MibTable
tnNASPortCfgTable = _TnNASPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnNASPortCfgTable.setStatus("current")
_TnNASPortCfgEntry_Object = MibTableRow
tnNASPortCfgEntry = _TnNASPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1, 1)
)
tnNASPortCfgEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
)
if mibBuilder.loadTexts:
    tnNASPortCfgEntry.setStatus("current")
_TnNASPortNum_Type = Unsigned32
_TnNASPortNum_Object = MibTableColumn
tnNASPortNum = _TnNASPortNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1, 1, 1),
    _TnNASPortNum_Type()
)
tnNASPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNASPortNum.setStatus("current")
_TnNASAdminState_Type = TnNASAdminStateType
_TnNASAdminState_Object = MibTableColumn
tnNASAdminState = _TnNASAdminState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1, 1, 2),
    _TnNASAdminState_Type()
)
tnNASAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASAdminState.setStatus("current")


class _TnNASRadiusAssignedQosEnabled_Type(Integer32):
    """Custom type tnNASRadiusAssignedQosEnabled based on Integer32"""
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


_TnNASRadiusAssignedQosEnabled_Type.__name__ = "Integer32"
_TnNASRadiusAssignedQosEnabled_Object = MibTableColumn
tnNASRadiusAssignedQosEnabled = _TnNASRadiusAssignedQosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1, 1, 3),
    _TnNASRadiusAssignedQosEnabled_Type()
)
tnNASRadiusAssignedQosEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASRadiusAssignedQosEnabled.setStatus("current")


class _TnNASRadiusAssignedVlanEnabled_Type(Integer32):
    """Custom type tnNASRadiusAssignedVlanEnabled based on Integer32"""
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


_TnNASRadiusAssignedVlanEnabled_Type.__name__ = "Integer32"
_TnNASRadiusAssignedVlanEnabled_Object = MibTableColumn
tnNASRadiusAssignedVlanEnabled = _TnNASRadiusAssignedVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1, 1, 4),
    _TnNASRadiusAssignedVlanEnabled_Type()
)
tnNASRadiusAssignedVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASRadiusAssignedVlanEnabled.setStatus("current")


class _TnNASGuestVlanEnabled_Type(Integer32):
    """Custom type tnNASGuestVlanEnabled based on Integer32"""
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


_TnNASGuestVlanEnabled_Type.__name__ = "Integer32"
_TnNASGuestVlanEnabled_Object = MibTableColumn
tnNASGuestVlanEnabled = _TnNASGuestVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1, 1, 5),
    _TnNASGuestVlanEnabled_Type()
)
tnNASGuestVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASGuestVlanEnabled.setStatus("current")


class _TnNASPortCfgState_Type(Integer32):
    """Custom type tnNASPortCfgState based on Integer32"""
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
        *(("linkDown", 0),
          ("authorized", 1),
          ("unauthorized", 2),
          ("globallyDisabled", 3),
          ("authOrUnauth", 4))
    )


_TnNASPortCfgState_Type.__name__ = "Integer32"
_TnNASPortCfgState_Object = MibTableColumn
tnNASPortCfgState = _TnNASPortCfgState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 2, 1, 1, 6),
    _TnNASPortCfgState_Type()
)
tnNASPortCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASPortCfgState.setStatus("current")
_TnNASAuthCountMgmt_ObjectIdentity = ObjectIdentity
tnNASAuthCountMgmt = _TnNASAuthCountMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 3)
)
_TnNASAuthCountTable_Object = MibTable
tnNASAuthCountTable = _TnNASAuthCountTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnNASAuthCountTable.setStatus("current")
_TnNASAuthCountEntry_Object = MibTableRow
tnNASAuthCountEntry = _TnNASAuthCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 3, 1, 1)
)
tnNASAuthCountEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
)
if mibBuilder.loadTexts:
    tnNASAuthCountEntry.setStatus("current")
_TnNASAuthCount_Type = Integer32
_TnNASAuthCount_Object = MibTableColumn
tnNASAuthCount = _TnNASAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 3, 1, 1, 1),
    _TnNASAuthCount_Type()
)
tnNASAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASAuthCount.setStatus("current")
_TnNASUnauthCount_Type = Integer32
_TnNASUnauthCount_Object = MibTableColumn
tnNASUnauthCount = _TnNASUnauthCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 3, 1, 1, 2),
    _TnNASUnauthCount_Type()
)
tnNASUnauthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASUnauthCount.setStatus("current")
_TnNASPortStatus_ObjectIdentity = ObjectIdentity
tnNASPortStatus = _TnNASPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 4)
)
_TnNASPortStatusTable_Object = MibTable
tnNASPortStatusTable = _TnNASPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnNASPortStatusTable.setStatus("current")
_TnNASPortStatusEntry_Object = MibTableRow
tnNASPortStatusEntry = _TnNASPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 4, 1, 1)
)
tnNASPortStatusEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
)
if mibBuilder.loadTexts:
    tnNASPortStatusEntry.setStatus("current")
_TnNASPortAdminState_Type = TnNASAdminStateType
_TnNASPortAdminState_Object = MibTableColumn
tnNASPortAdminState = _TnNASPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 4, 1, 1, 1),
    _TnNASPortAdminState_Type()
)
tnNASPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASPortAdminState.setStatus("current")


class _TnNASPortState_Type(Integer32):
    """Custom type tnNASPortState based on Integer32"""
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
        *(("linkDown", 0),
          ("authorized", 1),
          ("unauthorized", 2),
          ("globallyDisabled", 3),
          ("authOrUnauth", 4))
    )


_TnNASPortState_Type.__name__ = "Integer32"
_TnNASPortState_Object = MibTableColumn
tnNASPortState = _TnNASPortState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 4, 1, 1, 2),
    _TnNASPortState_Type()
)
tnNASPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASPortState.setStatus("current")
_TnNASQosClass_Type = OctetString
_TnNASQosClass_Object = MibTableColumn
tnNASQosClass = _TnNASQosClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 4, 1, 1, 3),
    _TnNASQosClass_Type()
)
tnNASQosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASQosClass.setStatus("current")
_TnNASPortVlanId_Type = VlanId
_TnNASPortVlanId_Object = MibTableColumn
tnNASPortVlanId = _TnNASPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 4, 1, 1, 4),
    _TnNASPortVlanId_Type()
)
tnNASPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASPortVlanId.setStatus("current")
_TnNASClientStatus_ObjectIdentity = ObjectIdentity
tnNASClientStatus = _TnNASClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 5)
)
_TnNASClientStatusTable_Object = MibTable
tnNASClientStatusTable = _TnNASClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnNASClientStatusTable.setStatus("current")
_TnNASClientStatusEntry_Object = MibTableRow
tnNASClientStatusEntry = _TnNASClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 5, 1, 1)
)
tnNASClientStatusEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
    (0, "TN-NAS-MIB", "tnNASClientNum"),
)
if mibBuilder.loadTexts:
    tnNASClientStatusEntry.setStatus("current")


class _TnNASClientNum_Type(Unsigned32):
    """Custom type tnNASClientNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TnNASClientNum_Type.__name__ = "Unsigned32"
_TnNASClientNum_Object = MibTableColumn
tnNASClientNum = _TnNASClientNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 5, 1, 1, 1),
    _TnNASClientNum_Type()
)
tnNASClientNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNASClientNum.setStatus("current")
_TnNASMacAddr_Type = MacAddress
_TnNASMacAddr_Object = MibTableColumn
tnNASMacAddr = _TnNASMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 5, 1, 1, 2),
    _TnNASMacAddr_Type()
)
tnNASMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASMacAddr.setStatus("current")
_TnNASVlanId_Type = VlanId
_TnNASVlanId_Object = MibTableColumn
tnNASVlanId = _TnNASVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 5, 1, 1, 3),
    _TnNASVlanId_Type()
)
tnNASVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASVlanId.setStatus("current")
_TnNASIdentify_Type = OctetString
_TnNASIdentify_Object = MibTableColumn
tnNASIdentify = _TnNASIdentify_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 5, 1, 1, 4),
    _TnNASIdentify_Type()
)
tnNASIdentify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASIdentify.setStatus("current")
_TnNASSelectedBackendServerCounter_ObjectIdentity = ObjectIdentity
tnNASSelectedBackendServerCounter = _TnNASSelectedBackendServerCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6)
)
_TnNASSelectedBackendServerCounterTable_Object = MibTable
tnNASSelectedBackendServerCounterTable = _TnNASSelectedBackendServerCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tnNASSelectedBackendServerCounterTable.setStatus("current")
_TnNASSelectedBackendServerCounterEntry_Object = MibTableRow
tnNASSelectedBackendServerCounterEntry = _TnNASSelectedBackendServerCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6, 1, 1)
)
tnNASSelectedBackendServerCounterEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
)
if mibBuilder.loadTexts:
    tnNASSelectedBackendServerCounterEntry.setStatus("current")
_TnNASRxAccessChallenges_Type = Gauge32
_TnNASRxAccessChallenges_Object = MibTableColumn
tnNASRxAccessChallenges = _TnNASRxAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6, 1, 1, 1),
    _TnNASRxAccessChallenges_Type()
)
tnNASRxAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxAccessChallenges.setStatus("current")
_TnNASRxOtherRequests_Type = Gauge32
_TnNASRxOtherRequests_Object = MibTableColumn
tnNASRxOtherRequests = _TnNASRxOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6, 1, 1, 2),
    _TnNASRxOtherRequests_Type()
)
tnNASRxOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxOtherRequests.setStatus("current")
_TnNASRxAuthSuccesses_Type = Gauge32
_TnNASRxAuthSuccesses_Object = MibTableColumn
tnNASRxAuthSuccesses = _TnNASRxAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6, 1, 1, 3),
    _TnNASRxAuthSuccesses_Type()
)
tnNASRxAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxAuthSuccesses.setStatus("current")
_TnNASRxAuthFailures_Type = Gauge32
_TnNASRxAuthFailures_Object = MibTableColumn
tnNASRxAuthFailures = _TnNASRxAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6, 1, 1, 4),
    _TnNASRxAuthFailures_Type()
)
tnNASRxAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxAuthFailures.setStatus("current")
_TnNASTxResponses_Type = Gauge32
_TnNASTxResponses_Object = MibTableColumn
tnNASTxResponses = _TnNASTxResponses_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 6, 1, 1, 5),
    _TnNASTxResponses_Type()
)
tnNASTxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASTxResponses.setStatus("current")
_TnNASSelectedEapolCounter_ObjectIdentity = ObjectIdentity
tnNASSelectedEapolCounter = _TnNASSelectedEapolCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7)
)
_TnNASSelectedEapolCounterTable_Object = MibTable
tnNASSelectedEapolCounterTable = _TnNASSelectedEapolCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tnNASSelectedEapolCounterTable.setStatus("current")
_TnNASSelectedEapolCounterEntry_Object = MibTableRow
tnNASSelectedEapolCounterEntry = _TnNASSelectedEapolCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1)
)
tnNASSelectedEapolCounterEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
)
if mibBuilder.loadTexts:
    tnNASSelectedEapolCounterEntry.setStatus("current")
_TnNASRxTotal_Type = Gauge32
_TnNASRxTotal_Object = MibTableColumn
tnNASRxTotal = _TnNASRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 1),
    _TnNASRxTotal_Type()
)
tnNASRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxTotal.setStatus("current")
_TnNASRxResponseId_Type = Gauge32
_TnNASRxResponseId_Object = MibTableColumn
tnNASRxResponseId = _TnNASRxResponseId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 2),
    _TnNASRxResponseId_Type()
)
tnNASRxResponseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxResponseId.setStatus("current")
_TnNASRxResponses_Type = Gauge32
_TnNASRxResponses_Object = MibTableColumn
tnNASRxResponses = _TnNASRxResponses_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 3),
    _TnNASRxResponses_Type()
)
tnNASRxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxResponses.setStatus("current")
_TnNASRxStart_Type = Gauge32
_TnNASRxStart_Object = MibTableColumn
tnNASRxStart = _TnNASRxStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 4),
    _TnNASRxStart_Type()
)
tnNASRxStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxStart.setStatus("current")
_TnNASRxLogoff_Type = Gauge32
_TnNASRxLogoff_Object = MibTableColumn
tnNASRxLogoff = _TnNASRxLogoff_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 5),
    _TnNASRxLogoff_Type()
)
tnNASRxLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxLogoff.setStatus("current")
_TnNASRxInvalidType_Type = Gauge32
_TnNASRxInvalidType_Object = MibTableColumn
tnNASRxInvalidType = _TnNASRxInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 6),
    _TnNASRxInvalidType_Type()
)
tnNASRxInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxInvalidType.setStatus("current")
_TnNASRxInvalidLength_Type = Gauge32
_TnNASRxInvalidLength_Object = MibTableColumn
tnNASRxInvalidLength = _TnNASRxInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 7),
    _TnNASRxInvalidLength_Type()
)
tnNASRxInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASRxInvalidLength.setStatus("current")
_TnNASTxTotal_Type = Gauge32
_TnNASTxTotal_Object = MibTableColumn
tnNASTxTotal = _TnNASTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 8),
    _TnNASTxTotal_Type()
)
tnNASTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASTxTotal.setStatus("current")
_TnNASTxRequestId_Type = Gauge32
_TnNASTxRequestId_Object = MibTableColumn
tnNASTxRequestId = _TnNASTxRequestId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 9),
    _TnNASTxRequestId_Type()
)
tnNASTxRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASTxRequestId.setStatus("current")
_TnNASTxRequests_Type = Gauge32
_TnNASTxRequests_Object = MibTableColumn
tnNASTxRequests = _TnNASTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 7, 1, 1, 10),
    _TnNASTxRequests_Type()
)
tnNASTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASTxRequests.setStatus("current")
_TnNASAttachedClientStatus_ObjectIdentity = ObjectIdentity
tnNASAttachedClientStatus = _TnNASAttachedClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8)
)
_TnNASAttachedClientStatusTable_Object = MibTable
tnNASAttachedClientStatusTable = _TnNASAttachedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tnNASAttachedClientStatusTable.setStatus("current")
_TnNASAttachedClientStatusEntry_Object = MibTableRow
tnNASAttachedClientStatusEntry = _TnNASAttachedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1)
)
tnNASAttachedClientStatusEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
    (0, "TN-NAS-MIB", "tnNASAttachedNum"),
)
if mibBuilder.loadTexts:
    tnNASAttachedClientStatusEntry.setStatus("current")
_TnNASAttachedNum_Type = Unsigned32
_TnNASAttachedNum_Object = MibTableColumn
tnNASAttachedNum = _TnNASAttachedNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1, 1),
    _TnNASAttachedNum_Type()
)
tnNASAttachedNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNASAttachedNum.setStatus("current")
_TnNASAttachedIdentify_Type = OctetString
_TnNASAttachedIdentify_Object = MibTableColumn
tnNASAttachedIdentify = _TnNASAttachedIdentify_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1, 2),
    _TnNASAttachedIdentify_Type()
)
tnNASAttachedIdentify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASAttachedIdentify.setStatus("current")
_TnNASMacAddress_Type = MacAddress
_TnNASMacAddress_Object = MibTableColumn
tnNASMacAddress = _TnNASMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1, 3),
    _TnNASMacAddress_Type()
)
tnNASMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASMacAddress.setStatus("current")
_TnNASAttachedVlanId_Type = VlanId
_TnNASAttachedVlanId_Object = MibTableColumn
tnNASAttachedVlanId = _TnNASAttachedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1, 4),
    _TnNASAttachedVlanId_Type()
)
tnNASAttachedVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASAttachedVlanId.setStatus("current")


class _TnNASState_Type(Integer32):
    """Custom type tnNASState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("authorized", 1),
          ("unauthorized", 2),
          ("globallyDisabled", 3))
    )


_TnNASState_Type.__name__ = "Integer32"
_TnNASState_Object = MibTableColumn
tnNASState = _TnNASState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1, 5),
    _TnNASState_Type()
)
tnNASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASState.setStatus("current")
_TnNASLastAuthentication_Type = OctetString
_TnNASLastAuthentication_Object = MibTableColumn
tnNASLastAuthentication = _TnNASLastAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1, 6),
    _TnNASLastAuthentication_Type()
)
tnNASLastAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNASLastAuthentication.setStatus("current")


class _TnNASSelected_Type(Integer32):
    """Custom type tnNASSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unselected", 0),
          ("selected", 1))
    )


_TnNASSelected_Type.__name__ = "Integer32"
_TnNASSelected_Object = MibTableColumn
tnNASSelected = _TnNASSelected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 8, 1, 1, 7),
    _TnNASSelected_Type()
)
tnNASSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASSelected.setStatus("current")
_TnNASClearCounter_ObjectIdentity = ObjectIdentity
tnNASClearCounter = _TnNASClearCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 9)
)
_TnNASClearCounterTable_Object = MibTable
tnNASClearCounterTable = _TnNASClearCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tnNASClearCounterTable.setStatus("current")
_TnNASClearCounterEntry_Object = MibTableRow
tnNASClearCounterEntry = _TnNASClearCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 9, 1, 1)
)
tnNASClearCounterEntry.setIndexNames(
    (0, "TN-NAS-MIB", "tnNASPortNum"),
)
if mibBuilder.loadTexts:
    tnNASClearCounterEntry.setStatus("current")


class _TnNASClear_Type(Integer32):
    """Custom type tnNASClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unclear", 0),
          ("clear", 1))
    )


_TnNASClear_Type.__name__ = "Integer32"
_TnNASClear_Object = MibTableColumn
tnNASClear = _TnNASClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 1, 9, 1, 1, 1),
    _TnNASClear_Type()
)
tnNASClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNASClear.setStatus("current")
_TnNASMIBConformance_ObjectIdentity = ObjectIdentity
tnNASMIBConformance = _TnNASMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 125, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-NAS-MIB",
    **{"TnNASAdminStateType": TnNASAdminStateType,
       "tnNASMIB": tnNASMIB,
       "tnNASMIBNotifications": tnNASMIBNotifications,
       "tnNASMIBObjects": tnNASMIBObjects,
       "tnNASSysMgmt": tnNASSysMgmt,
       "tnNASSysReAuthEnabled": tnNASSysReAuthEnabled,
       "tnNASSysReAuthPeriod": tnNASSysReAuthPeriod,
       "tnNASSysEAPOLTimeout": tnNASSysEAPOLTimeout,
       "tnNASSysAgingPeriod": tnNASSysAgingPeriod,
       "tnNASSysHoldTime": tnNASSysHoldTime,
       "tnNASSysRadiusAssignedQosEnable": tnNASSysRadiusAssignedQosEnable,
       "tnNASSysRadiusAssignedVlanEnable": tnNASSysRadiusAssignedVlanEnable,
       "tnNASSysGuestVlanEnable": tnNASSysGuestVlanEnable,
       "tnNASSysGuestVlanId": tnNASSysGuestVlanId,
       "tnNASSysMaxReAuthCount": tnNASSysMaxReAuthCount,
       "tnNASSysAllowGuestVlanIFEAPOLSeen": tnNASSysAllowGuestVlanIFEAPOLSeen,
       "tnNASPortMgmt": tnNASPortMgmt,
       "tnNASPortCfgTable": tnNASPortCfgTable,
       "tnNASPortCfgEntry": tnNASPortCfgEntry,
       "tnNASPortNum": tnNASPortNum,
       "tnNASAdminState": tnNASAdminState,
       "tnNASRadiusAssignedQosEnabled": tnNASRadiusAssignedQosEnabled,
       "tnNASRadiusAssignedVlanEnabled": tnNASRadiusAssignedVlanEnabled,
       "tnNASGuestVlanEnabled": tnNASGuestVlanEnabled,
       "tnNASPortCfgState": tnNASPortCfgState,
       "tnNASAuthCountMgmt": tnNASAuthCountMgmt,
       "tnNASAuthCountTable": tnNASAuthCountTable,
       "tnNASAuthCountEntry": tnNASAuthCountEntry,
       "tnNASAuthCount": tnNASAuthCount,
       "tnNASUnauthCount": tnNASUnauthCount,
       "tnNASPortStatus": tnNASPortStatus,
       "tnNASPortStatusTable": tnNASPortStatusTable,
       "tnNASPortStatusEntry": tnNASPortStatusEntry,
       "tnNASPortAdminState": tnNASPortAdminState,
       "tnNASPortState": tnNASPortState,
       "tnNASQosClass": tnNASQosClass,
       "tnNASPortVlanId": tnNASPortVlanId,
       "tnNASClientStatus": tnNASClientStatus,
       "tnNASClientStatusTable": tnNASClientStatusTable,
       "tnNASClientStatusEntry": tnNASClientStatusEntry,
       "tnNASClientNum": tnNASClientNum,
       "tnNASMacAddr": tnNASMacAddr,
       "tnNASVlanId": tnNASVlanId,
       "tnNASIdentify": tnNASIdentify,
       "tnNASSelectedBackendServerCounter": tnNASSelectedBackendServerCounter,
       "tnNASSelectedBackendServerCounterTable": tnNASSelectedBackendServerCounterTable,
       "tnNASSelectedBackendServerCounterEntry": tnNASSelectedBackendServerCounterEntry,
       "tnNASRxAccessChallenges": tnNASRxAccessChallenges,
       "tnNASRxOtherRequests": tnNASRxOtherRequests,
       "tnNASRxAuthSuccesses": tnNASRxAuthSuccesses,
       "tnNASRxAuthFailures": tnNASRxAuthFailures,
       "tnNASTxResponses": tnNASTxResponses,
       "tnNASSelectedEapolCounter": tnNASSelectedEapolCounter,
       "tnNASSelectedEapolCounterTable": tnNASSelectedEapolCounterTable,
       "tnNASSelectedEapolCounterEntry": tnNASSelectedEapolCounterEntry,
       "tnNASRxTotal": tnNASRxTotal,
       "tnNASRxResponseId": tnNASRxResponseId,
       "tnNASRxResponses": tnNASRxResponses,
       "tnNASRxStart": tnNASRxStart,
       "tnNASRxLogoff": tnNASRxLogoff,
       "tnNASRxInvalidType": tnNASRxInvalidType,
       "tnNASRxInvalidLength": tnNASRxInvalidLength,
       "tnNASTxTotal": tnNASTxTotal,
       "tnNASTxRequestId": tnNASTxRequestId,
       "tnNASTxRequests": tnNASTxRequests,
       "tnNASAttachedClientStatus": tnNASAttachedClientStatus,
       "tnNASAttachedClientStatusTable": tnNASAttachedClientStatusTable,
       "tnNASAttachedClientStatusEntry": tnNASAttachedClientStatusEntry,
       "tnNASAttachedNum": tnNASAttachedNum,
       "tnNASAttachedIdentify": tnNASAttachedIdentify,
       "tnNASMacAddress": tnNASMacAddress,
       "tnNASAttachedVlanId": tnNASAttachedVlanId,
       "tnNASState": tnNASState,
       "tnNASLastAuthentication": tnNASLastAuthentication,
       "tnNASSelected": tnNASSelected,
       "tnNASClearCounter": tnNASClearCounter,
       "tnNASClearCounterTable": tnNASClearCounterTable,
       "tnNASClearCounterEntry": tnNASClearCounterEntry,
       "tnNASClear": tnNASClear,
       "tnNASMIBConformance": tnNASMIBConformance}
)
