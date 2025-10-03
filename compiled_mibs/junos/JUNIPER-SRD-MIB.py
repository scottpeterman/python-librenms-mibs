# SNMP MIB module (JUNIPER-SRD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-SRD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:50 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(jnxSRDMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxSRDMibRoot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxSRDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1)
)
if mibBuilder.loadTexts:
    jnxSRDMIB.setRevisions(
        ("2014-11-20 20:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxSRDNotification_ObjectIdentity = ObjectIdentity
jnxSRDNotification = _JnxSRDNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1)
)
_JnxSRDNotificationType_ObjectIdentity = ObjectIdentity
jnxSRDNotificationType = _JnxSRDNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 0)
)
_JnxSRDNotificationObj_ObjectIdentity = ObjectIdentity
jnxSRDNotificationObj = _JnxSRDNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1)
)
_JnxSRDTrapRedundancySetID_Type = DisplayString
_JnxSRDTrapRedundancySetID_Object = MibScalar
jnxSRDTrapRedundancySetID = _JnxSRDTrapRedundancySetID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 1),
    _JnxSRDTrapRedundancySetID_Type()
)
jnxSRDTrapRedundancySetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapRedundancySetID.setStatus("current")
_JnxSRDTrapRedundancySetOldState_Type = DisplayString
_JnxSRDTrapRedundancySetOldState_Object = MibScalar
jnxSRDTrapRedundancySetOldState = _JnxSRDTrapRedundancySetOldState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 2),
    _JnxSRDTrapRedundancySetOldState_Type()
)
jnxSRDTrapRedundancySetOldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapRedundancySetOldState.setStatus("current")
_JnxSRDTrapRedundancySetEvent_Type = DisplayString
_JnxSRDTrapRedundancySetEvent_Object = MibScalar
jnxSRDTrapRedundancySetEvent = _JnxSRDTrapRedundancySetEvent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 3),
    _JnxSRDTrapRedundancySetEvent_Type()
)
jnxSRDTrapRedundancySetEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapRedundancySetEvent.setStatus("current")
_JnxSRDTrapRedundancySetNewState_Type = DisplayString
_JnxSRDTrapRedundancySetNewState_Object = MibScalar
jnxSRDTrapRedundancySetNewState = _JnxSRDTrapRedundancySetNewState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 4),
    _JnxSRDTrapRedundancySetNewState_Type()
)
jnxSRDTrapRedundancySetNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapRedundancySetNewState.setStatus("current")
_JnxSRDTrapNotificationMessage_Type = DisplayString
_JnxSRDTrapNotificationMessage_Object = MibScalar
jnxSRDTrapNotificationMessage = _JnxSRDTrapNotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 5),
    _JnxSRDTrapNotificationMessage_Type()
)
jnxSRDTrapNotificationMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapNotificationMessage.setStatus("current")
_JnxSRDTrapRedundancyPeerIPAddressType_Type = InetAddressType
_JnxSRDTrapRedundancyPeerIPAddressType_Object = MibScalar
jnxSRDTrapRedundancyPeerIPAddressType = _JnxSRDTrapRedundancyPeerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 6),
    _JnxSRDTrapRedundancyPeerIPAddressType_Type()
)
jnxSRDTrapRedundancyPeerIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapRedundancyPeerIPAddressType.setStatus("current")
_JnxSRDTrapRedundancyPeerIPAddress_Type = InetAddress
_JnxSRDTrapRedundancyPeerIPAddress_Object = MibScalar
jnxSRDTrapRedundancyPeerIPAddress = _JnxSRDTrapRedundancyPeerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 7),
    _JnxSRDTrapRedundancyPeerIPAddress_Type()
)
jnxSRDTrapRedundancyPeerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapRedundancyPeerIPAddress.setStatus("current")
_JnxSRDTrapRedundancyActionErrorCode_Type = DisplayString
_JnxSRDTrapRedundancyActionErrorCode_Object = MibScalar
jnxSRDTrapRedundancyActionErrorCode = _JnxSRDTrapRedundancyActionErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 1, 8),
    _JnxSRDTrapRedundancyActionErrorCode_Type()
)
jnxSRDTrapRedundancyActionErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDTrapRedundancyActionErrorCode.setStatus("current")
_JnxSRDRedundancyGroup_ObjectIdentity = ObjectIdentity
jnxSRDRedundancyGroup = _JnxSRDRedundancyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2)
)
_JnxSRDRedundancyGroupTable_Object = MibTable
jnxSRDRedundancyGroupTable = _JnxSRDRedundancyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxSRDRedundancyGroupTable.setStatus("current")
_JnxSRDRedundancyGroupEntry_Object = MibTableRow
jnxSRDRedundancyGroupEntry = _JnxSRDRedundancyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1)
)
jnxSRDRedundancyGroupEntry.setIndexNames(
    (0, "JUNIPER-SRD-MIB", "jnxSRDRedundancyGroupID"),
    (0, "JUNIPER-SRD-MIB", "jnxSRDRedundancySetID"),
)
if mibBuilder.loadTexts:
    jnxSRDRedundancyGroupEntry.setStatus("current")
