# SNMP MIB module (CIENA-CES-SW-XGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-SW-XGRADE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:54 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesSwXgradeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13)
)
if mibBuilder.loadTexts:
    cienaCesSwXgradeMIB.setRevisions(
        ("2017-06-07 00:00",
         "2012-07-24 00:00",
         "2010-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesSwXgradeMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesSwXgradeMIBObjects = _CienaCesSwXgradeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 1)
)
_CienaCesSwXgrade_ObjectIdentity = ObjectIdentity
cienaCesSwXgrade = _CienaCesSwXgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 1, 1)
)
_CienaCesSwXgradeGracefulUpgrade_Type = TruthValue
_CienaCesSwXgradeGracefulUpgrade_Object = MibScalar
cienaCesSwXgradeGracefulUpgrade = _CienaCesSwXgradeGracefulUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 1, 1, 1),
    _CienaCesSwXgradeGracefulUpgrade_Type()
)
cienaCesSwXgradeGracefulUpgrade.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSwXgradeGracefulUpgrade.setStatus("current")


class _CienaCesSwXgradeOp_Type(Integer32):
    """Custom type cienaCesSwXgradeOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("none", 0),
          ("download", 1),
          ("install", 2),
          ("activate", 3),
          ("protect", 4),
          ("validate", 5),
          ("revert", 6),
          ("configure", 7),
          ("run", 8),
          ("remove", 9))
    )


_CienaCesSwXgradeOp_Type.__name__ = "Integer32"
_CienaCesSwXgradeOp_Object = MibScalar
cienaCesSwXgradeOp = _CienaCesSwXgradeOp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 1, 1, 2),
    _CienaCesSwXgradeOp_Type()
)
cienaCesSwXgradeOp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSwXgradeOp.setStatus("current")


class _CienaCesSwXgradeStatus_Type(Integer32):
    """Custom type cienaCesSwXgradeStatus based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("unknown", 3),
          ("processing", 4),
          ("invalidCfgRule", 5),
          ("invalidFileName", 6),
          ("fileSystemError", 7),
          ("cannotResolveHostName", 8),
          ("tftpClientTimeout", 9),
          ("tftpServerError", 10),
          ("tftpBadTag", 11),
          ("tftpBadValue", 12),
          ("networkError", 13),
          ("platformTypeNotSupported", 14),
          ("swMgrBusy", 15),
          ("needBackupSw", 16),
          ("internalError", 17),
          ("fileNotExist", 18),
          ("missingAttribute", 19),
          ("invalidXgradeOp", 20),
          ("noDefaultTftpConfigured", 21),
          ("completedWithFailures", 22))
    )


_CienaCesSwXgradeStatus_Type.__name__ = "Integer32"
_CienaCesSwXgradeStatus_Object = MibScalar
cienaCesSwXgradeStatus = _CienaCesSwXgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 1, 1, 3),
    _CienaCesSwXgradeStatus_Type()
)
cienaCesSwXgradeStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSwXgradeStatus.setStatus("current")
_CienaCesSwXgradeMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesSwXgradeMIBConformance = _CienaCesSwXgradeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 3)
)
_CienaCesSwXgradeMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesSwXgradeMIBCompliances = _CienaCesSwXgradeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 3, 1)
)
_CienaCesSwXgradeMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesSwXgradeMIBGroups = _CienaCesSwXgradeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 13, 3, 2)
)
_CienaCesSwXgradeMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesSwXgradeMIBNotificationPrefix = _CienaCesSwXgradeMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 13)
)
_CienaCesSwXgradeMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesSwXgradeMIBNotifications = _CienaCesSwXgradeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 13, 0)
)

# Managed Objects groups


# Notification objects

cienaCesSwXgradeCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 13, 0, 1)
)
cienaCesSwXgradeCompletion.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SW-XGRADE-MIB", "cienaCesSwXgradeOp"),
        ("CIENA-CES-SW-XGRADE-MIB", "cienaCesSwXgradeStatus"),
        ("CIENA-CES-SW-XGRADE-MIB", "cienaCesSwXgradeGracefulUpgrade"))
)
if mibBuilder.loadTexts:
    cienaCesSwXgradeCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-SW-XGRADE-MIB",
    **{"cienaCesSwXgradeMIB": cienaCesSwXgradeMIB,
       "cienaCesSwXgradeMIBObjects": cienaCesSwXgradeMIBObjects,
       "cienaCesSwXgrade": cienaCesSwXgrade,
       "cienaCesSwXgradeGracefulUpgrade": cienaCesSwXgradeGracefulUpgrade,
       "cienaCesSwXgradeOp": cienaCesSwXgradeOp,
       "cienaCesSwXgradeStatus": cienaCesSwXgradeStatus,
       "cienaCesSwXgradeMIBConformance": cienaCesSwXgradeMIBConformance,
       "cienaCesSwXgradeMIBCompliances": cienaCesSwXgradeMIBCompliances,
       "cienaCesSwXgradeMIBGroups": cienaCesSwXgradeMIBGroups,
       "cienaCesSwXgradeMIBNotificationPrefix": cienaCesSwXgradeMIBNotificationPrefix,
       "cienaCesSwXgradeMIBNotifications": cienaCesSwXgradeMIBNotifications,
       "cienaCesSwXgradeCompletion": cienaCesSwXgradeCompletion}
)
