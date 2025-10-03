# SNMP MIB module (CIENA-CES-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-SECURITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:53 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44)
)
if mibBuilder.loadTexts:
    cienaCesSecurityMIB.setRevisions(
        ("2017-09-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesSecurityMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesSecurityMIBObjects = _CienaCesSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1)
)
_CienaCesSecurityCertExpiry_ObjectIdentity = ObjectIdentity
cienaCesSecurityCertExpiry = _CienaCesSecurityCertExpiry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 1)
)


class _CienaCesSecurityCertType_Type(Integer32):
    """Custom type cienaCesSecurityCertType based on Integer32"""
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
        *(("ca", 1),
          ("devCert", 2),
          ("sshClient", 3),
          ("sshServer", 4))
    )


_CienaCesSecurityCertType_Type.__name__ = "Integer32"
_CienaCesSecurityCertType_Object = MibScalar
cienaCesSecurityCertType = _CienaCesSecurityCertType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 1, 1),
    _CienaCesSecurityCertType_Type()
)
cienaCesSecurityCertType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSecurityCertType.setStatus("current")
_CienaCesSecurityCertName_Type = DisplayString
_CienaCesSecurityCertName_Object = MibScalar
cienaCesSecurityCertName = _CienaCesSecurityCertName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 1, 2),
    _CienaCesSecurityCertName_Type()
)
cienaCesSecurityCertName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSecurityCertName.setStatus("current")
_CienaCesSecurityCertValidTo_Type = DisplayString
_CienaCesSecurityCertValidTo_Object = MibScalar
cienaCesSecurityCertValidTo = _CienaCesSecurityCertValidTo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 1, 3),
    _CienaCesSecurityCertValidTo_Type()
)
cienaCesSecurityCertValidTo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSecurityCertValidTo.setStatus("current")
_CienaCesSecurityCertCrl_ObjectIdentity = ObjectIdentity
cienaCesSecurityCertCrl = _CienaCesSecurityCertCrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 2)
)
_CienaCesSecurityCaCrlType_Type = DisplayString
_CienaCesSecurityCaCrlType_Object = MibScalar
cienaCesSecurityCaCrlType = _CienaCesSecurityCaCrlType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 2, 1),
    _CienaCesSecurityCaCrlType_Type()
)
cienaCesSecurityCaCrlType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSecurityCaCrlType.setStatus("current")
_CienaCesSecurityCertCrlOperation_Type = DisplayString
_CienaCesSecurityCertCrlOperation_Object = MibScalar
cienaCesSecurityCertCrlOperation = _CienaCesSecurityCertCrlOperation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 2, 2),
    _CienaCesSecurityCertCrlOperation_Type()
)
cienaCesSecurityCertCrlOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSecurityCertCrlOperation.setStatus("current")
_CienaCesSecurityCaCrlInvalidCaReason_Type = DisplayString
_CienaCesSecurityCaCrlInvalidCaReason_Object = MibScalar
cienaCesSecurityCaCrlInvalidCaReason = _CienaCesSecurityCaCrlInvalidCaReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 2, 3),
    _CienaCesSecurityCaCrlInvalidCaReason_Type()
)
cienaCesSecurityCaCrlInvalidCaReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSecurityCaCrlInvalidCaReason.setStatus("current")
_CienaCesSecurityCertKeyOperation_Type = DisplayString
_CienaCesSecurityCertKeyOperation_Object = MibScalar
cienaCesSecurityCertKeyOperation = _CienaCesSecurityCertKeyOperation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 1, 2, 4),
    _CienaCesSecurityCertKeyOperation_Type()
)
cienaCesSecurityCertKeyOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSecurityCertKeyOperation.setStatus("current")
_CienaCesSecurityMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesSecurityMIBConformance = _CienaCesSecurityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 2)
)
_CienaCesSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesSecurityMIBCompliances = _CienaCesSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 2, 1)
)
_CienaCesSecurityMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesSecurityMIBGroups = _CienaCesSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 2, 2)
)
_CienaCesSecurityMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesSecurityMIBNotificationPrefix = _CienaCesSecurityMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43)
)
_CienaCesSecurityMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesSecurityMIBNotifications = _CienaCesSecurityMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43, 0)
)

# Managed Objects groups


# Notification objects

cienaCesSecurityCertExpiryWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43, 0, 1)
)
cienaCesSecurityCertExpiryWarningNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertType"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertName"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertValidTo"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityCertExpiryWarningNotification.setStatus(
        "current"
    )

cienaCesSecurityCertExpiryExpiredNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43, 0, 2)
)
cienaCesSecurityCertExpiryExpiredNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertType"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertName"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertValidTo"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityCertExpiryExpiredNotification.setStatus(
        "current"
    )

cienaCesSecurityCaCrlInstallNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43, 0, 3)
)
cienaCesSecurityCaCrlInstallNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCaCrlType"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertName"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertCrlOperation"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityCaCrlInstallNotification.setStatus(
        "current"
    )

cienaCesSecurityCaCrlInvalidCaNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43, 0, 4)
)
cienaCesSecurityCaCrlInvalidCaNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCaCrlInvalidCaReason"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityCaCrlInvalidCaNotification.setStatus(
        "current"
    )

cienaCesSecurityDevCertInstallNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43, 0, 5)
)
cienaCesSecurityDevCertInstallNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertName"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertCrlOperation"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityDevCertInstallNotification.setStatus(
        "current"
    )

cienaCesSecurityDevCertKeyCreateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 43, 0, 6)
)
cienaCesSecurityDevCertKeyCreateNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertName"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertKeyOperation"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityDevCertKeyCreateNotification.setStatus(
        "current"
    )


# Notifications groups

cienaCesSecurityCertExpiryGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 2, 2, 1)
)
cienaCesSecurityCertExpiryGroup.setObjects(
      *(("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertExpiryWarningNotification"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCertExpiryExpiredNotification"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityCertExpiryGroup.setStatus(
        "current"
    )

cienaCesSecurityCertCrlGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 44, 2, 2, 2)
)
cienaCesSecurityCertCrlGroup.setObjects(
      *(("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCaCrlInstallNotification"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityCaCrlInvalidCaNotification"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityDevCertInstallNotification"),
        ("CIENA-CES-SECURITY-MIB", "cienaCesSecurityDevCertKeyCreateNotification"))
)
if mibBuilder.loadTexts:
    cienaCesSecurityCertCrlGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-SECURITY-MIB",
    **{"cienaCesSecurityMIB": cienaCesSecurityMIB,
       "cienaCesSecurityMIBObjects": cienaCesSecurityMIBObjects,
       "cienaCesSecurityCertExpiry": cienaCesSecurityCertExpiry,
       "cienaCesSecurityCertType": cienaCesSecurityCertType,
       "cienaCesSecurityCertName": cienaCesSecurityCertName,
       "cienaCesSecurityCertValidTo": cienaCesSecurityCertValidTo,
       "cienaCesSecurityCertCrl": cienaCesSecurityCertCrl,
       "cienaCesSecurityCaCrlType": cienaCesSecurityCaCrlType,
       "cienaCesSecurityCertCrlOperation": cienaCesSecurityCertCrlOperation,
       "cienaCesSecurityCaCrlInvalidCaReason": cienaCesSecurityCaCrlInvalidCaReason,
       "cienaCesSecurityCertKeyOperation": cienaCesSecurityCertKeyOperation,
       "cienaCesSecurityMIBConformance": cienaCesSecurityMIBConformance,
       "cienaCesSecurityMIBCompliances": cienaCesSecurityMIBCompliances,
       "cienaCesSecurityMIBGroups": cienaCesSecurityMIBGroups,
       "cienaCesSecurityCertExpiryGroup": cienaCesSecurityCertExpiryGroup,
       "cienaCesSecurityCertCrlGroup": cienaCesSecurityCertCrlGroup,
       "cienaCesSecurityMIBNotificationPrefix": cienaCesSecurityMIBNotificationPrefix,
       "cienaCesSecurityMIBNotifications": cienaCesSecurityMIBNotifications,
       "cienaCesSecurityCertExpiryWarningNotification": cienaCesSecurityCertExpiryWarningNotification,
       "cienaCesSecurityCertExpiryExpiredNotification": cienaCesSecurityCertExpiryExpiredNotification,
       "cienaCesSecurityCaCrlInstallNotification": cienaCesSecurityCaCrlInstallNotification,
       "cienaCesSecurityCaCrlInvalidCaNotification": cienaCesSecurityCaCrlInvalidCaNotification,
       "cienaCesSecurityDevCertInstallNotification": cienaCesSecurityDevCertInstallNotification,
       "cienaCesSecurityDevCertKeyCreateNotification": cienaCesSecurityDevCertKeyCreateNotification}
)
