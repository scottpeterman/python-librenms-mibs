# SNMP MIB module (ARUBAWIRED-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-MSTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:18 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredMstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    arubaWiredMstpMIB.setRevisions(
        ("2020-06-12 00:00",
         "2018-01-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PointToPoint(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 1),
          ("forceFalse", 2),
          ("auto", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ArubaWiredMstpNotifications_ObjectIdentity = ObjectIdentity
arubaWiredMstpNotifications = _ArubaWiredMstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0)
)
_ArubaWiredMstpObjects_ObjectIdentity = ObjectIdentity
arubaWiredMstpObjects = _ArubaWiredMstpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1)
)
_ArubaWiredMstpNotificationTable_Object = MibTable
arubaWiredMstpNotificationTable = _ArubaWiredMstpNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredMstpNotificationTable.setStatus("current")
_ArubaWiredMstpNotificationEntry_Object = MibTableRow
arubaWiredMstpNotificationEntry = _ArubaWiredMstpNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1)
)
arubaWiredMstpNotificationEntry.setIndexNames(
    (0, "ARUBAWIRED-MSTP-MIB", "arubaWiredMstpId"),
)
if mibBuilder.loadTexts:
    arubaWiredMstpNotificationEntry.setStatus("current")


class _ArubaWiredMstpPortName_Type(DisplayString):
    """Custom type arubaWiredMstpPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpPortName_Type.__name__ = "DisplayString"
_ArubaWiredMstpPortName_Object = MibTableColumn
arubaWiredMstpPortName = _ArubaWiredMstpPortName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 1),
    _ArubaWiredMstpPortName_Type()
)
arubaWiredMstpPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpPortName.setStatus("current")


class _ArubaWiredMstpInstanceID_Type(Integer32):
    """Custom type arubaWiredMstpInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65),
    )


_ArubaWiredMstpInstanceID_Type.__name__ = "Integer32"
_ArubaWiredMstpInstanceID_Object = MibTableColumn
arubaWiredMstpInstanceID = _ArubaWiredMstpInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 2),
    _ArubaWiredMstpInstanceID_Type()
)
arubaWiredMstpInstanceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpInstanceID.setStatus("current")


class _ArubaWiredMstpPortErrantBpduRxCount_Type(Integer32):
    """Custom type arubaWiredMstpPortErrantBpduRxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArubaWiredMstpPortErrantBpduRxCount_Type.__name__ = "Integer32"
_ArubaWiredMstpPortErrantBpduRxCount_Object = MibTableColumn
arubaWiredMstpPortErrantBpduRxCount = _ArubaWiredMstpPortErrantBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 3),
    _ArubaWiredMstpPortErrantBpduRxCount_Type()
)
arubaWiredMstpPortErrantBpduRxCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpPortErrantBpduRxCount.setStatus("current")
_ArubaWiredMstpErrantBpduSrcMac_Type = MacAddress
_ArubaWiredMstpErrantBpduSrcMac_Object = MibTableColumn
arubaWiredMstpErrantBpduSrcMac = _ArubaWiredMstpErrantBpduSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 4),
    _ArubaWiredMstpErrantBpduSrcMac_Type()
)
arubaWiredMstpErrantBpduSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpErrantBpduSrcMac.setStatus("current")


class _ArubaWiredMstpSuperiorBpduSrcPort_Type(DisplayString):
    """Custom type arubaWiredMstpSuperiorBpduSrcPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpSuperiorBpduSrcPort_Type.__name__ = "DisplayString"
_ArubaWiredMstpSuperiorBpduSrcPort_Object = MibTableColumn
arubaWiredMstpSuperiorBpduSrcPort = _ArubaWiredMstpSuperiorBpduSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 5),
    _ArubaWiredMstpSuperiorBpduSrcPort_Type()
)
arubaWiredMstpSuperiorBpduSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpSuperiorBpduSrcPort.setStatus("current")
_ArubaWiredMstpSuperiorBpduSrcMac_Type = MacAddress
_ArubaWiredMstpSuperiorBpduSrcMac_Object = MibTableColumn
arubaWiredMstpSuperiorBpduSrcMac = _ArubaWiredMstpSuperiorBpduSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 6),
    _ArubaWiredMstpSuperiorBpduSrcMac_Type()
)
arubaWiredMstpSuperiorBpduSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpSuperiorBpduSrcMac.setStatus("current")


