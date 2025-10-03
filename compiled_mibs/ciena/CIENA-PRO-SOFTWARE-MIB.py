# SNMP MIB module (CIENA-PRO-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-PRO-SOFTWARE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:59 2025
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

(DateTime,) = mibBuilder.importSymbols(
    "CIENA-PRO-TYPES-MIB",
    "DateTime")

(cienaPro,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaPro")

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

cienaProSoftwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2)
)
if mibBuilder.loadTexts:
    cienaProSoftwareMIB.setRevisions(
        ("2020-10-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UpgradeOpState(TextualConvention, Integer32):
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("idle", 1),
          ("loadInProgress", 2),
          ("loadComplete", 3),
          ("loadFailed", 4),
          ("invokeInProgress", 5),
          ("invokeComplete", 6),
          ("invokeFailed", 7),
          ("installationInProgress", 8),
          ("installationComplete", 9),
          ("installationFailed", 10),
          ("commitInProgress", 11),
          ("commitComplete", 12),
          ("commitFailed", 13),
          ("cancelInProgress", 14),
          ("cancelComplete", 15),
          ("cancelFailed", 16),
          ("deleteInProgress", 17),
          ("deleteComplete", 18),
          ("deleteFailed", 19),
          ("automaticUpgradeInProgress", 20),
          ("automaticUpgradeComplete", 21),
          ("automaticUpgradeFailed", 22),
          ("moduleColdRestartRequired", 23),
          ("componentUpgradeInProgress", 24),
          ("componentUpgradeComplete", 25),
          ("componentUpgradeFailed", 26),
          ("deliveryInProgress", 27),
          ("deliveryComplete", 28),
          ("deliveryFailed", 29))
    )



class UpgradeOperation(TextualConvention, Integer32):
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
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("none", 1),
          ("softwareInstall", 2),
          ("softwareDeliver", 3),
          ("softwareLoad", 4),
          ("softwareActivate", 5),
          ("softwareCommit", 6),
          ("softwareCancel", 7),
          ("softwareDelete", 8),
          ("autoUpgrade", 9))
    )



class OperationResultType(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("unknownError", 2),
          ("timeout", 3),
          ("packageDeliveryFailure", 4),
          ("packageValidationFailure", 5),
          ("insufficientDiskSpace", 6),
          ("packageExtractionFailure", 7),
          ("systemError", 8),
          ("dependentServiceError", 9),
          ("packageInformationUnavailable", 10),
          ("upgradeVersionUnknown", 11),
          ("authenticationFailure", 12),
          ("fileNotFound", 13),
          ("fileTransferFailure", 14),
          ("invalidUri", 15),
          ("invalidState", 16),
          ("dataConversionFailure", 17),
          ("licenseCheckFailure", 18))
    )



# MIB Managed Objects in the order of their OIDs

