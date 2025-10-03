# SNMP MIB module (CIENA-CES-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-AAA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:22 2025
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

(cienaGlobalMacAddress,) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress")

(cienaCesConfig,
 cienaCesNotifications,
 cienaCommon) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications",
    "cienaCommon")

(CienaGlobalSeverity,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalSeverity")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60)
)
if mibBuilder.loadTexts:
    cienaCesAAAMIB.setRevisions(
        ("2022-12-06 00:00",
         "2021-08-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesAAAMibObjects_ObjectIdentity = ObjectIdentity
cienaCesAAAMibObjects = _CienaCesAAAMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1)
)


class _CienaCesAAAUserName_Type(DisplayString):
    """Custom type cienaCesAAAUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesAAAUserName_Type.__name__ = "DisplayString"
_CienaCesAAAUserName_Object = MibScalar
cienaCesAAAUserName = _CienaCesAAAUserName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 1),
    _CienaCesAAAUserName_Type()
)
cienaCesAAAUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAUserName.setStatus("current")
_CienaCesAAAHostIp_Type = IpAddress
_CienaCesAAAHostIp_Object = MibScalar
cienaCesAAAHostIp = _CienaCesAAAHostIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 2),
    _CienaCesAAAHostIp_Type()
)
cienaCesAAAHostIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAHostIp.setStatus("current")
_CienaCesAAAUserPort_Type = Unsigned32
_CienaCesAAAUserPort_Object = MibScalar
cienaCesAAAUserPort = _CienaCesAAAUserPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 3),
    _CienaCesAAAUserPort_Type()
)
cienaCesAAAUserPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAUserPort.setStatus("current")


class _CienaCesAAAUserAuthenticationServiceType_Type(Integer32):
    """Custom type cienaCesAAAUserAuthenticationServiceType based on Integer32"""
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
        *(("local", 1),
          ("tacacs", 2),
          ("radius", 3),
          ("radsec", 4))
    )


_CienaCesAAAUserAuthenticationServiceType_Type.__name__ = "Integer32"
_CienaCesAAAUserAuthenticationServiceType_Object = MibScalar
cienaCesAAAUserAuthenticationServiceType = _CienaCesAAAUserAuthenticationServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 4),
    _CienaCesAAAUserAuthenticationServiceType_Type()
)
cienaCesAAAUserAuthenticationServiceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAUserAuthenticationServiceType.setStatus("current")


class _CienaCesAAAUserAuthenticationStatus_Type(Integer32):
    """Custom type cienaCesAAAUserAuthenticationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_CienaCesAAAUserAuthenticationStatus_Type.__name__ = "Integer32"
_CienaCesAAAUserAuthenticationStatus_Object = MibScalar
cienaCesAAAUserAuthenticationStatus = _CienaCesAAAUserAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 5),
    _CienaCesAAAUserAuthenticationStatus_Type()
)
cienaCesAAAUserAuthenticationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAUserAuthenticationStatus.setStatus("current")
_CienaCesAAAUserAuthenticationDescription_Type = DisplayString
_CienaCesAAAUserAuthenticationDescription_Object = MibScalar
cienaCesAAAUserAuthenticationDescription = _CienaCesAAAUserAuthenticationDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 6),
    _CienaCesAAAUserAuthenticationDescription_Type()
)
cienaCesAAAUserAuthenticationDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAUserAuthenticationDescription.setStatus("current")
_CienaCesAAAServerGroup_Type = DisplayString
_CienaCesAAAServerGroup_Object = MibScalar
cienaCesAAAServerGroup = _CienaCesAAAServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 7),
    _CienaCesAAAServerGroup_Type()
)
cienaCesAAAServerGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAServerGroup.setStatus("current")
_CienaCesAAATacacsServer_Type = DisplayString
_CienaCesAAATacacsServer_Object = MibScalar
cienaCesAAATacacsServer = _CienaCesAAATacacsServer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 8),
    _CienaCesAAATacacsServer_Type()
)
cienaCesAAATacacsServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAATacacsServer.setStatus("current")


class _CienaCesAAAServerStatus_Type(Integer32):
    """Custom type cienaCesAAAServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unreachable", 2))
    )


_CienaCesAAAServerStatus_Type.__name__ = "Integer32"
_CienaCesAAAServerStatus_Object = MibScalar
cienaCesAAAServerStatus = _CienaCesAAAServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 9),
    _CienaCesAAAServerStatus_Type()
)
cienaCesAAAServerStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAServerStatus.setStatus("current")
_CienaCesAAAAllServerDownStatus_Type = TruthValue
_CienaCesAAAAllServerDownStatus_Object = MibScalar
cienaCesAAAAllServerDownStatus = _CienaCesAAAAllServerDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 10),
    _CienaCesAAAAllServerDownStatus_Type()
)
cienaCesAAAAllServerDownStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAAllServerDownStatus.setStatus("current")
_CienaCesAAALdapServer_Type = DisplayString
_CienaCesAAALdapServer_Object = MibScalar
cienaCesAAALdapServer = _CienaCesAAALdapServer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 11),
    _CienaCesAAALdapServer_Type()
)
cienaCesAAALdapServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAALdapServer.setStatus("current")
_CienaCesAAAUser_Type = DisplayString
_CienaCesAAAUser_Object = MibScalar
cienaCesAAAUser = _CienaCesAAAUser_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 12),
    _CienaCesAAAUser_Type()
)
cienaCesAAAUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAAUser.setStatus("current")
_CienaCesAAANacmGroup_Type = DisplayString
_CienaCesAAANacmGroup_Object = MibScalar
cienaCesAAANacmGroup = _CienaCesAAANacmGroup_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 13),
    _CienaCesAAANacmGroup_Type()
)
cienaCesAAANacmGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAANacmGroup.setStatus("current")


class _CienaCesAAALdapServerStatus_Type(Integer32):
    """Custom type cienaCesAAALdapServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2),
          ("ruleparseerror", 3))
    )


