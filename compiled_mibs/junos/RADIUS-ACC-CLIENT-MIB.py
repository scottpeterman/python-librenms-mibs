# SNMP MIB module (RADIUS-ACC-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\RADIUS-ACC-CLIENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:21 2025
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

radiusAccClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2)
)
if mibBuilder.loadTexts:
    radiusAccClientMIB.setRevisions(
        ("2006-08-21 00:00",
         "1999-06-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusMIB_ObjectIdentity = ObjectIdentity
radiusMIB = _RadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67)
)
if mibBuilder.loadTexts:
    radiusMIB.setStatus("current")
_RadiusAccounting_ObjectIdentity = ObjectIdentity
radiusAccounting = _RadiusAccounting_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2)
)
_RadiusAccClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusAccClientMIBObjects = _RadiusAccClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1)
)
_RadiusAccClient_ObjectIdentity = ObjectIdentity
radiusAccClient = _RadiusAccClient_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1)
)
_RadiusAccClientInvalidServerAddresses_Type = Counter32
_RadiusAccClientInvalidServerAddresses_Object = MibScalar
radiusAccClientInvalidServerAddresses = _RadiusAccClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 1),
    _RadiusAccClientInvalidServerAddresses_Type()
)
radiusAccClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientInvalidServerAddresses.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientInvalidServerAddresses.setUnits("packets")
_RadiusAccClientIdentifier_Type = SnmpAdminString
_RadiusAccClientIdentifier_Object = MibScalar
radiusAccClientIdentifier = _RadiusAccClientIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 2),
    _RadiusAccClientIdentifier_Type()
)
radiusAccClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientIdentifier.setStatus("current")
_RadiusAccServerTable_Object = MibTable
radiusAccServerTable = _RadiusAccServerTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAccServerTable.setStatus("deprecated")
_RadiusAccServerEntry_Object = MibTableRow
radiusAccServerEntry = _RadiusAccServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1)
)
radiusAccServerEntry.setIndexNames(
    (0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAccServerEntry.setStatus("deprecated")


class _RadiusAccServerIndex_Type(Integer32):
    """Custom type radiusAccServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAccServerIndex_Type.__name__ = "Integer32"
_RadiusAccServerIndex_Object = MibTableColumn
radiusAccServerIndex = _RadiusAccServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 1),
    _RadiusAccServerIndex_Type()
)
radiusAccServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAccServerIndex.setStatus("deprecated")
_RadiusAccServerAddress_Type = IpAddress
_RadiusAccServerAddress_Object = MibTableColumn
radiusAccServerAddress = _RadiusAccServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 2),
    _RadiusAccServerAddress_Type()
)
radiusAccServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServerAddress.setStatus("deprecated")


class _RadiusAccClientServerPortNumber_Type(Integer32):
    """Custom type radiusAccClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAccClientServerPortNumber_Type.__name__ = "Integer32"
_RadiusAccClientServerPortNumber_Object = MibTableColumn
radiusAccClientServerPortNumber = _RadiusAccClientServerPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 3),
    _RadiusAccClientServerPortNumber_Type()
)
radiusAccClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientServerPortNumber.setStatus("deprecated")
_RadiusAccClientRoundTripTime_Type = TimeTicks
_RadiusAccClientRoundTripTime_Object = MibTableColumn
radiusAccClientRoundTripTime = _RadiusAccClientRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 4),
    _RadiusAccClientRoundTripTime_Type()
)
radiusAccClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientRoundTripTime.setStatus("deprecated")
_RadiusAccClientRequests_Type = Counter32
_RadiusAccClientRequests_Object = MibTableColumn
radiusAccClientRequests = _RadiusAccClientRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 5),
    _RadiusAccClientRequests_Type()
)
radiusAccClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientRequests.setUnits("packets")
_RadiusAccClientRetransmissions_Type = Counter32
_RadiusAccClientRetransmissions_Object = MibTableColumn
radiusAccClientRetransmissions = _RadiusAccClientRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 6),
    _RadiusAccClientRetransmissions_Type()
)
radiusAccClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientRetransmissions.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientRetransmissions.setUnits("packets")
_RadiusAccClientResponses_Type = Counter32
_RadiusAccClientResponses_Object = MibTableColumn
radiusAccClientResponses = _RadiusAccClientResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 7),
    _RadiusAccClientResponses_Type()
)
radiusAccClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientResponses.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientResponses.setUnits("packets")
_RadiusAccClientMalformedResponses_Type = Counter32
_RadiusAccClientMalformedResponses_Object = MibTableColumn
radiusAccClientMalformedResponses = _RadiusAccClientMalformedResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 8),
    _RadiusAccClientMalformedResponses_Type()
)
radiusAccClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientMalformedResponses.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientMalformedResponses.setUnits("packets")
_RadiusAccClientBadAuthenticators_Type = Counter32
_RadiusAccClientBadAuthenticators_Object = MibTableColumn
radiusAccClientBadAuthenticators = _RadiusAccClientBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 9),
    _RadiusAccClientBadAuthenticators_Type()
)
radiusAccClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientBadAuthenticators.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientBadAuthenticators.setUnits("packets")
_RadiusAccClientPendingRequests_Type = Gauge32
_RadiusAccClientPendingRequests_Object = MibTableColumn
radiusAccClientPendingRequests = _RadiusAccClientPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 10),
    _RadiusAccClientPendingRequests_Type()
)
radiusAccClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientPendingRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientPendingRequests.setUnits("packets")
_RadiusAccClientTimeouts_Type = Counter32
_RadiusAccClientTimeouts_Object = MibTableColumn
radiusAccClientTimeouts = _RadiusAccClientTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 11),
    _RadiusAccClientTimeouts_Type()
)
radiusAccClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientTimeouts.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientTimeouts.setUnits("timeouts")
_RadiusAccClientUnknownTypes_Type = Counter32
_RadiusAccClientUnknownTypes_Object = MibTableColumn
radiusAccClientUnknownTypes = _RadiusAccClientUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 12),
    _RadiusAccClientUnknownTypes_Type()
)
radiusAccClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientUnknownTypes.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientUnknownTypes.setUnits("packets")
_RadiusAccClientPacketsDropped_Type = Counter32
_RadiusAccClientPacketsDropped_Object = MibTableColumn
radiusAccClientPacketsDropped = _RadiusAccClientPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 13),
    _RadiusAccClientPacketsDropped_Type()
)
radiusAccClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientPacketsDropped.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccClientPacketsDropped.setUnits("packets")
_RadiusAccServerExtTable_Object = MibTable
radiusAccServerExtTable = _RadiusAccServerExtTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    radiusAccServerExtTable.setStatus("current")
_RadiusAccServerExtEntry_Object = MibTableRow
radiusAccServerExtEntry = _RadiusAccServerExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1)
)
radiusAccServerExtEntry.setIndexNames(
    (0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerExtIndex"),
)
if mibBuilder.loadTexts:
    radiusAccServerExtEntry.setStatus("current")


class _RadiusAccServerExtIndex_Type(Integer32):
    """Custom type radiusAccServerExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAccServerExtIndex_Type.__name__ = "Integer32"
_RadiusAccServerExtIndex_Object = MibTableColumn
radiusAccServerExtIndex = _RadiusAccServerExtIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 1),
    _RadiusAccServerExtIndex_Type()
)
radiusAccServerExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAccServerExtIndex.setStatus("current")
_RadiusAccServerInetAddressType_Type = InetAddressType
_RadiusAccServerInetAddressType_Object = MibTableColumn
radiusAccServerInetAddressType = _RadiusAccServerInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 2),
    _RadiusAccServerInetAddressType_Type()
)
radiusAccServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServerInetAddressType.setStatus("current")
_RadiusAccServerInetAddress_Type = InetAddress
_RadiusAccServerInetAddress_Object = MibTableColumn
radiusAccServerInetAddress = _RadiusAccServerInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 3),
    _RadiusAccServerInetAddress_Type()
)
radiusAccServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServerInetAddress.setStatus("current")


class _RadiusAccClientServerInetPortNumber_Type(InetPortNumber):
    """Custom type radiusAccClientServerInetPortNumber based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusAccClientServerInetPortNumber_Type.__name__ = "InetPortNumber"
_RadiusAccClientServerInetPortNumber_Object = MibTableColumn
radiusAccClientServerInetPortNumber = _RadiusAccClientServerInetPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 4),
    _RadiusAccClientServerInetPortNumber_Type()
)
radiusAccClientServerInetPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientServerInetPortNumber.setStatus("current")
_RadiusAccClientExtRoundTripTime_Type = TimeTicks
_RadiusAccClientExtRoundTripTime_Object = MibTableColumn
radiusAccClientExtRoundTripTime = _RadiusAccClientExtRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 5),
    _RadiusAccClientExtRoundTripTime_Type()
)
radiusAccClientExtRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtRoundTripTime.setStatus("current")
_RadiusAccClientExtRequests_Type = Counter32
_RadiusAccClientExtRequests_Object = MibTableColumn
radiusAccClientExtRequests = _RadiusAccClientExtRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 6),
    _RadiusAccClientExtRequests_Type()
)
radiusAccClientExtRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtRequests.setUnits("packets")
_RadiusAccClientExtRetransmissions_Type = Counter32
_RadiusAccClientExtRetransmissions_Object = MibTableColumn
radiusAccClientExtRetransmissions = _RadiusAccClientExtRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 7),
    _RadiusAccClientExtRetransmissions_Type()
)
radiusAccClientExtRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtRetransmissions.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtRetransmissions.setUnits("packets")
_RadiusAccClientExtResponses_Type = Counter32
_RadiusAccClientExtResponses_Object = MibTableColumn
radiusAccClientExtResponses = _RadiusAccClientExtResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 8),
    _RadiusAccClientExtResponses_Type()
)
radiusAccClientExtResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtResponses.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtResponses.setUnits("packets")
_RadiusAccClientExtMalformedResponses_Type = Counter32
_RadiusAccClientExtMalformedResponses_Object = MibTableColumn
radiusAccClientExtMalformedResponses = _RadiusAccClientExtMalformedResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 9),
    _RadiusAccClientExtMalformedResponses_Type()
)
radiusAccClientExtMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtMalformedResponses.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtMalformedResponses.setUnits("packets")
_RadiusAccClientExtBadAuthenticators_Type = Counter32
_RadiusAccClientExtBadAuthenticators_Object = MibTableColumn
radiusAccClientExtBadAuthenticators = _RadiusAccClientExtBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 10),
    _RadiusAccClientExtBadAuthenticators_Type()
)
radiusAccClientExtBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtBadAuthenticators.setUnits("packets")
_RadiusAccClientExtPendingRequests_Type = Gauge32
_RadiusAccClientExtPendingRequests_Object = MibTableColumn
radiusAccClientExtPendingRequests = _RadiusAccClientExtPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 11),
    _RadiusAccClientExtPendingRequests_Type()
)
radiusAccClientExtPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtPendingRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtPendingRequests.setUnits("packets")
_RadiusAccClientExtTimeouts_Type = Counter32
_RadiusAccClientExtTimeouts_Object = MibTableColumn
radiusAccClientExtTimeouts = _RadiusAccClientExtTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 12),
    _RadiusAccClientExtTimeouts_Type()
)
radiusAccClientExtTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtTimeouts.setUnits("timeouts")
_RadiusAccClientExtUnknownTypes_Type = Counter32
_RadiusAccClientExtUnknownTypes_Object = MibTableColumn
radiusAccClientExtUnknownTypes = _RadiusAccClientExtUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 13),
    _RadiusAccClientExtUnknownTypes_Type()
)
radiusAccClientExtUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtUnknownTypes.setUnits("packets")
_RadiusAccClientExtPacketsDropped_Type = Counter32
_RadiusAccClientExtPacketsDropped_Object = MibTableColumn
radiusAccClientExtPacketsDropped = _RadiusAccClientExtPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 14),
    _RadiusAccClientExtPacketsDropped_Type()
)
radiusAccClientExtPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientExtPacketsDropped.setUnits("packets")
_RadiusAccClientCounterDiscontinuity_Type = TimeTicks
_RadiusAccClientCounterDiscontinuity_Object = MibTableColumn
radiusAccClientCounterDiscontinuity = _RadiusAccClientCounterDiscontinuity_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 15),
    _RadiusAccClientCounterDiscontinuity_Type()
)
radiusAccClientCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccClientCounterDiscontinuity.setUnits("centiseconds")
_RadiusAccClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusAccClientMIBConformance = _RadiusAccClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2)
)
_RadiusAccClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAccClientMIBCompliances = _RadiusAccClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1)
)
_RadiusAccClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusAccClientMIBGroups = _RadiusAccClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2)
)

