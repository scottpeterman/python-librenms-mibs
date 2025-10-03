# SNMP MIB module (CIENA-CES-CONFIG-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-CONFIG-MGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:31 2025
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

(cienaGlobalSeverity,) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesConfigMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36)
)
if mibBuilder.loadTexts:
    cienaCesConfigMgmtMIB.setRevisions(
        ("2015-02-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CienaCesConfigMgmtContext(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("cli", 2),
          ("snmp", 3),
          ("netconf", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesConfigMgmtMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesConfigMgmtMIBObjects = _CienaCesConfigMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1)
)
_CienaCesConfigMgmt_ObjectIdentity = ObjectIdentity
cienaCesConfigMgmt = _CienaCesConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1)
)
_CienaCesConfigMgmtConfigLastSaved_Type = DateAndTime
_CienaCesConfigMgmtConfigLastSaved_Object = MibScalar
cienaCesConfigMgmtConfigLastSaved = _CienaCesConfigMgmtConfigLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 1),
    _CienaCesConfigMgmtConfigLastSaved_Type()
)
cienaCesConfigMgmtConfigLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesConfigMgmtConfigLastSaved.setStatus("current")
_CienaCesConfigMgmtConfigLastChanged_Type = DateAndTime
_CienaCesConfigMgmtConfigLastChanged_Object = MibScalar
cienaCesConfigMgmtConfigLastChanged = _CienaCesConfigMgmtConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 2),
    _CienaCesConfigMgmtConfigLastChanged_Type()
)
cienaCesConfigMgmtConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesConfigMgmtConfigLastChanged.setStatus("current")
_CienaCesConfigMgmtConfigLastContext_Type = CienaCesConfigMgmtContext
_CienaCesConfigMgmtConfigLastContext_Object = MibScalar
cienaCesConfigMgmtConfigLastContext = _CienaCesConfigMgmtConfigLastContext_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 3),
    _CienaCesConfigMgmtConfigLastContext_Type()
)
cienaCesConfigMgmtConfigLastContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesConfigMgmtConfigLastContext.setStatus("current")
_CienaCesConfigMgmtConfigLastUser_Type = DisplayString
_CienaCesConfigMgmtConfigLastUser_Object = MibScalar
cienaCesConfigMgmtConfigLastUser = _CienaCesConfigMgmtConfigLastUser_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 4),
    _CienaCesConfigMgmtConfigLastUser_Type()
)
cienaCesConfigMgmtConfigLastUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesConfigMgmtConfigLastUser.setStatus("current")
_CienaCesConfigMgmtConfigLastOrigin_Type = DisplayString
_CienaCesConfigMgmtConfigLastOrigin_Object = MibScalar
cienaCesConfigMgmtConfigLastOrigin = _CienaCesConfigMgmtConfigLastOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 5),
    _CienaCesConfigMgmtConfigLastOrigin_Type()
)
cienaCesConfigMgmtConfigLastOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesConfigMgmtConfigLastOrigin.setStatus("current")
_CienaCesConfigMgmtMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesConfigMgmtMIBConformance = _CienaCesConfigMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2)
)
_CienaCesConfigMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesConfigMgmtMIBCompliances = _CienaCesConfigMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 1)
)
_CienaCesConfigMgmtMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesConfigMgmtMIBGroups = _CienaCesConfigMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 2)
)
_CienaCesConfigMgmtMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
cienaCesConfigMgmtMIBNotificationsPrefix = _CienaCesConfigMgmtMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 36)
)
_CienaCesConfigMgmtMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesConfigMgmtMIBNotifications = _CienaCesConfigMgmtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0)
)

# Managed Objects groups


# Notification objects

cienaCesConfigMgmtConfigSavedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 1)
)
cienaCesConfigMgmtConfigSavedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastSaved"),
        ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
)
if mibBuilder.loadTexts:
    cienaCesConfigMgmtConfigSavedNotification.setStatus(
        "current"
    )

cienaCesConfigMgmtConfigChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 2)
)
cienaCesConfigMgmtConfigChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastContext"),
        ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastUser"),
        ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastOrigin"),
        ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
)
if mibBuilder.loadTexts:
    cienaCesConfigMgmtConfigChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-CONFIG-MGMT-MIB",
    **{"CienaCesConfigMgmtContext": CienaCesConfigMgmtContext,
       "cienaCesConfigMgmtMIB": cienaCesConfigMgmtMIB,
       "cienaCesConfigMgmtMIBObjects": cienaCesConfigMgmtMIBObjects,
       "cienaCesConfigMgmt": cienaCesConfigMgmt,
       "cienaCesConfigMgmtConfigLastSaved": cienaCesConfigMgmtConfigLastSaved,
       "cienaCesConfigMgmtConfigLastChanged": cienaCesConfigMgmtConfigLastChanged,
       "cienaCesConfigMgmtConfigLastContext": cienaCesConfigMgmtConfigLastContext,
       "cienaCesConfigMgmtConfigLastUser": cienaCesConfigMgmtConfigLastUser,
       "cienaCesConfigMgmtConfigLastOrigin": cienaCesConfigMgmtConfigLastOrigin,
       "cienaCesConfigMgmtMIBConformance": cienaCesConfigMgmtMIBConformance,
       "cienaCesConfigMgmtMIBCompliances": cienaCesConfigMgmtMIBCompliances,
       "cienaCesConfigMgmtMIBGroups": cienaCesConfigMgmtMIBGroups,
       "cienaCesConfigMgmtMIBNotificationsPrefix": cienaCesConfigMgmtMIBNotificationsPrefix,
       "cienaCesConfigMgmtMIBNotifications": cienaCesConfigMgmtMIBNotifications,
       "cienaCesConfigMgmtConfigSavedNotification": cienaCesConfigMgmtConfigSavedNotification,
       "cienaCesConfigMgmtConfigChangeNotification": cienaCesConfigMgmtConfigChangeNotification}
)