_JnxSRDRedundancyGroupID_Type = DisplayString
_JnxSRDRedundancyGroupID_Object = MibTableColumn
jnxSRDRedundancyGroupID = _JnxSRDRedundancyGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 1),
    _JnxSRDRedundancyGroupID_Type()
)
jnxSRDRedundancyGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancyGroupID.setStatus("current")
_JnxSRDRedundancySetID_Type = DisplayString
_JnxSRDRedundancySetID_Object = MibTableColumn
jnxSRDRedundancySetID = _JnxSRDRedundancySetID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 2),
    _JnxSRDRedundancySetID_Type()
)
jnxSRDRedundancySetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetID.setStatus("current")
_JnxSRDRedundancyGroupTotalPeer_Type = Unsigned32
_JnxSRDRedundancyGroupTotalPeer_Object = MibTableColumn
jnxSRDRedundancyGroupTotalPeer = _JnxSRDRedundancyGroupTotalPeer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 3),
    _JnxSRDRedundancyGroupTotalPeer_Type()
)
jnxSRDRedundancyGroupTotalPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancyGroupTotalPeer.setStatus("current")
_JnxSRDRedundancyGroupConnStatus_Type = DisplayString
_JnxSRDRedundancyGroupConnStatus_Object = MibTableColumn
jnxSRDRedundancyGroupConnStatus = _JnxSRDRedundancyGroupConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 4),
    _JnxSRDRedundancyGroupConnStatus_Type()
)
jnxSRDRedundancyGroupConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancyGroupConnStatus.setStatus("current")
_JnxSRDRedundancySRDIccpConnStatus_Type = DisplayString
_JnxSRDRedundancySRDIccpConnStatus_Object = MibTableColumn
jnxSRDRedundancySRDIccpConnStatus = _JnxSRDRedundancySRDIccpConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 5),
    _JnxSRDRedundancySRDIccpConnStatus_Type()
)
jnxSRDRedundancySRDIccpConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySRDIccpConnStatus.setStatus("current")
_JnxSRDRedundancySRDRemoteIPAddressType_Type = InetAddressType
_JnxSRDRedundancySRDRemoteIPAddressType_Object = MibTableColumn
jnxSRDRedundancySRDRemoteIPAddressType = _JnxSRDRedundancySRDRemoteIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 6),
    _JnxSRDRedundancySRDRemoteIPAddressType_Type()
)
jnxSRDRedundancySRDRemoteIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySRDRemoteIPAddressType.setStatus("current")
_JnxSRDRedundancySRDRemoteIPAddress_Type = InetAddress
_JnxSRDRedundancySRDRemoteIPAddress_Object = MibTableColumn
jnxSRDRedundancySRDRemoteIPAddress = _JnxSRDRedundancySRDRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 7),
    _JnxSRDRedundancySRDRemoteIPAddress_Type()
)
jnxSRDRedundancySRDRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySRDRemoteIPAddress.setStatus("current")
_JnxSRDRedundancySetState_Type = DisplayString
_JnxSRDRedundancySetState_Object = MibTableColumn
jnxSRDRedundancySetState = _JnxSRDRedundancySetState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 8),
    _JnxSRDRedundancySetState_Type()
)
jnxSRDRedundancySetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetState.setStatus("current")
_JnxSRDRedundancySetPeerState_Type = DisplayString
_JnxSRDRedundancySetPeerState_Object = MibTableColumn
jnxSRDRedundancySetPeerState = _JnxSRDRedundancySetPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 9),
    _JnxSRDRedundancySetPeerState_Type()
)
jnxSRDRedundancySetPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetPeerState.setStatus("current")
_JnxSRDRedundancySetHealthStatus_Type = DisplayString
_JnxSRDRedundancySetHealthStatus_Object = MibTableColumn
jnxSRDRedundancySetHealthStatus = _JnxSRDRedundancySetHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 10),
    _JnxSRDRedundancySetHealthStatus_Type()
)
jnxSRDRedundancySetHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetHealthStatus.setStatus("current")
_JnxSRDRedundancySetLinkDownEventReceived_Type = Unsigned32
_JnxSRDRedundancySetLinkDownEventReceived_Object = MibTableColumn
jnxSRDRedundancySetLinkDownEventReceived = _JnxSRDRedundancySetLinkDownEventReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 11),
    _JnxSRDRedundancySetLinkDownEventReceived_Type()
)
jnxSRDRedundancySetLinkDownEventReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetLinkDownEventReceived.setStatus("current")
_JnxSRDRedundancySetLinkDownEventDropped_Type = Unsigned32
_JnxSRDRedundancySetLinkDownEventDropped_Object = MibTableColumn
jnxSRDRedundancySetLinkDownEventDropped = _JnxSRDRedundancySetLinkDownEventDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 12),
    _JnxSRDRedundancySetLinkDownEventDropped_Type()
)
jnxSRDRedundancySetLinkDownEventDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetLinkDownEventDropped.setStatus("current")
_JnxSRDRedundancySetRpdRestartEventReceived_Type = Unsigned32
_JnxSRDRedundancySetRpdRestartEventReceived_Object = MibTableColumn
jnxSRDRedundancySetRpdRestartEventReceived = _JnxSRDRedundancySetRpdRestartEventReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 13),
    _JnxSRDRedundancySetRpdRestartEventReceived_Type()
)
jnxSRDRedundancySetRpdRestartEventReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetRpdRestartEventReceived.setStatus("current")
_JnxSRDRedundancySetRpdRestartEventDropped_Type = Unsigned32
_JnxSRDRedundancySetRpdRestartEventDropped_Object = MibTableColumn
jnxSRDRedundancySetRpdRestartEventDropped = _JnxSRDRedundancySetRpdRestartEventDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 14),
    _JnxSRDRedundancySetRpdRestartEventDropped_Type()
)
jnxSRDRedundancySetRpdRestartEventDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetRpdRestartEventDropped.setStatus("current")
_JnxSRDRedundancySetRouteUpdateErrorEventReceived_Type = Unsigned32
_JnxSRDRedundancySetRouteUpdateErrorEventReceived_Object = MibTableColumn
jnxSRDRedundancySetRouteUpdateErrorEventReceived = _JnxSRDRedundancySetRouteUpdateErrorEventReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 15),
    _JnxSRDRedundancySetRouteUpdateErrorEventReceived_Type()
)
jnxSRDRedundancySetRouteUpdateErrorEventReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetRouteUpdateErrorEventReceived.setStatus("current")
_JnxSRDRedundancySetRouteUpdateErrorEventDropped_Type = Unsigned32
_JnxSRDRedundancySetRouteUpdateErrorEventDropped_Object = MibTableColumn
jnxSRDRedundancySetRouteUpdateErrorEventDropped = _JnxSRDRedundancySetRouteUpdateErrorEventDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 16),
    _JnxSRDRedundancySetRouteUpdateErrorEventDropped_Type()
)
jnxSRDRedundancySetRouteUpdateErrorEventDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetRouteUpdateErrorEventDropped.setStatus("current")
_JnxSRDRedundancySetAcquireMasterManualReceived_Type = Unsigned32
_JnxSRDRedundancySetAcquireMasterManualReceived_Object = MibTableColumn
jnxSRDRedundancySetAcquireMasterManualReceived = _JnxSRDRedundancySetAcquireMasterManualReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 17),
    _JnxSRDRedundancySetAcquireMasterManualReceived_Type()
)
jnxSRDRedundancySetAcquireMasterManualReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetAcquireMasterManualReceived.setStatus("current")
_JnxSRDRedundancySetAcquireMasterManualDropped_Type = Unsigned32
_JnxSRDRedundancySetAcquireMasterManualDropped_Object = MibTableColumn
jnxSRDRedundancySetAcquireMasterManualDropped = _JnxSRDRedundancySetAcquireMasterManualDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 18),
    _JnxSRDRedundancySetAcquireMasterManualDropped_Type()
)
jnxSRDRedundancySetAcquireMasterManualDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetAcquireMasterManualDropped.setStatus("current")
_JnxSRDRedundancySetAcquireMasterAutoReceived_Type = Unsigned32
_JnxSRDRedundancySetAcquireMasterAutoReceived_Object = MibTableColumn
jnxSRDRedundancySetAcquireMasterAutoReceived = _JnxSRDRedundancySetAcquireMasterAutoReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 19),
    _JnxSRDRedundancySetAcquireMasterAutoReceived_Type()
)
jnxSRDRedundancySetAcquireMasterAutoReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetAcquireMasterAutoReceived.setStatus("current")
_JnxSRDRedundancySetAcquireMasterAutoDropped_Type = Unsigned32
_JnxSRDRedundancySetAcquireMasterAutoDropped_Object = MibTableColumn
jnxSRDRedundancySetAcquireMasterAutoDropped = _JnxSRDRedundancySetAcquireMasterAutoDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 20),
    _JnxSRDRedundancySetAcquireMasterAutoDropped_Type()
)
jnxSRDRedundancySetAcquireMasterAutoDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetAcquireMasterAutoDropped.setStatus("current")
_JnxSRDRedundancySetReleaseMasterManualReceived_Type = Unsigned32
_JnxSRDRedundancySetReleaseMasterManualReceived_Object = MibTableColumn
jnxSRDRedundancySetReleaseMasterManualReceived = _JnxSRDRedundancySetReleaseMasterManualReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 21),
    _JnxSRDRedundancySetReleaseMasterManualReceived_Type()
)
jnxSRDRedundancySetReleaseMasterManualReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetReleaseMasterManualReceived.setStatus("current")
_JnxSRDRedundancySetReleaseMasterManualDropped_Type = Unsigned32
_JnxSRDRedundancySetReleaseMasterManualDropped_Object = MibTableColumn
jnxSRDRedundancySetReleaseMasterManualDropped = _JnxSRDRedundancySetReleaseMasterManualDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 22),
    _JnxSRDRedundancySetReleaseMasterManualDropped_Type()
)
jnxSRDRedundancySetReleaseMasterManualDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetReleaseMasterManualDropped.setStatus("current")
_JnxSRDRedundancySetReleaseMasterAutoReceived_Type = Unsigned32
_JnxSRDRedundancySetReleaseMasterAutoReceived_Object = MibTableColumn
jnxSRDRedundancySetReleaseMasterAutoReceived = _JnxSRDRedundancySetReleaseMasterAutoReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 23),
    _JnxSRDRedundancySetReleaseMasterAutoReceived_Type()
)
jnxSRDRedundancySetReleaseMasterAutoReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetReleaseMasterAutoReceived.setStatus("current")
_JnxSRDRedundancySetReleaseMasterAutoDropped_Type = Unsigned32
_JnxSRDRedundancySetReleaseMasterAutoDropped_Object = MibTableColumn
jnxSRDRedundancySetReleaseMasterAutoDropped = _JnxSRDRedundancySetReleaseMasterAutoDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 24),
    _JnxSRDRedundancySetReleaseMasterAutoDropped_Type()
)
jnxSRDRedundancySetReleaseMasterAutoDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetReleaseMasterAutoDropped.setStatus("current")
_JnxSRDRedundancySetPeerAcquireMasterReceived_Type = Unsigned32
_JnxSRDRedundancySetPeerAcquireMasterReceived_Object = MibTableColumn
jnxSRDRedundancySetPeerAcquireMasterReceived = _JnxSRDRedundancySetPeerAcquireMasterReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 25),
    _JnxSRDRedundancySetPeerAcquireMasterReceived_Type()
)
jnxSRDRedundancySetPeerAcquireMasterReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetPeerAcquireMasterReceived.setStatus("current")
_JnxSRDRedundancySetPeerAcquireMasterDropped_Type = Unsigned32
_JnxSRDRedundancySetPeerAcquireMasterDropped_Object = MibTableColumn
jnxSRDRedundancySetPeerAcquireMasterDropped = _JnxSRDRedundancySetPeerAcquireMasterDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 26),
    _JnxSRDRedundancySetPeerAcquireMasterDropped_Type()
)
jnxSRDRedundancySetPeerAcquireMasterDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetPeerAcquireMasterDropped.setStatus("current")
_JnxSRDRedundancySetPeerReleaseMasterReceived_Type = Unsigned32
_JnxSRDRedundancySetPeerReleaseMasterReceived_Object = MibTableColumn
jnxSRDRedundancySetPeerReleaseMasterReceived = _JnxSRDRedundancySetPeerReleaseMasterReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 27),
    _JnxSRDRedundancySetPeerReleaseMasterReceived_Type()
)
jnxSRDRedundancySetPeerReleaseMasterReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetPeerReleaseMasterReceived.setStatus("current")
_JnxSRDRedundancySetPeerReleaseMasterDropped_Type = Unsigned32
_JnxSRDRedundancySetPeerReleaseMasterDropped_Object = MibTableColumn
jnxSRDRedundancySetPeerReleaseMasterDropped = _JnxSRDRedundancySetPeerReleaseMasterDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 2, 1, 1, 28),
    _JnxSRDRedundancySetPeerReleaseMasterDropped_Type()
)
jnxSRDRedundancySetPeerReleaseMasterDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSRDRedundancySetPeerReleaseMasterDropped.setStatus("current")

