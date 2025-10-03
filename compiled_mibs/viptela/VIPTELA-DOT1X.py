# SNMP MIB module (VIPTELA-DOT1X) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-DOT1X
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:01 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_dot1x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 19)
)
if mibBuilder.loadTexts:
    viptela_dot1x.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Dot1xAuthMethod(TextualConvention, Integer32):
    status = "current"
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
        *(("radius", 0),
          ("radius-MAB", 1),
          ("local-MAB", 2),
          ("local-Auth", 3))
    )



class EapMethod(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("mD5", 1),
          ("pEAP-MS-CHAPv2", 2),
          ("eAP-TLS", 3))
    )



class Dot1xAuthState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("authenticated", 1),
          ("authenticating", 2),
          ("exception", 3),
          ("guest", 4),
          ("authFail", 5),
          ("authReject", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1)
)
_Dot1xInterfacesTable_Object = MibTable
dot1xInterfacesTable = _Dot1xInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xInterfacesTable.setStatus("current")
_Dot1xInterfacesEntry_Object = MibTableRow
dot1xInterfacesEntry = _Dot1xInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1)
)
dot1xInterfacesEntry.setIndexNames(
    (0, "VIPTELA-DOT1X", "dot1xInterfacesIfName"),
)
if mibBuilder.loadTexts:
    dot1xInterfacesEntry.setStatus("current")


class _Dot1xInterfacesIfName_Type(String):
    """Custom type dot1xInterfacesIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot1xInterfacesIfName_Type.__name__ = "String"
_Dot1xInterfacesIfName_Object = MibTableColumn
dot1xInterfacesIfName = _Dot1xInterfacesIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 1),
    _Dot1xInterfacesIfName_Type()
)
dot1xInterfacesIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xInterfacesIfName.setStatus("current")


class _Dot1xInterfacesOperState_Type(Integer32):
    """Custom type dot1xInterfacesOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_Dot1xInterfacesOperState_Type.__name__ = "Integer32"
_Dot1xInterfacesOperState_Object = MibTableColumn
dot1xInterfacesOperState = _Dot1xInterfacesOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 2),
    _Dot1xInterfacesOperState_Type()
)
dot1xInterfacesOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesOperState.setStatus("current")


class _Dot1xInterfacesHostMode_Type(Integer32):
    """Custom type dot1xInterfacesHostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single-Host", 0),
          ("multi-Auth", 1),
          ("multi-Host", 2))
    )


_Dot1xInterfacesHostMode_Type.__name__ = "Integer32"
_Dot1xInterfacesHostMode_Object = MibTableColumn
dot1xInterfacesHostMode = _Dot1xInterfacesHostMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 3),
    _Dot1xInterfacesHostMode_Type()
)
dot1xInterfacesHostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesHostMode.setStatus("current")


class _Dot1xInterfacesCtrlDir_Type(Integer32):
    """Custom type dot1xInterfacesCtrlDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("both", 1))
    )