# Managed Objects groups

radiusAccClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 1)
)
radiusAccClientMIBGroup.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientIdentifier"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientInvalidServerAddresses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRoundTripTime"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRequests"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRetransmissions"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientResponses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMalformedResponses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientBadAuthenticators"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPendingRequests"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientTimeouts"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientUnknownTypes"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPacketsDropped"))
)
if mibBuilder.loadTexts:
    radiusAccClientMIBGroup.setStatus("deprecated")

radiusAccClientExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 2)
)
radiusAccClientExtMIBGroup.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientIdentifier"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientInvalidServerAddresses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerInetAddressType"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerInetAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerInetPortNumber"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtRoundTripTime"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtRequests"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtRetransmissions"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtResponses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtMalformedResponses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtBadAuthenticators"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtPendingRequests"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtTimeouts"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtUnknownTypes"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtPacketsDropped"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientCounterDiscontinuity"))
)
if mibBuilder.loadTexts:
    radiusAccClientExtMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAccClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1, 1)
)
radiusAccClientMIBCompliance.setObjects(
    ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAccClientMIBCompliance.setStatus(
        "deprecated"
    )

radiusAccClientExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1, 2)
)
radiusAccClientExtMIBCompliance.setObjects(
    ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientExtMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAccClientExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    **{"radiusMIB": radiusMIB,
       "radiusAccounting": radiusAccounting,
       "radiusAccClientMIB": radiusAccClientMIB,
       "radiusAccClientMIBObjects": radiusAccClientMIBObjects,
       "radiusAccClient": radiusAccClient,
       "radiusAccClientInvalidServerAddresses": radiusAccClientInvalidServerAddresses,
       "radiusAccClientIdentifier": radiusAccClientIdentifier,
       "radiusAccServerTable": radiusAccServerTable,
       "radiusAccServerEntry": radiusAccServerEntry,
       "radiusAccServerIndex": radiusAccServerIndex,
       "radiusAccServerAddress": radiusAccServerAddress,
       "radiusAccClientServerPortNumber": radiusAccClientServerPortNumber,
       "radiusAccClientRoundTripTime": radiusAccClientRoundTripTime,
       "radiusAccClientRequests": radiusAccClientRequests,
       "radiusAccClientRetransmissions": radiusAccClientRetransmissions,
       "radiusAccClientResponses": radiusAccClientResponses,
       "radiusAccClientMalformedResponses": radiusAccClientMalformedResponses,
       "radiusAccClientBadAuthenticators": radiusAccClientBadAuthenticators,
       "radiusAccClientPendingRequests": radiusAccClientPendingRequests,
       "radiusAccClientTimeouts": radiusAccClientTimeouts,
       "radiusAccClientUnknownTypes": radiusAccClientUnknownTypes,
       "radiusAccClientPacketsDropped": radiusAccClientPacketsDropped,
       "radiusAccServerExtTable": radiusAccServerExtTable,
       "radiusAccServerExtEntry": radiusAccServerExtEntry,
       "radiusAccServerExtIndex": radiusAccServerExtIndex,
       "radiusAccServerInetAddressType": radiusAccServerInetAddressType,
       "radiusAccServerInetAddress": radiusAccServerInetAddress,
       "radiusAccClientServerInetPortNumber": radiusAccClientServerInetPortNumber,
       "radiusAccClientExtRoundTripTime": radiusAccClientExtRoundTripTime,
       "radiusAccClientExtRequests": radiusAccClientExtRequests,
       "radiusAccClientExtRetransmissions": radiusAccClientExtRetransmissions,
       "radiusAccClientExtResponses": radiusAccClientExtResponses,
       "radiusAccClientExtMalformedResponses": radiusAccClientExtMalformedResponses,
       "radiusAccClientExtBadAuthenticators": radiusAccClientExtBadAuthenticators,
       "radiusAccClientExtPendingRequests": radiusAccClientExtPendingRequests,
       "radiusAccClientExtTimeouts": radiusAccClientExtTimeouts,
       "radiusAccClientExtUnknownTypes": radiusAccClientExtUnknownTypes,
       "radiusAccClientExtPacketsDropped": radiusAccClientExtPacketsDropped,
       "radiusAccClientCounterDiscontinuity": radiusAccClientCounterDiscontinuity,
       "radiusAccClientMIBConformance": radiusAccClientMIBConformance,
       "radiusAccClientMIBCompliances": radiusAccClientMIBCompliances,
       "radiusAccClientMIBCompliance": radiusAccClientMIBCompliance,
       "radiusAccClientExtMIBCompliance": radiusAccClientExtMIBCompliance,
       "radiusAccClientMIBGroups": radiusAccClientMIBGroups,
       "radiusAccClientMIBGroup": radiusAccClientMIBGroup,
       "radiusAccClientExtMIBGroup": radiusAccClientExtMIBGroup}
)