# Managed Objects groups


# Notification objects

jnxSRDRdeundancySetStateTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 0, 1)
)
jnxSRDRdeundancySetStateTransition.setObjects(
      *(("JUNIPER-SRD-MIB", "jnxSRDTrapRedundancyPeerIPAddressType"),
        ("JUNIPER-SRD-MIB", "jnxSRDTrapRedundancyPeerIPAddress"),
        ("JUNIPER-SRD-MIB", "jnxSRDTrapRedundancySetID"),
        ("JUNIPER-SRD-MIB", "jnxSRDTrapRedundancySetOldState"),
        ("JUNIPER-SRD-MIB", "jnxSRDTrapRedundancySetEvent"),
        ("JUNIPER-SRD-MIB", "jnxSRDTrapRedundancySetNewState"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    jnxSRDRdeundancySetStateTransition.setStatus(
        "current"
    )

jnxSRDRdeundancySetActionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 82, 1, 1, 0, 2)
)
jnxSRDRdeundancySetActionError.setObjects(
      *(("JUNIPER-SRD-MIB", "jnxSRDTrapRedundancyActionErrorCode"),
        ("JUNIPER-SRD-MIB", "jnxSRDTrapNotificationMessage"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    jnxSRDRdeundancySetActionError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SRD-MIB",
    **{"jnxSRDMIB": jnxSRDMIB,
       "jnxSRDNotification": jnxSRDNotification,
       "jnxSRDNotificationType": jnxSRDNotificationType,
       "jnxSRDRdeundancySetStateTransition": jnxSRDRdeundancySetStateTransition,
       "jnxSRDRdeundancySetActionError": jnxSRDRdeundancySetActionError,
       "jnxSRDNotificationObj": jnxSRDNotificationObj,
       "jnxSRDTrapRedundancySetID": jnxSRDTrapRedundancySetID,
       "jnxSRDTrapRedundancySetOldState": jnxSRDTrapRedundancySetOldState,
       "jnxSRDTrapRedundancySetEvent": jnxSRDTrapRedundancySetEvent,
       "jnxSRDTrapRedundancySetNewState": jnxSRDTrapRedundancySetNewState,
       "jnxSRDTrapNotificationMessage": jnxSRDTrapNotificationMessage,
       "jnxSRDTrapRedundancyPeerIPAddressType": jnxSRDTrapRedundancyPeerIPAddressType,
       "jnxSRDTrapRedundancyPeerIPAddress": jnxSRDTrapRedundancyPeerIPAddress,
       "jnxSRDTrapRedundancyActionErrorCode": jnxSRDTrapRedundancyActionErrorCode,
       "jnxSRDRedundancyGroup": jnxSRDRedundancyGroup,
       "jnxSRDRedundancyGroupTable": jnxSRDRedundancyGroupTable,
       "jnxSRDRedundancyGroupEntry": jnxSRDRedundancyGroupEntry,
       "jnxSRDRedundancyGroupID": jnxSRDRedundancyGroupID,
       "jnxSRDRedundancySetID": jnxSRDRedundancySetID,
       "jnxSRDRedundancyGroupTotalPeer": jnxSRDRedundancyGroupTotalPeer,
       "jnxSRDRedundancyGroupConnStatus": jnxSRDRedundancyGroupConnStatus,
       "jnxSRDRedundancySRDIccpConnStatus": jnxSRDRedundancySRDIccpConnStatus,
       "jnxSRDRedundancySRDRemoteIPAddressType": jnxSRDRedundancySRDRemoteIPAddressType,
       "jnxSRDRedundancySRDRemoteIPAddress": jnxSRDRedundancySRDRemoteIPAddress,
       "jnxSRDRedundancySetState": jnxSRDRedundancySetState,
       "jnxSRDRedundancySetPeerState": jnxSRDRedundancySetPeerState,
       "jnxSRDRedundancySetHealthStatus": jnxSRDRedundancySetHealthStatus,
       "jnxSRDRedundancySetLinkDownEventReceived": jnxSRDRedundancySetLinkDownEventReceived,
       "jnxSRDRedundancySetLinkDownEventDropped": jnxSRDRedundancySetLinkDownEventDropped,
       "jnxSRDRedundancySetRpdRestartEventReceived": jnxSRDRedundancySetRpdRestartEventReceived,
       "jnxSRDRedundancySetRpdRestartEventDropped": jnxSRDRedundancySetRpdRestartEventDropped,
       "jnxSRDRedundancySetRouteUpdateErrorEventReceived": jnxSRDRedundancySetRouteUpdateErrorEventReceived,
       "jnxSRDRedundancySetRouteUpdateErrorEventDropped": jnxSRDRedundancySetRouteUpdateErrorEventDropped,
       "jnxSRDRedundancySetAcquireMasterManualReceived": jnxSRDRedundancySetAcquireMasterManualReceived,
       "jnxSRDRedundancySetAcquireMasterManualDropped": jnxSRDRedundancySetAcquireMasterManualDropped,
       "jnxSRDRedundancySetAcquireMasterAutoReceived": jnxSRDRedundancySetAcquireMasterAutoReceived,
       "jnxSRDRedundancySetAcquireMasterAutoDropped": jnxSRDRedundancySetAcquireMasterAutoDropped,
       "jnxSRDRedundancySetReleaseMasterManualReceived": jnxSRDRedundancySetReleaseMasterManualReceived,
       "jnxSRDRedundancySetReleaseMasterManualDropped": jnxSRDRedundancySetReleaseMasterManualDropped,
       "jnxSRDRedundancySetReleaseMasterAutoReceived": jnxSRDRedundancySetReleaseMasterAutoReceived,
       "jnxSRDRedundancySetReleaseMasterAutoDropped": jnxSRDRedundancySetReleaseMasterAutoDropped,
       "jnxSRDRedundancySetPeerAcquireMasterReceived": jnxSRDRedundancySetPeerAcquireMasterReceived,
       "jnxSRDRedundancySetPeerAcquireMasterDropped": jnxSRDRedundancySetPeerAcquireMasterDropped,
       "jnxSRDRedundancySetPeerReleaseMasterReceived": jnxSRDRedundancySetPeerReleaseMasterReceived,
       "jnxSRDRedundancySetPeerReleaseMasterDropped": jnxSRDRedundancySetPeerReleaseMasterDropped}
)