_Dot1xInterfacesCtrlDir_Type.__name__ = "Integer32"
_Dot1xInterfacesCtrlDir_Object = MibTableColumn
dot1xInterfacesCtrlDir = _Dot1xInterfacesCtrlDir_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 4),
    _Dot1xInterfacesCtrlDir_Type()
)
dot1xInterfacesCtrlDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesCtrlDir.setStatus("current")
_Dot1xInterfacesMabServer_Type = TruthValue
_Dot1xInterfacesMabServer_Object = MibTableColumn
dot1xInterfacesMabServer = _Dot1xInterfacesMabServer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 5),
    _Dot1xInterfacesMabServer_Type()
)
dot1xInterfacesMabServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesMabServer.setStatus("current")
_Dot1xInterfacesMabLocal_Type = TruthValue
_Dot1xInterfacesMabLocal_Object = MibTableColumn
dot1xInterfacesMabLocal = _Dot1xInterfacesMabLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 6),
    _Dot1xInterfacesMabLocal_Type()
)
dot1xInterfacesMabLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesMabLocal.setStatus("current")
_Dot1xInterfacesWakeOnLan_Type = TruthValue
_Dot1xInterfacesWakeOnLan_Object = MibTableColumn
dot1xInterfacesWakeOnLan = _Dot1xInterfacesWakeOnLan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 7),
    _Dot1xInterfacesWakeOnLan_Type()
)
dot1xInterfacesWakeOnLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesWakeOnLan.setStatus("current")
_Dot1xInterfacesReauthTimeout_Type = UnsignedShort
_Dot1xInterfacesReauthTimeout_Object = MibTableColumn
dot1xInterfacesReauthTimeout = _Dot1xInterfacesReauthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 8),
    _Dot1xInterfacesReauthTimeout_Type()
)
dot1xInterfacesReauthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesReauthTimeout.setStatus("current")
_Dot1xInterfacesInactivityTimeout_Type = UnsignedShort
_Dot1xInterfacesInactivityTimeout_Object = MibTableColumn
dot1xInterfacesInactivityTimeout = _Dot1xInterfacesInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 9),
    _Dot1xInterfacesInactivityTimeout_Type()
)
dot1xInterfacesInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesInactivityTimeout.setStatus("current")
_Dot1xInterfacesGuestVlan_Type = Integer32
_Dot1xInterfacesGuestVlan_Object = MibTableColumn
dot1xInterfacesGuestVlan = _Dot1xInterfacesGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 10),
    _Dot1xInterfacesGuestVlan_Type()
)
dot1xInterfacesGuestVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesGuestVlan.setStatus("current")
_Dot1xInterfacesAuthFailVlan_Type = Integer32
_Dot1xInterfacesAuthFailVlan_Object = MibTableColumn
dot1xInterfacesAuthFailVlan = _Dot1xInterfacesAuthFailVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 11),
    _Dot1xInterfacesAuthFailVlan_Type()
)
dot1xInterfacesAuthFailVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesAuthFailVlan.setStatus("current")
_Dot1xInterfacesAuthRejectVlan_Type = Integer32
_Dot1xInterfacesAuthRejectVlan_Object = MibTableColumn
dot1xInterfacesAuthRejectVlan = _Dot1xInterfacesAuthRejectVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 12),
    _Dot1xInterfacesAuthRejectVlan_Type()
)
dot1xInterfacesAuthRejectVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesAuthRejectVlan.setStatus("current")
_Dot1xInterfacesDefaultVlan_Type = Integer32
_Dot1xInterfacesDefaultVlan_Object = MibTableColumn
dot1xInterfacesDefaultVlan = _Dot1xInterfacesDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 13),
    _Dot1xInterfacesDefaultVlan_Type()
)
dot1xInterfacesDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesDefaultVlan.setStatus("current")
_Dot1xInterfacesPrimaryRadiusServer_Type = InetAddressIP
_Dot1xInterfacesPrimaryRadiusServer_Object = MibTableColumn
dot1xInterfacesPrimaryRadiusServer = _Dot1xInterfacesPrimaryRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 14),
    _Dot1xInterfacesPrimaryRadiusServer_Type()
)
dot1xInterfacesPrimaryRadiusServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesPrimaryRadiusServer.setStatus("current")
_Dot1xInterfacesSecondaryRadiusServer_Type = InetAddressIP
_Dot1xInterfacesSecondaryRadiusServer_Object = MibTableColumn
dot1xInterfacesSecondaryRadiusServer = _Dot1xInterfacesSecondaryRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 15),
    _Dot1xInterfacesSecondaryRadiusServer_Type()
)
dot1xInterfacesSecondaryRadiusServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesSecondaryRadiusServer.setStatus("current")
_Dot1xInterfacesAccountingInterval_Type = UnsignedShort
_Dot1xInterfacesAccountingInterval_Object = MibTableColumn
dot1xInterfacesAccountingInterval = _Dot1xInterfacesAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 16),
    _Dot1xInterfacesAccountingInterval_Type()
)
dot1xInterfacesAccountingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesAccountingInterval.setStatus("current")