class _ArubaWiredMstpPortInstanceState_Type(DisplayString):
    """Custom type arubaWiredMstpPortInstanceState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpPortInstanceState_Type.__name__ = "DisplayString"
_ArubaWiredMstpPortInstanceState_Object = MibTableColumn
arubaWiredMstpPortInstanceState = _ArubaWiredMstpPortInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 7),
    _ArubaWiredMstpPortInstanceState_Type()
)
arubaWiredMstpPortInstanceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpPortInstanceState.setStatus("current")


class _ArubaWiredMstpErrantBpduDetector_Type(Integer32):
    """Custom type arubaWiredMstpErrantBpduDetector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bpduFilter", 1),
          ("bpduProtection", 2))
    )


_ArubaWiredMstpErrantBpduDetector_Type.__name__ = "Integer32"
_ArubaWiredMstpErrantBpduDetector_Object = MibTableColumn
arubaWiredMstpErrantBpduDetector = _ArubaWiredMstpErrantBpduDetector_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 8),
    _ArubaWiredMstpErrantBpduDetector_Type()
)
arubaWiredMstpErrantBpduDetector.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpErrantBpduDetector.setStatus("current")


class _ArubaWiredMstpPortDesignatedBridge_Type(DisplayString):
    """Custom type arubaWiredMstpPortDesignatedBridge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpPortDesignatedBridge_Type.__name__ = "DisplayString"
_ArubaWiredMstpPortDesignatedBridge_Object = MibTableColumn
arubaWiredMstpPortDesignatedBridge = _ArubaWiredMstpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 9),
    _ArubaWiredMstpPortDesignatedBridge_Type()
)
arubaWiredMstpPortDesignatedBridge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpPortDesignatedBridge.setStatus("current")


class _ArubaWiredMstpOldPortRole_Type(DisplayString):
    """Custom type arubaWiredMstpOldPortRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpOldPortRole_Type.__name__ = "DisplayString"
_ArubaWiredMstpOldPortRole_Object = MibTableColumn
arubaWiredMstpOldPortRole = _ArubaWiredMstpOldPortRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 10),
    _ArubaWiredMstpOldPortRole_Type()
)
arubaWiredMstpOldPortRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpOldPortRole.setStatus("current")


class _ArubaWiredMstpNewPortRole_Type(DisplayString):
    """Custom type arubaWiredMstpNewPortRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpNewPortRole_Type.__name__ = "DisplayString"
_ArubaWiredMstpNewPortRole_Object = MibTableColumn
arubaWiredMstpNewPortRole = _ArubaWiredMstpNewPortRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 11),
    _ArubaWiredMstpNewPortRole_Type()
)
arubaWiredMstpNewPortRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpNewPortRole.setStatus("current")
_ArubaWiredMstpTopoChangeTime_Type = DateAndTime
_ArubaWiredMstpTopoChangeTime_Object = MibTableColumn
arubaWiredMstpTopoChangeTime = _ArubaWiredMstpTopoChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 12),
    _ArubaWiredMstpTopoChangeTime_Type()
)
arubaWiredMstpTopoChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpTopoChangeTime.setStatus("current")


class _ArubaWiredMstpPreviousRootBridgeID_Type(DisplayString):
    """Custom type arubaWiredMstpPreviousRootBridgeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpPreviousRootBridgeID_Type.__name__ = "DisplayString"
_ArubaWiredMstpPreviousRootBridgeID_Object = MibTableColumn
arubaWiredMstpPreviousRootBridgeID = _ArubaWiredMstpPreviousRootBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 13),
    _ArubaWiredMstpPreviousRootBridgeID_Type()
)
arubaWiredMstpPreviousRootBridgeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpPreviousRootBridgeID.setStatus("current")


class _ArubaWiredMstpNewRootBridgeID_Type(DisplayString):
    """Custom type arubaWiredMstpNewRootBridgeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredMstpNewRootBridgeID_Type.__name__ = "DisplayString"
_ArubaWiredMstpNewRootBridgeID_Object = MibTableColumn
arubaWiredMstpNewRootBridgeID = _ArubaWiredMstpNewRootBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 14),
    _ArubaWiredMstpNewRootBridgeID_Type()
)
arubaWiredMstpNewRootBridgeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpNewRootBridgeID.setStatus("current")
_ArubaWiredMstpRootBridgeChangeTimeStamp_Type = DateAndTime
_ArubaWiredMstpRootBridgeChangeTimeStamp_Object = MibTableColumn
arubaWiredMstpRootBridgeChangeTimeStamp = _ArubaWiredMstpRootBridgeChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 15),
    _ArubaWiredMstpRootBridgeChangeTimeStamp_Type()
)
arubaWiredMstpRootBridgeChangeTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMstpRootBridgeChangeTimeStamp.setStatus("current")


class _ArubaWiredMstpId_Type(Integer32):
    """Custom type arubaWiredMstpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65),
    )