_CienaCesAAALdapServerStatus_Type.__name__ = "Integer32"
_CienaCesAAALdapServerStatus_Object = MibScalar
cienaCesAAALdapServerStatus = _CienaCesAAALdapServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 60, 1, 14),
    _CienaCesAAALdapServerStatus_Type()
)
cienaCesAAALdapServerStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesAAALdapServerStatus.setStatus("current")
_CienaCesAAAMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesAAAMIBNotificationPrefix = _CienaCesAAAMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 111)
)
_CienaCesAAAMIBNotification_ObjectIdentity = ObjectIdentity
cienaCesAAAMIBNotification = _CienaCesAAAMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 111, 0)
)

# Managed Objects groups


# Notification objects

cienaCesAAAUserAuthenticationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 111, 0, 1)
)
cienaCesAAAUserAuthenticationEvent.setObjects(
      *(("CIENA-CES-AAA-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAUserName"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAHostIp"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAUserPort"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAUserAuthenticationServiceType"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAUserAuthenticationStatus"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAUserAuthenticationDescription"))
)
if mibBuilder.loadTexts:
    cienaCesAAAUserAuthenticationEvent.setStatus(
        "current"
    )

cienaCesAAATacacsServerStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 111, 0, 2)
)
cienaCesAAATacacsServerStatusEvent.setObjects(
      *(("CIENA-CES-AAA-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAServerGroup"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAATacacsServer"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAServerStatus"))
)
if mibBuilder.loadTexts:
    cienaCesAAATacacsServerStatusEvent.setStatus(
        "current"
    )

cienaCesAAAAllTacacsServersDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 111, 0, 3)
)
cienaCesAAAAllTacacsServersDownEvent.setObjects(
      *(("CIENA-CES-AAA-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAServerGroup"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAAllServerDownStatus"))
)
if mibBuilder.loadTexts:
    cienaCesAAAAllTacacsServersDownEvent.setStatus(
        "current"
    )

cienaCesAAALdapServerStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 111, 0, 4)
)
cienaCesAAALdapServerStatusEvent.setObjects(
      *(("CIENA-CES-AAA-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAALdapServer"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAUser"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAANacmGroup"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAALdapServerStatus"))
)
if mibBuilder.loadTexts:
    cienaCesAAALdapServerStatusEvent.setStatus(
        "current"
    )

cienaCesAAAAllLdapServersDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 111, 0, 5)
)
cienaCesAAAAllLdapServersDownEvent.setObjects(
      *(("CIENA-CES-AAA-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-AAA-MIB", "cienaCesAAAAllServerDownStatus"))
)
if mibBuilder.loadTexts:
    cienaCesAAAAllLdapServersDownEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-AAA-MIB",
    **{"cienaCesAAAMIB": cienaCesAAAMIB,
       "cienaCesAAAMibObjects": cienaCesAAAMibObjects,
       "cienaCesAAAUserName": cienaCesAAAUserName,
       "cienaCesAAAHostIp": cienaCesAAAHostIp,
       "cienaCesAAAUserPort": cienaCesAAAUserPort,
       "cienaCesAAAUserAuthenticationServiceType": cienaCesAAAUserAuthenticationServiceType,
       "cienaCesAAAUserAuthenticationStatus": cienaCesAAAUserAuthenticationStatus,
       "cienaCesAAAUserAuthenticationDescription": cienaCesAAAUserAuthenticationDescription,
       "cienaCesAAAServerGroup": cienaCesAAAServerGroup,
       "cienaCesAAATacacsServer": cienaCesAAATacacsServer,
       "cienaCesAAAServerStatus": cienaCesAAAServerStatus,
       "cienaCesAAAAllServerDownStatus": cienaCesAAAAllServerDownStatus,
       "cienaCesAAALdapServer": cienaCesAAALdapServer,
       "cienaCesAAAUser": cienaCesAAAUser,
       "cienaCesAAANacmGroup": cienaCesAAANacmGroup,
       "cienaCesAAALdapServerStatus": cienaCesAAALdapServerStatus,
       "cienaCesAAAMIBNotificationPrefix": cienaCesAAAMIBNotificationPrefix,
       "cienaCesAAAMIBNotification": cienaCesAAAMIBNotification,
       "cienaCesAAAUserAuthenticationEvent": cienaCesAAAUserAuthenticationEvent,
       "cienaCesAAATacacsServerStatusEvent": cienaCesAAATacacsServerStatusEvent,
       "cienaCesAAAAllTacacsServersDownEvent": cienaCesAAAAllTacacsServersDownEvent,
       "cienaCesAAALdapServerStatusEvent": cienaCesAAALdapServerStatusEvent,
       "cienaCesAAAAllLdapServersDownEvent": cienaCesAAAAllLdapServersDownEvent}
)