class _Dot1xInterfacesNasIdentifier_Type(String):
    """Custom type dot1xInterfacesNasIdentifier based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Dot1xInterfacesNasIdentifier_Type.__name__ = "String"
_Dot1xInterfacesNasIdentifier_Object = MibTableColumn
dot1xInterfacesNasIdentifier = _Dot1xInterfacesNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 17),
    _Dot1xInterfacesNasIdentifier_Type()
)
dot1xInterfacesNasIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesNasIdentifier.setStatus("current")
_Dot1xInterfacesNasIPAddr_Type = InetAddressIP
_Dot1xInterfacesNasIPAddr_Object = MibTableColumn
dot1xInterfacesNasIPAddr = _Dot1xInterfacesNasIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 18),
    _Dot1xInterfacesNasIPAddr_Type()
)
dot1xInterfacesNasIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesNasIPAddr.setStatus("current")
_Dot1xInterfacesNumClients_Type = Unsigned32
_Dot1xInterfacesNumClients_Object = MibTableColumn
dot1xInterfacesNumClients = _Dot1xInterfacesNumClients_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 1, 1, 19),
    _Dot1xInterfacesNumClients_Type()
)
dot1xInterfacesNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInterfacesNumClients.setStatus("current")
_Dot1xClientsTable_Object = MibTable
dot1xClientsTable = _Dot1xClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2)
)
if mibBuilder.loadTexts:
    dot1xClientsTable.setStatus("current")
_Dot1xClientsEntry_Object = MibTableRow
dot1xClientsEntry = _Dot1xClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1)
)
dot1xClientsEntry.setIndexNames(
    (0, "VIPTELA-DOT1X", "dot1xClientsIfName"),
    (0, "VIPTELA-DOT1X", "dot1xClientsMacAddress"),
)
if mibBuilder.loadTexts:
    dot1xClientsEntry.setStatus("current")


class _Dot1xClientsIfName_Type(String):
    """Custom type dot1xClientsIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot1xClientsIfName_Type.__name__ = "String"