_ArubaWiredMstpId_Type.__name__ = "Integer32"
_ArubaWiredMstpId_Object = MibTableColumn
arubaWiredMstpId = _ArubaWiredMstpId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 1, 1, 16),
    _ArubaWiredMstpId_Type()
)
arubaWiredMstpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMstpId.setStatus("current")
_ArubaWiredMstpPortTable_Object = MibTable
arubaWiredMstpPortTable = _ArubaWiredMstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredMstpPortTable.setStatus("current")
_ArubaWiredMstpPortEntry_Object = MibTableRow
arubaWiredMstpPortEntry = _ArubaWiredMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1)
)
arubaWiredMstpPortEntry.setIndexNames(
    (0, "ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMstpPortEntry.setStatus("current")
_ArubaWiredMstpPortIndex_Type = InterfaceIndex
_ArubaWiredMstpPortIndex_Object = MibTableColumn
arubaWiredMstpPortIndex = _ArubaWiredMstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 1),
    _ArubaWiredMstpPortIndex_Type()
)
arubaWiredMstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMstpPortIndex.setStatus("current")


class _ArubaWiredMstpPortAdminEdge_Type(TruthValue):
    """Custom type arubaWiredMstpPortAdminEdge based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortAdminEdge_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortAdminEdge_Object = MibTableColumn
arubaWiredMstpPortAdminEdge = _ArubaWiredMstpPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 2),
    _ArubaWiredMstpPortAdminEdge_Type()
)
arubaWiredMstpPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortAdminEdge.setStatus("current")


class _ArubaWiredMstpPortAdminPointToPoint_Type(PointToPoint):
    """Custom type arubaWiredMstpPortAdminPointToPoint based on PointToPoint"""
    defaultValue = 3


_ArubaWiredMstpPortAdminPointToPoint_Type.__name__ = "PointToPoint"
_ArubaWiredMstpPortAdminPointToPoint_Object = MibTableColumn
arubaWiredMstpPortAdminPointToPoint = _ArubaWiredMstpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 3),
    _ArubaWiredMstpPortAdminPointToPoint_Type()
)
arubaWiredMstpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortAdminPointToPoint.setStatus("current")


class _ArubaWiredMstpPortAutoEdge_Type(TruthValue):
    """Custom type arubaWiredMstpPortAutoEdge based on TruthValue"""
    defaultValue = 1


_ArubaWiredMstpPortAutoEdge_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortAutoEdge_Object = MibTableColumn
arubaWiredMstpPortAutoEdge = _ArubaWiredMstpPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 4),
    _ArubaWiredMstpPortAutoEdge_Type()
)
arubaWiredMstpPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortAutoEdge.setStatus("current")


class _ArubaWiredMstpPortBpduFiltering_Type(TruthValue):
    """Custom type arubaWiredMstpPortBpduFiltering based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortBpduFiltering_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortBpduFiltering_Object = MibTableColumn
arubaWiredMstpPortBpduFiltering = _ArubaWiredMstpPortBpduFiltering_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 5),
    _ArubaWiredMstpPortBpduFiltering_Type()
)
arubaWiredMstpPortBpduFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortBpduFiltering.setStatus("current")


class _ArubaWiredMstpPortRestrictedTcn_Type(TruthValue):
    """Custom type arubaWiredMstpPortRestrictedTcn based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortRestrictedTcn_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortRestrictedTcn_Object = MibTableColumn
arubaWiredMstpPortRestrictedTcn = _ArubaWiredMstpPortRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 6),
    _ArubaWiredMstpPortRestrictedTcn_Type()
)
arubaWiredMstpPortRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortRestrictedTcn.setStatus("current")


class _ArubaWiredMstpPortRootGuard_Type(TruthValue):
    """Custom type arubaWiredMstpPortRootGuard based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortRootGuard_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortRootGuard_Object = MibTableColumn