_CienaProSoftware_ObjectIdentity = ObjectIdentity
cienaProSoftware = _CienaProSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1)
)
_CienaProSoftwareUpgradeOperationalState_Type = UpgradeOpState
_CienaProSoftwareUpgradeOperationalState_Object = MibScalar
cienaProSoftwareUpgradeOperationalState = _CienaProSoftwareUpgradeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 1),
    _CienaProSoftwareUpgradeOperationalState_Type()
)
cienaProSoftwareUpgradeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareUpgradeOperationalState.setStatus("current")
_CienaProSoftwareEntityReportedState_Type = UpgradeOpState
_CienaProSoftwareEntityReportedState_Object = MibScalar
cienaProSoftwareEntityReportedState = _CienaProSoftwareEntityReportedState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 2),
    _CienaProSoftwareEntityReportedState_Type()
)
cienaProSoftwareEntityReportedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareEntityReportedState.setStatus("current")
_CienaProSoftwareOperationInProgress_Type = UpgradeOperation
_CienaProSoftwareOperationInProgress_Object = MibScalar
cienaProSoftwareOperationInProgress = _CienaProSoftwareOperationInProgress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 3),
    _CienaProSoftwareOperationInProgress_Type()
)
cienaProSoftwareOperationInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareOperationInProgress.setStatus("current")
_CienaProSoftwareOperationStartTimestamp_Type = DateTime
_CienaProSoftwareOperationStartTimestamp_Object = MibScalar
cienaProSoftwareOperationStartTimestamp = _CienaProSoftwareOperationStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 4),
    _CienaProSoftwareOperationStartTimestamp_Type()
)
cienaProSoftwareOperationStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareOperationStartTimestamp.setStatus("current")
_CienaProSoftwareLastOperation_Type = UpgradeOperation
_CienaProSoftwareLastOperation_Object = MibScalar
cienaProSoftwareLastOperation = _CienaProSoftwareLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 5),
    _CienaProSoftwareLastOperation_Type()
)
cienaProSoftwareLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareLastOperation.setStatus("current")
_CienaProSoftwareLastOperationResult_Type = OperationResultType
_CienaProSoftwareLastOperationResult_Object = MibScalar
cienaProSoftwareLastOperationResult = _CienaProSoftwareLastOperationResult_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 6),
    _CienaProSoftwareLastOperationResult_Type()
)
cienaProSoftwareLastOperationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareLastOperationResult.setStatus("current")
_CienaProSoftwareLastOperationResultStr_Type = OctetString
_CienaProSoftwareLastOperationResultStr_Object = MibScalar
cienaProSoftwareLastOperationResultStr = _CienaProSoftwareLastOperationResultStr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 7),
    _CienaProSoftwareLastOperationResultStr_Type()
)
cienaProSoftwareLastOperationResultStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareLastOperationResultStr.setStatus("current")
_CienaProSoftwareLastOperationStartTimestamp_Type = DateTime
_CienaProSoftwareLastOperationStartTimestamp_Object = MibScalar
cienaProSoftwareLastOperationStartTimestamp = _CienaProSoftwareLastOperationStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 8),
    _CienaProSoftwareLastOperationStartTimestamp_Type()
)
cienaProSoftwareLastOperationStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareLastOperationStartTimestamp.setStatus("current")
_CienaProSoftwareLastOperationEndTimestamp_Type = DateTime
_CienaProSoftwareLastOperationEndTimestamp_Object = MibScalar
cienaProSoftwareLastOperationEndTimestamp = _CienaProSoftwareLastOperationEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 9),
    _CienaProSoftwareLastOperationEndTimestamp_Type()
)
cienaProSoftwareLastOperationEndTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareLastOperationEndTimestamp.setStatus("current")
_CienaProSoftwareCommittedVersion_Type = OctetString
_CienaProSoftwareCommittedVersion_Object = MibScalar
cienaProSoftwareCommittedVersion = _CienaProSoftwareCommittedVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 10),
    _CienaProSoftwareCommittedVersion_Type()
)
cienaProSoftwareCommittedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareCommittedVersion.setStatus("current")
_CienaProSoftwareActiveVersion_Type = OctetString
_CienaProSoftwareActiveVersion_Object = MibScalar
cienaProSoftwareActiveVersion = _CienaProSoftwareActiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 11),
    _CienaProSoftwareActiveVersion_Type()
)
cienaProSoftwareActiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareActiveVersion.setStatus("current")
_CienaProSoftwareUpgradeToVersion_Type = OctetString
_CienaProSoftwareUpgradeToVersion_Object = MibScalar
cienaProSoftwareUpgradeToVersion = _CienaProSoftwareUpgradeToVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 12),
    _CienaProSoftwareUpgradeToVersion_Type()
)
cienaProSoftwareUpgradeToVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareUpgradeToVersion.setStatus("current")
_CienaProSoftwareRunningVersion_Type = OctetString
_CienaProSoftwareRunningVersion_Object = MibScalar
cienaProSoftwareRunningVersion = _CienaProSoftwareRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 30, 2, 1, 13),
    _CienaProSoftwareRunningVersion_Type()
)
cienaProSoftwareRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaProSoftwareRunningVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-PRO-SOFTWARE-MIB",
    **{"UpgradeOpState": UpgradeOpState,
       "UpgradeOperation": UpgradeOperation,
       "OperationResultType": OperationResultType,
       "cienaProSoftwareMIB": cienaProSoftwareMIB,
       "cienaProSoftware": cienaProSoftware,
       "cienaProSoftwareUpgradeOperationalState": cienaProSoftwareUpgradeOperationalState,
       "cienaProSoftwareEntityReportedState": cienaProSoftwareEntityReportedState,
       "cienaProSoftwareOperationInProgress": cienaProSoftwareOperationInProgress,
       "cienaProSoftwareOperationStartTimestamp": cienaProSoftwareOperationStartTimestamp,
       "cienaProSoftwareLastOperation": cienaProSoftwareLastOperation,
       "cienaProSoftwareLastOperationResult": cienaProSoftwareLastOperationResult,
       "cienaProSoftwareLastOperationResultStr": cienaProSoftwareLastOperationResultStr,
       "cienaProSoftwareLastOperationStartTimestamp": cienaProSoftwareLastOperationStartTimestamp,
       "cienaProSoftwareLastOperationEndTimestamp": cienaProSoftwareLastOperationEndTimestamp,
       "cienaProSoftwareCommittedVersion": cienaProSoftwareCommittedVersion,
       "cienaProSoftwareActiveVersion": cienaProSoftwareActiveVersion,
       "cienaProSoftwareUpgradeToVersion": cienaProSoftwareUpgradeToVersion,
       "cienaProSoftwareRunningVersion": cienaProSoftwareRunningVersion}
)