_Dot1xClientsIfName_Object = MibTableColumn
dot1xClientsIfName = _Dot1xClientsIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 1),
    _Dot1xClientsIfName_Type()
)
dot1xClientsIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xClientsIfName.setStatus("current")
_Dot1xClientsMacAddress_Type = String
_Dot1xClientsMacAddress_Object = MibTableColumn
dot1xClientsMacAddress = _Dot1xClientsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 2),
    _Dot1xClientsMacAddress_Type()
)
dot1xClientsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xClientsMacAddress.setStatus("current")
_Dot1xClientsAuthState_Type = Dot1xAuthState
_Dot1xClientsAuthState_Object = MibTableColumn
dot1xClientsAuthState = _Dot1xClientsAuthState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 3),
    _Dot1xClientsAuthState_Type()
)
dot1xClientsAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsAuthState.setStatus("current")
_Dot1xClientsAuthMethod_Type = Dot1xAuthMethod
_Dot1xClientsAuthMethod_Object = MibTableColumn
dot1xClientsAuthMethod = _Dot1xClientsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 4),
    _Dot1xClientsAuthMethod_Type()
)
dot1xClientsAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsAuthMethod.setStatus("current")
_Dot1xClientsVlan_Type = Integer32
_Dot1xClientsVlan_Object = MibTableColumn
dot1xClientsVlan = _Dot1xClientsVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 5),
    _Dot1xClientsVlan_Type()
)
dot1xClientsVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsVlan.setStatus("current")
_Dot1xClientsVpn_Type = Integer32
_Dot1xClientsVpn_Object = MibTableColumn
dot1xClientsVpn = _Dot1xClientsVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 6),
    _Dot1xClientsVpn_Type()
)
dot1xClientsVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsVpn.setStatus("current")
_Dot1xClientsEapMethod_Type = String
_Dot1xClientsEapMethod_Object = MibTableColumn
dot1xClientsEapMethod = _Dot1xClientsEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 7),
    _Dot1xClientsEapMethod_Type()
)
dot1xClientsEapMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapMethod.setStatus("current")
_Dot1xClientsUsername_Type = String
_Dot1xClientsUsername_Object = MibTableColumn
dot1xClientsUsername = _Dot1xClientsUsername_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 8),
    _Dot1xClientsUsername_Type()
)
dot1xClientsUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsUsername.setStatus("current")
_Dot1xClientsSessionTime_Type = Unsigned32
_Dot1xClientsSessionTime_Object = MibTableColumn
dot1xClientsSessionTime = _Dot1xClientsSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 9),
    _Dot1xClientsSessionTime_Type()
)
dot1xClientsSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsSessionTime.setStatus("current")
_Dot1xClientsConnectedTime_Type = Unsigned32
_Dot1xClientsConnectedTime_Object = MibTableColumn
dot1xClientsConnectedTime = _Dot1xClientsConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 10),
    _Dot1xClientsConnectedTime_Type()
)
dot1xClientsConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsConnectedTime.setStatus("current")
_Dot1xClientsInactiveTime_Type = Unsigned32
_Dot1xClientsInactiveTime_Object = MibTableColumn
dot1xClientsInactiveTime = _Dot1xClientsInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 11),
    _Dot1xClientsInactiveTime_Type()
)
dot1xClientsInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsInactiveTime.setStatus("current")
_Dot1xClientsSessionId_Type = String
_Dot1xClientsSessionId_Object = MibTableColumn
dot1xClientsSessionId = _Dot1xClientsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 12),
    _Dot1xClientsSessionId_Type()
)
dot1xClientsSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsSessionId.setStatus("current")
_Dot1xClientsEapolFramesRx_Type = Unsigned32
_Dot1xClientsEapolFramesRx_Object = MibTableColumn
dot1xClientsEapolFramesRx = _Dot1xClientsEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 13),
    _Dot1xClientsEapolFramesRx_Type()
)
dot1xClientsEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolFramesRx.setStatus("current")
_Dot1xClientsEapolFramesTx_Type = Unsigned32
_Dot1xClientsEapolFramesTx_Object = MibTableColumn
dot1xClientsEapolFramesTx = _Dot1xClientsEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 14),
    _Dot1xClientsEapolFramesTx_Type()
)
dot1xClientsEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolFramesTx.setStatus("current")
_Dot1xClientsEapolStartFramesRx_Type = Unsigned32
_Dot1xClientsEapolStartFramesRx_Object = MibTableColumn
dot1xClientsEapolStartFramesRx = _Dot1xClientsEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 15),
    _Dot1xClientsEapolStartFramesRx_Type()
)
dot1xClientsEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolStartFramesRx.setStatus("current")
_Dot1xClientsEapolLogoffFramesRx_Type = Unsigned32
_Dot1xClientsEapolLogoffFramesRx_Object = MibTableColumn
dot1xClientsEapolLogoffFramesRx = _Dot1xClientsEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 16),
    _Dot1xClientsEapolLogoffFramesRx_Type()
)
dot1xClientsEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolLogoffFramesRx.setStatus("current")
_Dot1xClientsEapolRequestIdFramesTx_Type = Unsigned32
_Dot1xClientsEapolRequestIdFramesTx_Object = MibTableColumn
dot1xClientsEapolRequestIdFramesTx = _Dot1xClientsEapolRequestIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 17),
    _Dot1xClientsEapolRequestIdFramesTx_Type()
)
dot1xClientsEapolRequestIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolRequestIdFramesTx.setStatus("current")
_Dot1xClientsEapolResponseIdFramesRx_Type = Unsigned32
_Dot1xClientsEapolResponseIdFramesRx_Object = MibTableColumn
dot1xClientsEapolResponseIdFramesRx = _Dot1xClientsEapolResponseIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 18),
    _Dot1xClientsEapolResponseIdFramesRx_Type()
)
dot1xClientsEapolResponseIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolResponseIdFramesRx.setStatus("current")
_Dot1xClientsEapolRequestFramesTx_Type = Unsigned32
_Dot1xClientsEapolRequestFramesTx_Object = MibTableColumn
dot1xClientsEapolRequestFramesTx = _Dot1xClientsEapolRequestFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 19),
    _Dot1xClientsEapolRequestFramesTx_Type()
)
dot1xClientsEapolRequestFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolRequestFramesTx.setStatus("current")
_Dot1xClientsEapolResponseFramesRx_Type = Unsigned32
_Dot1xClientsEapolResponseFramesRx_Object = MibTableColumn
dot1xClientsEapolResponseFramesRx = _Dot1xClientsEapolResponseFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 2, 1, 20),
    _Dot1xClientsEapolResponseFramesRx_Type()
)
dot1xClientsEapolResponseFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xClientsEapolResponseFramesRx.setStatus("current")
_Dot1xRadiusTable_Object = MibTable
dot1xRadiusTable = _Dot1xRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3)
)
if mibBuilder.loadTexts:
    dot1xRadiusTable.setStatus("current")
_Dot1xRadiusEntry_Object = MibTableRow
dot1xRadiusEntry = _Dot1xRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1)
)
dot1xRadiusEntry.setIndexNames(
    (0, "VIPTELA-DOT1X", "dot1xRadiusIfName"),
    (0, "VIPTELA-DOT1X", "dot1xRadiusIpAddress"),
)
if mibBuilder.loadTexts:
    dot1xRadiusEntry.setStatus("current")