arubaWiredMstpPortRootGuard = _ArubaWiredMstpPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 7),
    _ArubaWiredMstpPortRootGuard_Type()
)
arubaWiredMstpPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortRootGuard.setStatus("current")


class _ArubaWiredMstpPortLoopGuard_Type(TruthValue):
    """Custom type arubaWiredMstpPortLoopGuard based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortLoopGuard_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortLoopGuard_Object = MibTableColumn
arubaWiredMstpPortLoopGuard = _ArubaWiredMstpPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 8),
    _ArubaWiredMstpPortLoopGuard_Type()
)
arubaWiredMstpPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortLoopGuard.setStatus("current")


class _ArubaWiredMstpPortBpduProtection_Type(TruthValue):
    """Custom type arubaWiredMstpPortBpduProtection based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortBpduProtection_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortBpduProtection_Object = MibTableColumn
arubaWiredMstpPortBpduProtection = _ArubaWiredMstpPortBpduProtection_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 9),
    _ArubaWiredMstpPortBpduProtection_Type()
)
arubaWiredMstpPortBpduProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortBpduProtection.setStatus("current")


class _ArubaWiredMstpPortRpvstProtection_Type(TruthValue):
    """Custom type arubaWiredMstpPortRpvstProtection based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortRpvstProtection_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortRpvstProtection_Object = MibTableColumn
arubaWiredMstpPortRpvstProtection = _ArubaWiredMstpPortRpvstProtection_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 10),
    _ArubaWiredMstpPortRpvstProtection_Type()
)
arubaWiredMstpPortRpvstProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortRpvstProtection.setStatus("current")


class _ArubaWiredMstpPortRpvstFiltering_Type(TruthValue):
    """Custom type arubaWiredMstpPortRpvstFiltering based on TruthValue"""
    defaultValue = 2


_ArubaWiredMstpPortRpvstFiltering_Type.__name__ = "TruthValue"
_ArubaWiredMstpPortRpvstFiltering_Object = MibTableColumn
arubaWiredMstpPortRpvstFiltering = _ArubaWiredMstpPortRpvstFiltering_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 2, 1, 11),
    _ArubaWiredMstpPortRpvstFiltering_Type()
)
arubaWiredMstpPortRpvstFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpPortRpvstFiltering.setStatus("current")
_ArubaWiredMstpGeneralGroup_ObjectIdentity = ObjectIdentity
arubaWiredMstpGeneralGroup = _ArubaWiredMstpGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 3)
)
_ArubaWiredMstpBpduGuardTimeout_Type = Integer32
_ArubaWiredMstpBpduGuardTimeout_Object = MibScalar
arubaWiredMstpBpduGuardTimeout = _ArubaWiredMstpBpduGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 1, 3, 1),
    _ArubaWiredMstpBpduGuardTimeout_Type()
)
arubaWiredMstpBpduGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMstpBpduGuardTimeout.setStatus("current")
_ArubaWiredMstpConformance_ObjectIdentity = ObjectIdentity
arubaWiredMstpConformance = _ArubaWiredMstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2)
)
_ArubaWiredMstpGroups_ObjectIdentity = ObjectIdentity
arubaWiredMstpGroups = _ArubaWiredMstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2, 1)
)
_ArubaWiredMstpCompliances_ObjectIdentity = ObjectIdentity
arubaWiredMstpCompliances = _ArubaWiredMstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2, 2)
)

# Managed Objects groups

arubaWiredMstpNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2, 1, 1)
)
arubaWiredMstpNotificationObjectGroup.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortErrantBpduRxCount"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpErrantBpduSrcMac"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpSuperiorBpduSrcPort"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpSuperiorBpduSrcMac"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortInstanceState"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpErrantBpduDetector"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortDesignatedBridge"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpOldPortRole"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNewPortRole"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpTopoChangeTime"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPreviousRootBridgeID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNewRootBridgeID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpRootBridgeChangeTimeStamp"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpNotificationObjectGroup.setStatus("current")

arubaWiredMstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2, 1, 3)
)
arubaWiredMstpPortGroup.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortAdminEdge"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortAdminPointToPoint"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortAutoEdge"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortBpduFiltering"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortRestrictedTcn"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortRootGuard"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortLoopGuard"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortBpduProtection"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortRpvstProtection"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortRpvstFiltering"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpPortGroup.setStatus("current")

arubaWiredMstpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2, 1, 4)
)
arubaWiredMstpGroup.setObjects(
    ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpBpduGuardTimeout")
)
if mibBuilder.loadTexts:
    arubaWiredMstpGroup.setStatus("current")


# Notification objects

arubaWiredMstpErrantBpduReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 1)
)
arubaWiredMstpErrantBpduReceived.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortErrantBpduRxCount"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpErrantBpduSrcMac"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortInstanceState"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpErrantBpduDetector"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpErrantBpduReceived.setStatus(
        "current"
    )

arubaWiredMstpInstanceTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 2)
)
arubaWiredMstpInstanceTopologyChange.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpOldPortRole"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNewPortRole"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpTopoChangeTime"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpInstanceTopologyChange.setStatus(
        "current"
    )

arubaWiredMstpCISTTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 3)
)
arubaWiredMstpCISTTopologyChange.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpOldPortRole"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNewPortRole"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpTopoChangeTime"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpCISTTopologyChange.setStatus(
        "current"
    )

arubaWiredMstpInstanceNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 4)
)
arubaWiredMstpInstanceNewRoot.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPreviousRootBridgeID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNewRootBridgeID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpRootBridgeChangeTimeStamp"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpInstanceNewRoot.setStatus(
        "current"
    )

arubaWiredMstpCISTNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 5)
)
arubaWiredMstpCISTNewRoot.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPreviousRootBridgeID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNewRootBridgeID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpRootBridgeChangeTimeStamp"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpCISTNewRoot.setStatus(
        "current"
    )

arubaWiredMstpInstanceLoopGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 6)
)
arubaWiredMstpInstanceLoopGuardInconsistency.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortDesignatedBridge"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpInstanceLoopGuardInconsistency.setStatus(
        "current"
    )

arubaWiredMstpCISTLoopGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 7)
)
arubaWiredMstpCISTLoopGuardInconsistency.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortDesignatedBridge"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpCISTLoopGuardInconsistency.setStatus(
        "current"
    )

arubaWiredMstpInstanceRootGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 8)
)
arubaWiredMstpInstanceRootGuardInconsistency.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceID"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpSuperiorBpduSrcMac"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpSuperiorBpduSrcPort"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpInstanceRootGuardInconsistency.setStatus(
        "current"
    )

arubaWiredMstpCISTRootGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 0, 9)
)
arubaWiredMstpCISTRootGuardInconsistency.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortName"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpSuperiorBpduSrcMac"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpSuperiorBpduSrcPort"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpCISTRootGuardInconsistency.setStatus(
        "current"
    )


# Notifications groups

arubaWiredMstpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2, 1, 2)
)
arubaWiredMstpNotificationGroup.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpErrantBpduReceived"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceNewRoot"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpCISTNewRoot"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceRootGuardInconsistency"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpCISTRootGuardInconsistency"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceLoopGuardInconsistency"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpCISTLoopGuardInconsistency"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpInstanceTopologyChange"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpCISTTopologyChange"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredMstpNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13, 2, 2, 1)
)
arubaWiredMstpNotificationCompliance.setObjects(
      *(("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNotificationObjectGroup"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpNotificationGroup"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpPortGroup"),
        ("ARUBAWIRED-MSTP-MIB", "arubaWiredMstpGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredMstpNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-MSTP-MIB",
    **{"PointToPoint": PointToPoint,
       "arubaWiredMstpMIB": arubaWiredMstpMIB,
       "arubaWiredMstpNotifications": arubaWiredMstpNotifications,
       "arubaWiredMstpErrantBpduReceived": arubaWiredMstpErrantBpduReceived,
       "arubaWiredMstpInstanceTopologyChange": arubaWiredMstpInstanceTopologyChange,
       "arubaWiredMstpCISTTopologyChange": arubaWiredMstpCISTTopologyChange,
       "arubaWiredMstpInstanceNewRoot": arubaWiredMstpInstanceNewRoot,
       "arubaWiredMstpCISTNewRoot": arubaWiredMstpCISTNewRoot,
       "arubaWiredMstpInstanceLoopGuardInconsistency": arubaWiredMstpInstanceLoopGuardInconsistency,
       "arubaWiredMstpCISTLoopGuardInconsistency": arubaWiredMstpCISTLoopGuardInconsistency,
       "arubaWiredMstpInstanceRootGuardInconsistency": arubaWiredMstpInstanceRootGuardInconsistency,
       "arubaWiredMstpCISTRootGuardInconsistency": arubaWiredMstpCISTRootGuardInconsistency,
       "arubaWiredMstpObjects": arubaWiredMstpObjects,
       "arubaWiredMstpNotificationTable": arubaWiredMstpNotificationTable,
       "arubaWiredMstpNotificationEntry": arubaWiredMstpNotificationEntry,
       "arubaWiredMstpPortName": arubaWiredMstpPortName,
       "arubaWiredMstpInstanceID": arubaWiredMstpInstanceID,
       "arubaWiredMstpPortErrantBpduRxCount": arubaWiredMstpPortErrantBpduRxCount,
       "arubaWiredMstpErrantBpduSrcMac": arubaWiredMstpErrantBpduSrcMac,
       "arubaWiredMstpSuperiorBpduSrcPort": arubaWiredMstpSuperiorBpduSrcPort,
       "arubaWiredMstpSuperiorBpduSrcMac": arubaWiredMstpSuperiorBpduSrcMac,
       "arubaWiredMstpPortInstanceState": arubaWiredMstpPortInstanceState,
       "arubaWiredMstpErrantBpduDetector": arubaWiredMstpErrantBpduDetector,
       "arubaWiredMstpPortDesignatedBridge": arubaWiredMstpPortDesignatedBridge,
       "arubaWiredMstpOldPortRole": arubaWiredMstpOldPortRole,
       "arubaWiredMstpNewPortRole": arubaWiredMstpNewPortRole,
       "arubaWiredMstpTopoChangeTime": arubaWiredMstpTopoChangeTime,
       "arubaWiredMstpPreviousRootBridgeID": arubaWiredMstpPreviousRootBridgeID,
       "arubaWiredMstpNewRootBridgeID": arubaWiredMstpNewRootBridgeID,
       "arubaWiredMstpRootBridgeChangeTimeStamp": arubaWiredMstpRootBridgeChangeTimeStamp,
       "arubaWiredMstpId": arubaWiredMstpId,
       "arubaWiredMstpPortTable": arubaWiredMstpPortTable,
       "arubaWiredMstpPortEntry": arubaWiredMstpPortEntry,
       "arubaWiredMstpPortIndex": arubaWiredMstpPortIndex,
       "arubaWiredMstpPortAdminEdge": arubaWiredMstpPortAdminEdge,
       "arubaWiredMstpPortAdminPointToPoint": arubaWiredMstpPortAdminPointToPoint,
       "arubaWiredMstpPortAutoEdge": arubaWiredMstpPortAutoEdge,
       "arubaWiredMstpPortBpduFiltering": arubaWiredMstpPortBpduFiltering,
       "arubaWiredMstpPortRestrictedTcn": arubaWiredMstpPortRestrictedTcn,
       "arubaWiredMstpPortRootGuard": arubaWiredMstpPortRootGuard,
       "arubaWiredMstpPortLoopGuard": arubaWiredMstpPortLoopGuard,
       "arubaWiredMstpPortBpduProtection": arubaWiredMstpPortBpduProtection,
       "arubaWiredMstpPortRpvstProtection": arubaWiredMstpPortRpvstProtection,
       "arubaWiredMstpPortRpvstFiltering": arubaWiredMstpPortRpvstFiltering,
       "arubaWiredMstpGeneralGroup": arubaWiredMstpGeneralGroup,
       "arubaWiredMstpBpduGuardTimeout": arubaWiredMstpBpduGuardTimeout,
       "arubaWiredMstpConformance": arubaWiredMstpConformance,
       "arubaWiredMstpGroups": arubaWiredMstpGroups,
       "arubaWiredMstpNotificationObjectGroup": arubaWiredMstpNotificationObjectGroup,
       "arubaWiredMstpNotificationGroup": arubaWiredMstpNotificationGroup,
       "arubaWiredMstpPortGroup": arubaWiredMstpPortGroup,
       "arubaWiredMstpGroup": arubaWiredMstpGroup,
       "arubaWiredMstpCompliances": arubaWiredMstpCompliances,
       "arubaWiredMstpNotificationCompliance": arubaWiredMstpNotificationCompliance}
)
