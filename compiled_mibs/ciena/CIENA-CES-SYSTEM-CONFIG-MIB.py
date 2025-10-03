# SNMP MIB module (CIENA-CES-SYSTEM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:56 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesSystemConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14)
)
if mibBuilder.loadTexts:
    cienaCesSystemConfigMIB.setRevisions(
        ("2017-06-07 00:00",
         "2016-10-28 00:00",
         "2010-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FileName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesSystemConfigMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesSystemConfigMIBObjects = _CienaCesSystemConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1)
)
_CienaCesSystemConfigNotifAttrs_ObjectIdentity = ObjectIdentity
cienaCesSystemConfigNotifAttrs = _CienaCesSystemConfigNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1)
)
_CienaCesSystemConfigFileName_Type = FileName
_CienaCesSystemConfigFileName_Object = MibScalar
cienaCesSystemConfigFileName = _CienaCesSystemConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 1),
    _CienaCesSystemConfigFileName_Type()
)
cienaCesSystemConfigFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSystemConfigFileName.setStatus("current")


class _CienaCesSystemConfigErrLineNum_Type(Integer32):
    """Custom type cienaCesSystemConfigErrLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesSystemConfigErrLineNum_Type.__name__ = "Integer32"
_CienaCesSystemConfigErrLineNum_Object = MibScalar
cienaCesSystemConfigErrLineNum = _CienaCesSystemConfigErrLineNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 2),
    _CienaCesSystemConfigErrLineNum_Type()
)
cienaCesSystemConfigErrLineNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSystemConfigErrLineNum.setStatus("current")
_CienaCesSystemConfigErrStr_Type = DisplayString
_CienaCesSystemConfigErrStr_Object = MibScalar
cienaCesSystemConfigErrStr = _CienaCesSystemConfigErrStr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 3),
    _CienaCesSystemConfigErrStr_Type()
)
cienaCesSystemConfigErrStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSystemConfigErrStr.setStatus("current")


class _CienaCesSystemConfigErrLinesTotal_Type(Integer32):
    """Custom type cienaCesSystemConfigErrLinesTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CienaCesSystemConfigErrLinesTotal_Type.__name__ = "Integer32"
_CienaCesSystemConfigErrLinesTotal_Object = MibScalar
cienaCesSystemConfigErrLinesTotal = _CienaCesSystemConfigErrLinesTotal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 4),
    _CienaCesSystemConfigErrLinesTotal_Type()
)
cienaCesSystemConfigErrLinesTotal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSystemConfigErrLinesTotal.setStatus("current")
_CienaCesCommandFileHost_Type = DisplayString
_CienaCesCommandFileHost_Object = MibScalar
cienaCesCommandFileHost = _CienaCesCommandFileHost_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 5),
    _CienaCesCommandFileHost_Type()
)
cienaCesCommandFileHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCommandFileHost.setStatus("current")
_CienaCesCommandFileName_Type = FileName
_CienaCesCommandFileName_Object = MibScalar
cienaCesCommandFileName = _CienaCesCommandFileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 6),
    _CienaCesCommandFileName_Type()
)
cienaCesCommandFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCommandFileName.setStatus("current")
_CienaCesCommandFileError_Type = DisplayString
_CienaCesCommandFileError_Object = MibScalar
cienaCesCommandFileError = _CienaCesCommandFileError_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 7),
    _CienaCesCommandFileError_Type()
)
cienaCesCommandFileError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCommandFileError.setStatus("current")
_CienaCesSystemConfigMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesSystemConfigMIBConformance = _CienaCesSystemConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 3)
)
_CienaCesSystemConfigCompliances_ObjectIdentity = ObjectIdentity
cienaCesSystemConfigCompliances = _CienaCesSystemConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 3, 1)
)
_CienaCesSystemConfigMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesSystemConfigMIBGroups = _CienaCesSystemConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 3, 2)
)
_CienaCesSystemConfigMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesSystemConfigMIBNotificationPrefix = _CienaCesSystemConfigMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 14)
)
_CienaCesSystemConfigMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesSystemConfigMIBNotifications = _CienaCesSystemConfigMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0)
)

# Managed Objects groups


# Notification objects

cienaCesImproperCmdInConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0, 1)
)
cienaCesImproperCmdInConfigFile.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesSystemConfigFileName"),
        ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesSystemConfigErrLinesTotal"))
)
if mibBuilder.loadTexts:
    cienaCesImproperCmdInConfigFile.setStatus(
        "current"
    )

cienaCesCommandFileCompletedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0, 2)
)
cienaCesCommandFileCompletedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileHost"),
        ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileName"))
)
if mibBuilder.loadTexts:
    cienaCesCommandFileCompletedNotification.setStatus(
        "current"
    )

cienaCesCommandFileFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0, 3)
)
cienaCesCommandFileFailedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileHost"),
        ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileName"),
        ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileError"))
)
if mibBuilder.loadTexts:
    cienaCesCommandFileFailedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-SYSTEM-CONFIG-MIB",
    **{"FileName": FileName,
       "cienaCesSystemConfigMIB": cienaCesSystemConfigMIB,
       "cienaCesSystemConfigMIBObjects": cienaCesSystemConfigMIBObjects,
       "cienaCesSystemConfigNotifAttrs": cienaCesSystemConfigNotifAttrs,
       "cienaCesSystemConfigFileName": cienaCesSystemConfigFileName,
       "cienaCesSystemConfigErrLineNum": cienaCesSystemConfigErrLineNum,
       "cienaCesSystemConfigErrStr": cienaCesSystemConfigErrStr,
       "cienaCesSystemConfigErrLinesTotal": cienaCesSystemConfigErrLinesTotal,
       "cienaCesCommandFileHost": cienaCesCommandFileHost,
       "cienaCesCommandFileName": cienaCesCommandFileName,
       "cienaCesCommandFileError": cienaCesCommandFileError,
       "cienaCesSystemConfigMIBConformance": cienaCesSystemConfigMIBConformance,
       "cienaCesSystemConfigCompliances": cienaCesSystemConfigCompliances,
       "cienaCesSystemConfigMIBGroups": cienaCesSystemConfigMIBGroups,
       "cienaCesSystemConfigMIBNotificationPrefix": cienaCesSystemConfigMIBNotificationPrefix,
       "cienaCesSystemConfigMIBNotifications": cienaCesSystemConfigMIBNotifications,
       "cienaCesImproperCmdInConfigFile": cienaCesImproperCmdInConfigFile,
       "cienaCesCommandFileCompletedNotification": cienaCesCommandFileCompletedNotification,
       "cienaCesCommandFileFailedNotification": cienaCesCommandFileFailedNotification}
)