class _Dot1xRadiusIfName_Type(String):
    """Custom type dot1xRadiusIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot1xRadiusIfName_Type.__name__ = "String"
_Dot1xRadiusIfName_Object = MibTableColumn
dot1xRadiusIfName = _Dot1xRadiusIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 1),
    _Dot1xRadiusIfName_Type()
)
dot1xRadiusIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xRadiusIfName.setStatus("current")
_Dot1xRadiusIpAddress_Type = InetAddressIP
_Dot1xRadiusIpAddress_Object = MibTableColumn
dot1xRadiusIpAddress = _Dot1xRadiusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 2),
    _Dot1xRadiusIpAddress_Type()
)
dot1xRadiusIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xRadiusIpAddress.setStatus("current")
_Dot1xRadiusVpn_Type = Unsigned32
_Dot1xRadiusVpn_Object = MibTableColumn
dot1xRadiusVpn = _Dot1xRadiusVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 3),
    _Dot1xRadiusVpn_Type()
)
dot1xRadiusVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusVpn.setStatus("current")
_Dot1xRadiusIsPrimary_Type = TruthValue
_Dot1xRadiusIsPrimary_Object = MibTableColumn
dot1xRadiusIsPrimary = _Dot1xRadiusIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 4),
    _Dot1xRadiusIsPrimary_Type()
)
dot1xRadiusIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusIsPrimary.setStatus("current")
_Dot1xRadiusAuthPort_Type = Unsigned32
_Dot1xRadiusAuthPort_Object = MibTableColumn
dot1xRadiusAuthPort = _Dot1xRadiusAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 5),
    _Dot1xRadiusAuthPort_Type()
)
dot1xRadiusAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthPort.setStatus("current")
_Dot1xRadiusAuthIsCurrent_Type = TruthValue
_Dot1xRadiusAuthIsCurrent_Object = MibTableColumn
dot1xRadiusAuthIsCurrent = _Dot1xRadiusAuthIsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 6),
    _Dot1xRadiusAuthIsCurrent_Type()
)
dot1xRadiusAuthIsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthIsCurrent.setStatus("current")
_Dot1xRadiusAuthRoundTripTime_Type = Unsigned32
_Dot1xRadiusAuthRoundTripTime_Object = MibTableColumn
dot1xRadiusAuthRoundTripTime = _Dot1xRadiusAuthRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 7),
    _Dot1xRadiusAuthRoundTripTime_Type()
)
dot1xRadiusAuthRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthRoundTripTime.setStatus("current")
_Dot1xRadiusAuthAccessRequests_Type = Unsigned32
_Dot1xRadiusAuthAccessRequests_Object = MibTableColumn
dot1xRadiusAuthAccessRequests = _Dot1xRadiusAuthAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 8),
    _Dot1xRadiusAuthAccessRequests_Type()
)
dot1xRadiusAuthAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthAccessRequests.setStatus("current")
_Dot1xRadiusAuthAccessRetransmissions_Type = Unsigned32
_Dot1xRadiusAuthAccessRetransmissions_Object = MibTableColumn
dot1xRadiusAuthAccessRetransmissions = _Dot1xRadiusAuthAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 9),
    _Dot1xRadiusAuthAccessRetransmissions_Type()
)
dot1xRadiusAuthAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthAccessRetransmissions.setStatus("current")
_Dot1xRadiusAuthAccessAccepts_Type = Unsigned32
_Dot1xRadiusAuthAccessAccepts_Object = MibTableColumn
dot1xRadiusAuthAccessAccepts = _Dot1xRadiusAuthAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 10),
    _Dot1xRadiusAuthAccessAccepts_Type()
)
dot1xRadiusAuthAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthAccessAccepts.setStatus("current")
_Dot1xRadiusAuthAccessRejects_Type = Unsigned32
_Dot1xRadiusAuthAccessRejects_Object = MibTableColumn
dot1xRadiusAuthAccessRejects = _Dot1xRadiusAuthAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 11),
    _Dot1xRadiusAuthAccessRejects_Type()
)
dot1xRadiusAuthAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthAccessRejects.setStatus("current")
_Dot1xRadiusAuthAccessChallenges_Type = Unsigned32
_Dot1xRadiusAuthAccessChallenges_Object = MibTableColumn
dot1xRadiusAuthAccessChallenges = _Dot1xRadiusAuthAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 12),
    _Dot1xRadiusAuthAccessChallenges_Type()
)
dot1xRadiusAuthAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthAccessChallenges.setStatus("current")
_Dot1xRadiusAuthMalformedAccessResponses_Type = Unsigned32
_Dot1xRadiusAuthMalformedAccessResponses_Object = MibTableColumn
dot1xRadiusAuthMalformedAccessResponses = _Dot1xRadiusAuthMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 13),
    _Dot1xRadiusAuthMalformedAccessResponses_Type()
)
dot1xRadiusAuthMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthMalformedAccessResponses.setStatus("current")
_Dot1xRadiusAuthBadAuthenticators_Type = Unsigned32
_Dot1xRadiusAuthBadAuthenticators_Object = MibTableColumn
dot1xRadiusAuthBadAuthenticators = _Dot1xRadiusAuthBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 14),
    _Dot1xRadiusAuthBadAuthenticators_Type()
)
dot1xRadiusAuthBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthBadAuthenticators.setStatus("current")
_Dot1xRadiusAuthPendingRequests_Type = Unsigned32
_Dot1xRadiusAuthPendingRequests_Object = MibTableColumn
dot1xRadiusAuthPendingRequests = _Dot1xRadiusAuthPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 15),
    _Dot1xRadiusAuthPendingRequests_Type()
)
dot1xRadiusAuthPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthPendingRequests.setStatus("current")
_Dot1xRadiusAuthTimeouts_Type = Unsigned32
_Dot1xRadiusAuthTimeouts_Object = MibTableColumn
dot1xRadiusAuthTimeouts = _Dot1xRadiusAuthTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 16),
    _Dot1xRadiusAuthTimeouts_Type()
)
dot1xRadiusAuthTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthTimeouts.setStatus("current")
_Dot1xRadiusAuthUnknownTypes_Type = Unsigned32
_Dot1xRadiusAuthUnknownTypes_Object = MibTableColumn
dot1xRadiusAuthUnknownTypes = _Dot1xRadiusAuthUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 17),
    _Dot1xRadiusAuthUnknownTypes_Type()
)
dot1xRadiusAuthUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthUnknownTypes.setStatus("current")
_Dot1xRadiusAuthPacketsDropped_Type = Unsigned32
_Dot1xRadiusAuthPacketsDropped_Object = MibTableColumn
dot1xRadiusAuthPacketsDropped = _Dot1xRadiusAuthPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 18),
    _Dot1xRadiusAuthPacketsDropped_Type()
)
dot1xRadiusAuthPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAuthPacketsDropped.setStatus("current")
_Dot1xRadiusAcctPort_Type = Unsigned32
_Dot1xRadiusAcctPort_Object = MibTableColumn
dot1xRadiusAcctPort = _Dot1xRadiusAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 19),
    _Dot1xRadiusAcctPort_Type()
)
dot1xRadiusAcctPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctPort.setStatus("current")
_Dot1xRadiusAcctIsCurrent_Type = TruthValue
_Dot1xRadiusAcctIsCurrent_Object = MibTableColumn
dot1xRadiusAcctIsCurrent = _Dot1xRadiusAcctIsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 20),
    _Dot1xRadiusAcctIsCurrent_Type()
)
dot1xRadiusAcctIsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctIsCurrent.setStatus("current")
_Dot1xRadiusAcctRoundTripTime_Type = Unsigned32
_Dot1xRadiusAcctRoundTripTime_Object = MibTableColumn
dot1xRadiusAcctRoundTripTime = _Dot1xRadiusAcctRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 21),
    _Dot1xRadiusAcctRoundTripTime_Type()
)
dot1xRadiusAcctRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctRoundTripTime.setStatus("current")
_Dot1xRadiusAcctRequests_Type = Unsigned32
_Dot1xRadiusAcctRequests_Object = MibTableColumn
dot1xRadiusAcctRequests = _Dot1xRadiusAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 22),
    _Dot1xRadiusAcctRequests_Type()
)
dot1xRadiusAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctRequests.setStatus("current")
_Dot1xRadiusAcctRetransmissions_Type = Unsigned32
_Dot1xRadiusAcctRetransmissions_Object = MibTableColumn
dot1xRadiusAcctRetransmissions = _Dot1xRadiusAcctRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 23),
    _Dot1xRadiusAcctRetransmissions_Type()
)
dot1xRadiusAcctRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctRetransmissions.setStatus("current")
_Dot1xRadiusAcctResponses_Type = Unsigned32
_Dot1xRadiusAcctResponses_Object = MibTableColumn
dot1xRadiusAcctResponses = _Dot1xRadiusAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 24),
    _Dot1xRadiusAcctResponses_Type()
)
dot1xRadiusAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctResponses.setStatus("current")
_Dot1xRadiusAcctMalformedResponses_Type = Unsigned32
_Dot1xRadiusAcctMalformedResponses_Object = MibTableColumn
dot1xRadiusAcctMalformedResponses = _Dot1xRadiusAcctMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 25),
    _Dot1xRadiusAcctMalformedResponses_Type()
)
dot1xRadiusAcctMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctMalformedResponses.setStatus("current")
_Dot1xRadiusAcctBadAuthenticators_Type = Unsigned32
_Dot1xRadiusAcctBadAuthenticators_Object = MibTableColumn
dot1xRadiusAcctBadAuthenticators = _Dot1xRadiusAcctBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 26),
    _Dot1xRadiusAcctBadAuthenticators_Type()
)
dot1xRadiusAcctBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctBadAuthenticators.setStatus("current")
_Dot1xRadiusAcctPendingRequests_Type = Unsigned32
_Dot1xRadiusAcctPendingRequests_Object = MibTableColumn
dot1xRadiusAcctPendingRequests = _Dot1xRadiusAcctPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 27),
    _Dot1xRadiusAcctPendingRequests_Type()
)
dot1xRadiusAcctPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctPendingRequests.setStatus("current")
_Dot1xRadiusAcctTimeouts_Type = Unsigned32
_Dot1xRadiusAcctTimeouts_Object = MibTableColumn
dot1xRadiusAcctTimeouts = _Dot1xRadiusAcctTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 28),
    _Dot1xRadiusAcctTimeouts_Type()
)
dot1xRadiusAcctTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctTimeouts.setStatus("current")
_Dot1xRadiusAcctUnknownTypes_Type = Unsigned32
_Dot1xRadiusAcctUnknownTypes_Object = MibTableColumn
dot1xRadiusAcctUnknownTypes = _Dot1xRadiusAcctUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 29),
    _Dot1xRadiusAcctUnknownTypes_Type()
)
dot1xRadiusAcctUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctUnknownTypes.setStatus("current")
_Dot1xRadiusAcctPacketsDropped_Type = Unsigned32
_Dot1xRadiusAcctPacketsDropped_Object = MibTableColumn
dot1xRadiusAcctPacketsDropped = _Dot1xRadiusAcctPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 19, 1, 3, 1, 30),
    _Dot1xRadiusAcctPacketsDropped_Type()
)
dot1xRadiusAcctPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xRadiusAcctPacketsDropped.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-DOT1X",
    **{"UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "Dot1xAuthMethod": Dot1xAuthMethod,
       "EapMethod": EapMethod,
       "Dot1xAuthState": Dot1xAuthState,
       "viptela-dot1x": viptela_dot1x,
       "dot1x": dot1x,
       "dot1xInterfacesTable": dot1xInterfacesTable,
       "dot1xInterfacesEntry": dot1xInterfacesEntry,
       "dot1xInterfacesIfName": dot1xInterfacesIfName,
       "dot1xInterfacesOperState": dot1xInterfacesOperState,
       "dot1xInterfacesHostMode": dot1xInterfacesHostMode,
       "dot1xInterfacesCtrlDir": dot1xInterfacesCtrlDir,
       "dot1xInterfacesMabServer": dot1xInterfacesMabServer,
       "dot1xInterfacesMabLocal": dot1xInterfacesMabLocal,
       "dot1xInterfacesWakeOnLan": dot1xInterfacesWakeOnLan,
       "dot1xInterfacesReauthTimeout": dot1xInterfacesReauthTimeout,
       "dot1xInterfacesInactivityTimeout": dot1xInterfacesInactivityTimeout,
       "dot1xInterfacesGuestVlan": dot1xInterfacesGuestVlan,
       "dot1xInterfacesAuthFailVlan": dot1xInterfacesAuthFailVlan,
       "dot1xInterfacesAuthRejectVlan": dot1xInterfacesAuthRejectVlan,
       "dot1xInterfacesDefaultVlan": dot1xInterfacesDefaultVlan,
       "dot1xInterfacesPrimaryRadiusServer": dot1xInterfacesPrimaryRadiusServer,
       "dot1xInterfacesSecondaryRadiusServer": dot1xInterfacesSecondaryRadiusServer,
       "dot1xInterfacesAccountingInterval": dot1xInterfacesAccountingInterval,
       "dot1xInterfacesNasIdentifier": dot1xInterfacesNasIdentifier,
       "dot1xInterfacesNasIPAddr": dot1xInterfacesNasIPAddr,
       "dot1xInterfacesNumClients": dot1xInterfacesNumClients,
       "dot1xClientsTable": dot1xClientsTable,
       "dot1xClientsEntry": dot1xClientsEntry,
       "dot1xClientsIfName": dot1xClientsIfName,
       "dot1xClientsMacAddress": dot1xClientsMacAddress,
       "dot1xClientsAuthState": dot1xClientsAuthState,
       "dot1xClientsAuthMethod": dot1xClientsAuthMethod,
       "dot1xClientsVlan": dot1xClientsVlan,
       "dot1xClientsVpn": dot1xClientsVpn,
       "dot1xClientsEapMethod": dot1xClientsEapMethod,
       "dot1xClientsUsername": dot1xClientsUsername,
       "dot1xClientsSessionTime": dot1xClientsSessionTime,
       "dot1xClientsConnectedTime": dot1xClientsConnectedTime,
       "dot1xClientsInactiveTime": dot1xClientsInactiveTime,
       "dot1xClientsSessionId": dot1xClientsSessionId,
       "dot1xClientsEapolFramesRx": dot1xClientsEapolFramesRx,
       "dot1xClientsEapolFramesTx": dot1xClientsEapolFramesTx,
       "dot1xClientsEapolStartFramesRx": dot1xClientsEapolStartFramesRx,
       "dot1xClientsEapolLogoffFramesRx": dot1xClientsEapolLogoffFramesRx,
       "dot1xClientsEapolRequestIdFramesTx": dot1xClientsEapolRequestIdFramesTx,
       "dot1xClientsEapolResponseIdFramesRx": dot1xClientsEapolResponseIdFramesRx,
       "dot1xClientsEapolRequestFramesTx": dot1xClientsEapolRequestFramesTx,
       "dot1xClientsEapolResponseFramesRx": dot1xClientsEapolResponseFramesRx,
       "dot1xRadiusTable": dot1xRadiusTable,
       "dot1xRadiusEntry": dot1xRadiusEntry,
       "dot1xRadiusIfName": dot1xRadiusIfName,
       "dot1xRadiusIpAddress": dot1xRadiusIpAddress,
       "dot1xRadiusVpn": dot1xRadiusVpn,
       "dot1xRadiusIsPrimary": dot1xRadiusIsPrimary,
       "dot1xRadiusAuthPort": dot1xRadiusAuthPort,
       "dot1xRadiusAuthIsCurrent": dot1xRadiusAuthIsCurrent,
       "dot1xRadiusAuthRoundTripTime": dot1xRadiusAuthRoundTripTime,
       "dot1xRadiusAuthAccessRequests": dot1xRadiusAuthAccessRequests,
       "dot1xRadiusAuthAccessRetransmissions": dot1xRadiusAuthAccessRetransmissions,
       "dot1xRadiusAuthAccessAccepts": dot1xRadiusAuthAccessAccepts,
       "dot1xRadiusAuthAccessRejects": dot1xRadiusAuthAccessRejects,
       "dot1xRadiusAuthAccessChallenges": dot1xRadiusAuthAccessChallenges,
       "dot1xRadiusAuthMalformedAccessResponses": dot1xRadiusAuthMalformedAccessResponses,
       "dot1xRadiusAuthBadAuthenticators": dot1xRadiusAuthBadAuthenticators,
       "dot1xRadiusAuthPendingRequests": dot1xRadiusAuthPendingRequests,
       "dot1xRadiusAuthTimeouts": dot1xRadiusAuthTimeouts,
       "dot1xRadiusAuthUnknownTypes": dot1xRadiusAuthUnknownTypes,
       "dot1xRadiusAuthPacketsDropped": dot1xRadiusAuthPacketsDropped,
       "dot1xRadiusAcctPort": dot1xRadiusAcctPort,
       "dot1xRadiusAcctIsCurrent": dot1xRadiusAcctIsCurrent,
       "dot1xRadiusAcctRoundTripTime": dot1xRadiusAcctRoundTripTime,
       "dot1xRadiusAcctRequests": dot1xRadiusAcctRequests,
       "dot1xRadiusAcctRetransmissions": dot1xRadiusAcctRetransmissions,
       "dot1xRadiusAcctResponses": dot1xRadiusAcctResponses,
       "dot1xRadiusAcctMalformedResponses": dot1xRadiusAcctMalformedResponses,
       "dot1xRadiusAcctBadAuthenticators": dot1xRadiusAcctBadAuthenticators,
       "dot1xRadiusAcctPendingRequests": dot1xRadiusAcctPendingRequests,
       "dot1xRadiusAcctTimeouts": dot1xRadiusAcctTimeouts,
       "dot1xRadiusAcctUnknownTypes": dot1xRadiusAcctUnknownTypes,
       "dot1xRadiusAcctPacketsDropped": dot1xRadiusAcctPacketsDropped}
)
