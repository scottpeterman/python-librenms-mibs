# SNMP MIB module (TELESTE-LUMINATO-MIB2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teleste\TELESTE-LUMINATO-MIB2
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:04 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(luminato,) = mibBuilder.importSymbols(
    "TELESTE-ROOT-MIB",
    "luminato")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4)
)
_Params_ObjectIdentity = ObjectIdentity
params = _Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1)
)


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("severityEmergency", 0),
          ("severityAlert", 1),
          ("severityCritical", 2),
          ("severityError", 3),
          ("severityWarning", 4),
          ("severityNotice", 5),
          ("severityInformational", 6),
          ("severityDebug", 7),
          ("severityNominal", 8))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 1),
    _Severity_Type()
)
severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    severity.setStatus("current")


class _Module_Type(Integer32):
    """Custom type module based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("moduleChassis", 0),
          ("moduleSlot1", 1),
          ("moduleSlot2", 2),
          ("moduleSlot3", 3),
          ("moduleSlot4", 4),
          ("moduleSlot5", 5),
          ("moduleSlot6", 6),
          ("modulePsu", 7))
    )


_Module_Type.__name__ = "Integer32"
_Module_Object = MibScalar
module = _Module_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 2),
    _Module_Type()
)
module.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    module.setStatus("current")
_Description_Type = OctetString
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 8),
    _Description_Type()
)
description.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    description.setStatus("current")
_Reason_Type = Unsigned32
_Reason_Object = MibScalar
reason = _Reason_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 10),
    _Reason_Type()
)
reason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    reason.setStatus("current")
_ParamTable_Object = MibTable
paramTable = _ParamTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 11)
)
if mibBuilder.loadTexts:
    paramTable.setStatus("optional")
_ParamEntry_Object = MibTableRow
paramEntry = _ParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 11, 1)
)
paramEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB2", "paramIdx"),
)
if mibBuilder.loadTexts:
    paramEntry.setStatus("current")


class _ParamIdx_Type(Integer32):
    """Custom type paramIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ParamIdx_Type.__name__ = "Integer32"
_ParamIdx_Object = MibTableColumn
paramIdx = _ParamIdx_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 11, 1, 1),
    _ParamIdx_Type()
)
paramIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    paramIdx.setStatus("current")
_ParamValue_Type = Unsigned32
_ParamValue_Object = MibTableColumn
paramValue = _ParamValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 1, 11, 1, 2),
    _ParamValue_Type()
)
paramValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    paramValue.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 1)
)
_Specific_ObjectIdentity = ObjectIdentity
specific = _Specific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2)
)

# Managed Objects groups


# Notification objects

extendedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 1, 1)
)
extendedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedAlarmEvent.setStatus(
        "current"
    )

extendedPidMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 2)
)
extendedPidMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPidMissingAlarmEvent.setStatus(
        "current"
    )

extendedServiceMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 3)
)
extendedServiceMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedServiceMissingAlarmEvent.setStatus(
        "current"
    )

extendedPidConflictAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4)
)
extendedPidConflictAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPidConflictAlarmEvent.setStatus(
        "current"
    )

extendedTemperatureTooHighAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 6)
)
extendedTemperatureTooHighAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedTemperatureTooHighAlarmEvent.setStatus(
        "current"
    )

extendedTemperatureTooLowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 7)
)
extendedTemperatureTooLowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedTemperatureTooLowAlarmEvent.setStatus(
        "current"
    )

extendedManualTableInsertionFailedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 8)
)
extendedManualTableInsertionFailedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedManualTableInsertionFailedAlarmEvent.setStatus(
        "current"
    )

extendedAlertMessageAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 10)
)
extendedAlertMessageAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedAlertMessageAlarmEvent.setStatus(
        "current"
    )

extendedServicesPassthroughAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 11)
)
extendedServicesPassthroughAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedServicesPassthroughAlarmEvent.setStatus(
        "current"
    )

extendedEcmStreamCannotBeAttachedToIncompatibleCwgAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 13)
)
extendedEcmStreamCannotBeAttachedToIncompatibleCwgAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEcmStreamCannotBeAttachedToIncompatibleCwgAlarmEvent.setStatus(
        "current"
    )

extendedPsigTableInsertionFailedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 15)
)
extendedPsigTableInsertionFailedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsigTableInsertionFailedAlarmEvent.setStatus(
        "current"
    )

extendedPsiTableCaptureFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 17)
)
extendedPsiTableCaptureFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsiTableCaptureFailureAlarmEvent.setStatus(
        "current"
    )

extendedSignalMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 18)
)
extendedSignalMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSignalMissingAlarmEvent.setStatus(
        "current"
    )

extendedNoTsSyncAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 19)
)
extendedNoTsSyncAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNoTsSyncAlarmEvent.setStatus(
        "current"
    )

extendedTsRxErrorsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 20)
)
extendedTsRxErrorsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedTsRxErrorsAlarmEvent.setStatus(
        "current"
    )

extendedTsInputBufferOverflowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 21)
)
extendedTsInputBufferOverflowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedTsInputBufferOverflowAlarmEvent.setStatus(
        "current"
    )

extendedAsiLinkDownAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 22)
)
extendedAsiLinkDownAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedAsiLinkDownAlarmEvent.setStatus(
        "current"
    )

extendedForbiddenNetworkAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 23)
)
extendedForbiddenNetworkAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedForbiddenNetworkAlarmEvent.setStatus(
        "current"
    )

extendedSidConflictAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 24)
)
extendedSidConflictAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSidConflictAlarmEvent.setStatus(
        "current"
    )

extendedLinkMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 25)
)
extendedLinkMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedLinkMissingAlarmEvent.setStatus(
        "current"
    )

extendedEcmMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 26)
)
extendedEcmMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEcmMissingAlarmEvent.setStatus(
        "current"
    )

extendedScramblingConflictInSharedComponentAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 27)
)
extendedScramblingConflictInSharedComponentAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedScramblingConflictInSharedComponentAlarmEvent.setStatus(
        "current"
    )

extendedScrambledSharedComponentAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 28)
)
extendedScrambledSharedComponentAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedScrambledSharedComponentAlarmEvent.setStatus(
        "current"
    )

extendedUsedInputIsNotSptsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 29)
)
extendedUsedInputIsNotSptsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUsedInputIsNotSptsAlarmEvent.setStatus(
        "current"
    )

extendedConfigurationErrorAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 30)
)
extendedConfigurationErrorAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedConfigurationErrorAlarmEvent.setStatus(
        "current"
    )

extendedDescramblingFailedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 31)
)
extendedDescramblingFailedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDescramblingFailedAlarmEvent.setStatus(
        "current"
    )

extendedCwGroupConflictAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 32)
)
extendedCwGroupConflictAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCwGroupConflictAlarmEvent.setStatus(
        "current"
    )

extendedInvalidSdtTemplateAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 33)
)
extendedInvalidSdtTemplateAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedInvalidSdtTemplateAlarmEvent.setStatus(
        "current"
    )

extendedCannotDescrambleDueToCamRoutingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 34)
)
extendedCannotDescrambleDueToCamRoutingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCannotDescrambleDueToCamRoutingAlarmEvent.setStatus(
        "current"
    )

extendedRedundancyActivatedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 35)
)
extendedRedundancyActivatedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRedundancyActivatedAlarmEvent.setStatus(
        "current"
    )

extendedRtpInputPacketSequenceAnomaliesDetectedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 36)
)
extendedRtpInputPacketSequenceAnomaliesDetectedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRtpInputPacketSequenceAnomaliesDetectedAlarmEvent.setStatus(
        "current"
    )

extendedRtpInputErrorsDroppedPacketsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 37)
)
extendedRtpInputErrorsDroppedPacketsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRtpInputErrorsDroppedPacketsAlarmEvent.setStatus(
        "current"
    )

extendedFecHasCorrectedPacketsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 38)
)
extendedFecHasCorrectedPacketsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFecHasCorrectedPacketsAlarmEvent.setStatus(
        "current"
    )

extendedFecInputAnomaliesDetectedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 39)
)
extendedFecInputAnomaliesDetectedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFecInputAnomaliesDetectedAlarmEvent.setStatus(
        "current"
    )

extendedFecErrorCorrectionCapacityExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 40)
)
extendedFecErrorCorrectionCapacityExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFecErrorCorrectionCapacityExceededAlarmEvent.setStatus(
        "current"
    )

extendedTooManyServicesAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 42)
)
extendedTooManyServicesAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedTooManyServicesAlarmEvent.setStatus(
        "current"
    )

extendedLowSignalLevelAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 43)
)
extendedLowSignalLevelAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedLowSignalLevelAlarmEvent.setStatus(
        "current"
    )

extendedSignalMutedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 44)
)
extendedSignalMutedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSignalMutedAlarmEvent.setStatus(
        "current"
    )

extendedProidiomScramblingDisabledAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 45)
)
extendedProidiomScramblingDisabledAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedProidiomScramblingDisabledAlarmEvent.setStatus(
        "current"
    )

extendedVmxConnectionLostAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 46)
)
extendedVmxConnectionLostAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedVmxConnectionLostAlarmEvent.setStatus(
        "current"
    )

extendedControlWordErrorAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 47)
)
extendedControlWordErrorAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedControlWordErrorAlarmEvent.setStatus(
        "current"
    )

extendedOutputServiceCapacityExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 48)
)
extendedOutputServiceCapacityExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedOutputServiceCapacityExceededAlarmEvent.setStatus(
        "current"
    )

extendedLowSignalQualityAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 49)
)
extendedLowSignalQualityAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedLowSignalQualityAlarmEvent.setStatus(
        "current"
    )

extendedModuleOffAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4096)
)
extendedModuleOffAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedModuleOffAlarmEvent.setStatus(
        "current"
    )

extendedPidCapacityExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4104)
)
extendedPidCapacityExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPidCapacityExceededAlarmEvent.setStatus(
        "current"
    )

extendedPsiSiCaptureCapacityExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4105)
)
extendedPsiSiCaptureCapacityExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsiSiCaptureCapacityExceededAlarmEvent.setStatus(
        "current"
    )

extendedOutOfServiceIdsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4106)
)
extendedOutOfServiceIdsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedOutOfServiceIdsAlarmEvent.setStatus(
        "current"
    )

extendedCaModuleMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4108)
)
extendedCaModuleMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCaModuleMissingAlarmEvent.setStatus(
        "current"
    )

extendedPsiSiInsertCapacityExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4109)
)
extendedPsiSiInsertCapacityExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsiSiInsertCapacityExceededAlarmEvent.setStatus(
        "current"
    )

extendedMultiplexOversubscriptionPacketsDiscardedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4110)
)
extendedMultiplexOversubscriptionPacketsDiscardedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMultiplexOversubscriptionPacketsDiscardedAlarmEvent.setStatus(
        "current"
    )

extendedUnknownModuleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4111)
)
extendedUnknownModuleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUnknownModuleAlarmEvent.setStatus(
        "current"
    )

extendedMainVoltageTooHighAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4112)
)
extendedMainVoltageTooHighAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMainVoltageTooHighAlarmEvent.setStatus(
        "current"
    )

extendedMainVoltageTooLowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4113)
)
extendedMainVoltageTooLowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMainVoltageTooLowAlarmEvent.setStatus(
        "current"
    )

extendedCurrentTooHighAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4114)
)
extendedCurrentTooHighAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCurrentTooHighAlarmEvent.setStatus(
        "current"
    )

extendedCurrentTooLowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4115)
)
extendedCurrentTooLowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCurrentTooLowAlarmEvent.setStatus(
        "current"
    )

extendedDaemonInitializationFailedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4127)
)
extendedDaemonInitializationFailedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDaemonInitializationFailedAlarmEvent.setStatus(
        "current"
    )

extendedDeviceDriverFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4129)
)
extendedDeviceDriverFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDeviceDriverFailureAlarmEvent.setStatus(
        "current"
    )

extendedHardwareFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4130)
)
extendedHardwareFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedHardwareFailureAlarmEvent.setStatus(
        "current"
    )

extendedFanFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4131)
)
extendedFanFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFanFailureAlarmEvent.setStatus(
        "current"
    )

extendedRunningOnBackupPowerAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4132)
)
extendedRunningOnBackupPowerAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRunningOnBackupPowerAlarmEvent.setStatus(
        "current"
    )

extendedPowerSupplyOverloadedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4133)
)
extendedPowerSupplyOverloadedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPowerSupplyOverloadedAlarmEvent.setStatus(
        "current"
    )

extendedBootingUpAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4134)
)
extendedBootingUpAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBootingUpAlarmEvent.setStatus(
        "current"
    )

extendedBootFailedRetryingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4135)
)
extendedBootFailedRetryingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBootFailedRetryingAlarmEvent.setStatus(
        "current"
    )

extendedBootFailedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4136)
)
extendedBootFailedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBootFailedAlarmEvent.setStatus(
        "current"
    )

extendedShuttingDownAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4137)
)
extendedShuttingDownAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedShuttingDownAlarmEvent.setStatus(
        "current"
    )

extendedConnectionLostAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4138)
)
extendedConnectionLostAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedConnectionLostAlarmEvent.setStatus(
        "current"
    )

extendedIncompatibleModuleDisabledAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4139)
)
extendedIncompatibleModuleDisabledAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedIncompatibleModuleDisabledAlarmEvent.setStatus(
        "current"
    )

extendedFailedToBootAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4141)
)
extendedFailedToBootAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFailedToBootAlarmEvent.setStatus(
        "current"
    )

extendedUpcTooLowInputPowerAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4147)
)
extendedUpcTooLowInputPowerAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUpcTooLowInputPowerAlarmEvent.setStatus(
        "current"
    )

extendedUpcTooHighInputPowerAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4148)
)
extendedUpcTooHighInputPowerAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUpcTooHighInputPowerAlarmEvent.setStatus(
        "current"
    )

extendedCalibrationDataMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4149)
)
extendedCalibrationDataMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCalibrationDataMissingAlarmEvent.setStatus(
        "current"
    )

extendedCalibrationCheckSkippedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4150)
)
extendedCalibrationCheckSkippedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCalibrationCheckSkippedAlarmEvent.setStatus(
        "current"
    )

extendedDescramblingFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4151)
)
extendedDescramblingFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDescramblingFailureAlarmEvent.setStatus(
        "current"
    )

extendedBackupSwitchedOverToBackupDeviceAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4153)
)
extendedBackupSwitchedOverToBackupDeviceAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupSwitchedOverToBackupDeviceAlarmEvent.setStatus(
        "current"
    )

extendedFailedToQuerySomeOfTheNitDataAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4157)
)
extendedFailedToQuerySomeOfTheNitDataAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFailedToQuerySomeOfTheNitDataAlarmEvent.setStatus(
        "current"
    )

extendedNitWizardFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4158)
)
extendedNitWizardFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNitWizardFailureAlarmEvent.setStatus(
        "current"
    )

extendedDuplicateFrequencyInTwoOrMoreSelectedQamOutputsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4159)
)
extendedDuplicateFrequencyInTwoOrMoreSelectedQamOutputsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDuplicateFrequencyInTwoOrMoreSelectedQamOutputsAlarmEvent.setStatus(
        "current"
    )

extendedCannotResolveTableVersionUsingDefaultAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4160)
)
extendedCannotResolveTableVersionUsingDefaultAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCannotResolveTableVersionUsingDefaultAlarmEvent.setStatus(
        "current"
    )

extendedUnsupportedConfigurationAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4175)
)
extendedUnsupportedConfigurationAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUnsupportedConfigurationAlarmEvent.setStatus(
        "current"
    )

extendedFrequencyOutOfRangeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4176)
)
extendedFrequencyOutOfRangeAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFrequencyOutOfRangeAlarmEvent.setStatus(
        "current"
    )

extendedOutputPowerOutOfRangeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4177)
)
extendedOutputPowerOutOfRangeAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedOutputPowerOutOfRangeAlarmEvent.setStatus(
        "current"
    )

extendedSymbolrateOutOfRangeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4178)
)
extendedSymbolrateOutOfRangeAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSymbolrateOutOfRangeAlarmEvent.setStatus(
        "current"
    )

extendedChannelDistanceTooNarrowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4179)
)
extendedChannelDistanceTooNarrowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedChannelDistanceTooNarrowAlarmEvent.setStatus(
        "current"
    )

extendedInvalidLnbVoltageConfigurationAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4180)
)
extendedInvalidLnbVoltageConfigurationAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedInvalidLnbVoltageConfigurationAlarmEvent.setStatus(
        "current"
    )

extendedInvalidFecRateForSelectedModulationAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4181)
)
extendedInvalidFecRateForSelectedModulationAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedInvalidFecRateForSelectedModulationAlarmEvent.setStatus(
        "current"
    )

extendedLnbCurrentAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4182)
)
extendedLnbCurrentAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedLnbCurrentAlarmEvent.setStatus(
        "current"
    )

extendedFrequencyOffsetAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4183)
)
extendedFrequencyOffsetAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFrequencyOffsetAlarmEvent.setStatus(
        "current"
    )

extendedRestartingDescramblingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4185)
)
extendedRestartingDescramblingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRestartingDescramblingAlarmEvent.setStatus(
        "current"
    )

extendedRebootingCamAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4186)
)
extendedRebootingCamAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRebootingCamAlarmEvent.setStatus(
        "current"
    )

extendedEcmgFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4187)
)
extendedEcmgFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEcmgFailureAlarmEvent.setStatus(
        "current"
    )

extendedEcmStreamFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4188)
)
extendedEcmStreamFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEcmStreamFailureAlarmEvent.setStatus(
        "current"
    )

extendedEmmFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4189)
)
extendedEmmFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEmmFailureAlarmEvent.setStatus(
        "current"
    )

extendedEmmStreamFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4190)
)
extendedEmmStreamFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEmmStreamFailureAlarmEvent.setStatus(
        "current"
    )

extendedEcmgNotConnectedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4191)
)
extendedEcmgNotConnectedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEcmgNotConnectedAlarmEvent.setStatus(
        "current"
    )

extendedEmmNotConnectedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4192)
)
extendedEmmNotConnectedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEmmNotConnectedAlarmEvent.setStatus(
        "current"
    )

extendedScsNotLicensedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4193)
)
extendedScsNotLicensedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedScsNotLicensedAlarmEvent.setStatus(
        "current"
    )

extendedEcmgSwitchedToSpareServerAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4194)
)
extendedEcmgSwitchedToSpareServerAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEcmgSwitchedToSpareServerAlarmEvent.setStatus(
        "current"
    )

extendedUpdatedBootLoaderAvailableAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4195)
)
extendedUpdatedBootLoaderAvailableAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUpdatedBootLoaderAvailableAlarmEvent.setStatus(
        "current"
    )

extendedUpdatingStage1BootLoaderAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4196)
)
extendedUpdatingStage1BootLoaderAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUpdatingStage1BootLoaderAlarmEvent.setStatus(
        "current"
    )

extendedUpdatingStage2BootLoaderAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4197)
)
extendedUpdatingStage2BootLoaderAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUpdatingStage2BootLoaderAlarmEvent.setStatus(
        "current"
    )

extendedFailedToUpdateStage1BootLoaderAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4198)
)
extendedFailedToUpdateStage1BootLoaderAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFailedToUpdateStage1BootLoaderAlarmEvent.setStatus(
        "current"
    )

extendedFailedToUpdateStage2BootLoaderAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4199)
)
extendedFailedToUpdateStage2BootLoaderAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFailedToUpdateStage2BootLoaderAlarmEvent.setStatus(
        "current"
    )

extendedBackupActiveBackupAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4203)
)
extendedBackupActiveBackupAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupActiveBackupAlarmEvent.setStatus(
        "current"
    )

extendedConfiguringModuleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4205)
)
extendedConfiguringModuleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedConfiguringModuleAlarmEvent.setStatus(
        "current"
    )

extendedNoModuleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4206)
)
extendedNoModuleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNoModuleAlarmEvent.setStatus(
        "current"
    )

extendedProcessStartedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4208)
)
extendedProcessStartedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedProcessStartedAlarmEvent.setStatus(
        "current"
    )

extendedBackupLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4209)
)
extendedBackupLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedMultiplexingLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4211)
)
extendedMultiplexingLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMultiplexingLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedDemultiplexingLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4212)
)
extendedDemultiplexingLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDemultiplexingLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedDvbProcessingLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4213)
)
extendedDvbProcessingLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDvbProcessingLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedMsdLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4214)
)
extendedMsdLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMsdLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedDvbS2LicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4215)
)
extendedDvbS2LicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDvbS2LicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedScramblingLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4216)
)
extendedScramblingLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedScramblingLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedScsLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4217)
)
extendedScsLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedScsLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedUserFromGroupAdminIsUsingCliAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4218)
)
extendedUserFromGroupAdminIsUsingCliAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUserFromGroupAdminIsUsingCliAlarmEvent.setStatus(
        "current"
    )

extendedUserFromGroupInstallIsUsingCliAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4219)
)
extendedUserFromGroupInstallIsUsingCliAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUserFromGroupInstallIsUsingCliAlarmEvent.setStatus(
        "current"
    )

extendedUserFromGroupOperIsUsingCliAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4220)
)
extendedUserFromGroupOperIsUsingCliAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUserFromGroupOperIsUsingCliAlarmEvent.setStatus(
        "current"
    )

extendedUserFromGroupMonitorIsUsingCliAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4221)
)
extendedUserFromGroupMonitorIsUsingCliAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUserFromGroupMonitorIsUsingCliAlarmEvent.setStatus(
        "current"
    )

extendedExtIoSignaledAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4223)
)
extendedExtIoSignaledAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedExtIoSignaledAlarmEvent.setStatus(
        "current"
    )

extendedExtIoBackupPowerSupplyFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4224)
)
extendedExtIoBackupPowerSupplyFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedExtIoBackupPowerSupplyFailureAlarmEvent.setStatus(
        "current"
    )

extendedExtIoIntrusionDetectedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4225)
)
extendedExtIoIntrusionDetectedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedExtIoIntrusionDetectedAlarmEvent.setStatus(
        "current"
    )

extendedRedundancyFailedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4227)
)
extendedRedundancyFailedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRedundancyFailedAlarmEvent.setStatus(
        "current"
    )

extendedMultiplexOversubscriptionPacketsDelayedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4228)
)
extendedMultiplexOversubscriptionPacketsDelayedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMultiplexOversubscriptionPacketsDelayedAlarmEvent.setStatus(
        "current"
    )

extendedCbrOutputOversubscriptionAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4229)
)
extendedCbrOutputOversubscriptionAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCbrOutputOversubscriptionAlarmEvent.setStatus(
        "current"
    )

extendedBackupHwDoesNotSupportSelectedDeviceRoleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4230)
)
extendedBackupHwDoesNotSupportSelectedDeviceRoleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupHwDoesNotSupportSelectedDeviceRoleAlarmEvent.setStatus(
        "current"
    )

extendedSoftwareUpdateInProgressAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4231)
)
extendedSoftwareUpdateInProgressAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSoftwareUpdateInProgressAlarmEvent.setStatus(
        "current"
    )

extendedSoftwareUpdateReadyWaitingForRebootToCompleteAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4232)
)
extendedSoftwareUpdateReadyWaitingForRebootToCompleteAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSoftwareUpdateReadyWaitingForRebootToCompleteAlarmEvent.setStatus(
        "current"
    )

extendedSoftwareUpdateFailedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4233)
)
extendedSoftwareUpdateFailedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSoftwareUpdateFailedAlarmEvent.setStatus(
        "current"
    )

extendedBackupModuleHwDoesNotSupportSelectedOnePlusOneBackupRoleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4234)
)
extendedBackupModuleHwDoesNotSupportSelectedOnePlusOneBackupRoleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupModuleHwDoesNotSupportSelectedOnePlusOneBackupRoleAlarmEvent.setStatus(
        "current"
    )

extendedEitProcessingLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4235)
)
extendedEitProcessingLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEitProcessingLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedCbrOutputOversubscriptionPacketsDiscardedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4236)
)
extendedCbrOutputOversubscriptionPacketsDiscardedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCbrOutputOversubscriptionPacketsDiscardedAlarmEvent.setStatus(
        "current"
    )

extendedIpInputCapacityExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4238)
)
extendedIpInputCapacityExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedIpInputCapacityExceededAlarmEvent.setStatus(
        "current"
    )

extendedEitReinsertCapacityExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4239)
)
extendedEitReinsertCapacityExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEitReinsertCapacityExceededAlarmEvent.setStatus(
        "current"
    )

extendedDvbTimeMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4243)
)
extendedDvbTimeMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDvbTimeMissingAlarmEvent.setStatus(
        "current"
    )

extendedDvbT2LicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4244)
)
extendedDvbT2LicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDvbT2LicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedDcFeedCurrentAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4245)
)
extendedDcFeedCurrentAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDcFeedCurrentAlarmEvent.setStatus(
        "current"
    )

extendedNotGeneratingTdtTotTableWaitingForCorrectSystemTimeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4246)
)
extendedNotGeneratingTdtTotTableWaitingForCorrectSystemTimeAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNotGeneratingTdtTotTableWaitingForCorrectSystemTimeAlarmEvent.setStatus(
        "current"
    )

extendedDataPlpIdSelectionRequiredAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4247)
)
extendedDataPlpIdSelectionRequiredAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDataPlpIdSelectionRequiredAlarmEvent.setStatus(
        "current"
    )

extendedDataPlpIdSelectionNotValidAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4248)
)
extendedDataPlpIdSelectionNotValidAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDataPlpIdSelectionNotValidAlarmEvent.setStatus(
        "current"
    )

extendedHierarchyHpSelectedForNonAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4249)
)
extendedHierarchyHpSelectedForNonAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedHierarchyHpSelectedForNonAlarmEvent.setStatus(
        "current"
    )

extendedBackupVoltageTooHighAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4253)
)
extendedBackupVoltageTooHighAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupVoltageTooHighAlarmEvent.setStatus(
        "current"
    )

extendedBackupVoltageTooLowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4254)
)
extendedBackupVoltageTooLowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupVoltageTooLowAlarmEvent.setStatus(
        "current"
    )

extendedCamFailureActionTakenRestartingDescramblingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4256)
)
extendedCamFailureActionTakenRestartingDescramblingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCamFailureActionTakenRestartingDescramblingAlarmEvent.setStatus(
        "current"
    )

extendedCamFailureActionTakenRebootingCaModuleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4257)
)
extendedCamFailureActionTakenRebootingCaModuleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCamFailureActionTakenRebootingCaModuleAlarmEvent.setStatus(
        "current"
    )

extendedCaMenuIsOpenAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4258)
)
extendedCaMenuIsOpenAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedCaMenuIsOpenAlarmEvent.setStatus(
        "current"
    )

extendedNitSidConflictAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4260)
)
extendedNitSidConflictAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNitSidConflictAlarmEvent.setStatus(
        "current"
    )

extendedNotGeneratingSttTableWaitingForCorrectSystemTimeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4261)
)
extendedNotGeneratingSttTableWaitingForCorrectSystemTimeAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNotGeneratingSttTableWaitingForCorrectSystemTimeAlarmEvent.setStatus(
        "current"
    )

extendedNumberOfFecLicensesExceededAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4262)
)
extendedNumberOfFecLicensesExceededAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNumberOfFecLicensesExceededAlarmEvent.setStatus(
        "current"
    )

extendedErrorCorrectionOverloadTooManySimultaneousMissingPacketsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4263)
)
extendedErrorCorrectionOverloadTooManySimultaneousMissingPacketsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedErrorCorrectionOverloadTooManySimultaneousMissingPacketsAlarmEvent.setStatus(
        "current"
    )

extendedFecPacketsDiscardedModuleBitrateTooHighAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4264)
)
extendedFecPacketsDiscardedModuleBitrateTooHighAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFecPacketsDiscardedModuleBitrateTooHighAlarmEvent.setStatus(
        "current"
    )

extendedMediaPacketsDiscardedModuleBitrateTooHighAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4265)
)
extendedMediaPacketsDiscardedModuleBitrateTooHighAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMediaPacketsDiscardedModuleBitrateTooHighAlarmEvent.setStatus(
        "current"
    )

extendedSfpLinkDownAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4269)
)
extendedSfpLinkDownAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSfpLinkDownAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncTurnedOffAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4272)
)
extendedBackupsyncTurnedOffAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncTurnedOffAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncManualModeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4273)
)
extendedBackupsyncManualModeAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncManualModeAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncAutomaticModeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4274)
)
extendedBackupsyncAutomaticModeAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncAutomaticModeAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncConfigurationWillBeSynchronizedAutomaticallyAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4275)
)
extendedBackupsyncConfigurationWillBeSynchronizedAutomaticallyAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncConfigurationWillBeSynchronizedAutomaticallyAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncSynchronizingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4276)
)
extendedBackupsyncSynchronizingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncSynchronizingAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncSwCompatibilityCheckAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4278)
)
extendedBackupsyncSwCompatibilityCheckAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncSwCompatibilityCheckAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncHwCompatibilityCheckAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4279)
)
extendedBackupsyncHwCompatibilityCheckAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncHwCompatibilityCheckAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncConfigurationFaultAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4280)
)
extendedBackupsyncConfigurationFaultAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncConfigurationFaultAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncConnectionLostAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4281)
)
extendedBackupsyncConnectionLostAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncConnectionLostAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncAutosyncNotPossibleFromBackupToMainAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4283)
)
extendedBackupsyncAutosyncNotPossibleFromBackupToMainAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncAutosyncNotPossibleFromBackupToMainAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncRebootingPairDeviceToNewConfigurationAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4284)
)
extendedBackupsyncRebootingPairDeviceToNewConfigurationAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncRebootingPairDeviceToNewConfigurationAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncCheckLicenseCompatibilityAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4285)
)
extendedBackupsyncCheckLicenseCompatibilityAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncCheckLicenseCompatibilityAlarmEvent.setStatus(
        "current"
    )

extendedBackupsyncLicenseCompatibilityCheckAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4286)
)
extendedBackupsyncLicenseCompatibilityCheckAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupsyncLicenseCompatibilityCheckAlarmEvent.setStatus(
        "current"
    )

extendedDeviceFirstBootActionsAreInProgressAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4288)
)
extendedDeviceFirstBootActionsAreInProgressAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDeviceFirstBootActionsAreInProgressAlarmEvent.setStatus(
        "current"
    )

extendedDeviceConfigurationBackupInProgressAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4289)
)
extendedDeviceConfigurationBackupInProgressAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDeviceConfigurationBackupInProgressAlarmEvent.setStatus(
        "current"
    )

extendedDeviceConfigurationRestoreInProgressAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4290)
)
extendedDeviceConfigurationRestoreInProgressAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDeviceConfigurationRestoreInProgressAlarmEvent.setStatus(
        "current"
    )

extendedDeviceOtherSoftwareActivationAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4291)
)
extendedDeviceOtherSoftwareActivationAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDeviceOtherSoftwareActivationAlarmEvent.setStatus(
        "current"
    )

extendedTooManyOutputPidsConfiguredAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4292)
)
extendedTooManyOutputPidsConfiguredAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedTooManyOutputPidsConfiguredAlarmEvent.setStatus(
        "current"
    )

extendedRebootRequestByUserAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4293)
)
extendedRebootRequestByUserAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRebootRequestByUserAlarmEvent.setStatus(
        "current"
    )

extendedRemovedFromTheChassisAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4294)
)
extendedRemovedFromTheChassisAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedRemovedFromTheChassisAlarmEvent.setStatus(
        "current"
    )

extendedInsertedIntoTheChassisAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4295)
)
extendedInsertedIntoTheChassisAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedInsertedIntoTheChassisAlarmEvent.setStatus(
        "current"
    )

extendedPacketsDiscardedInIpMirrorOutputsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4297)
)
extendedPacketsDiscardedInIpMirrorOutputsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPacketsDiscardedInIpMirrorOutputsAlarmEvent.setStatus(
        "current"
    )

extendedAesLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4298)
)
extendedAesLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedAesLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedSymbolRateTooHighForSelectedModulationSelectHighSpeedModulationModeToAvoidErrorsAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4299)
)
extendedSymbolRateTooHighForSelectedModulationSelectHighSpeedModulationModeToAvoidErrorsAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSymbolRateTooHighForSelectedModulationSelectHighSpeedModulationModeToAvoidErrorsAlarmEvent.setStatus(
        "current"
    )

extendedEcmResponsesDelayedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4300)
)
extendedEcmResponsesDelayedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEcmResponsesDelayedAlarmEvent.setStatus(
        "current"
    )

extendedDisconnectedHostInMultichassisGroupAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4302)
)
extendedDisconnectedHostInMultichassisGroupAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDisconnectedHostInMultichassisGroupAlarmEvent.setStatus(
        "current"
    )

extendedMultichassisConfigurationFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4303)
)
extendedMultichassisConfigurationFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedMultichassisConfigurationFailureAlarmEvent.setStatus(
        "current"
    )

extendedSwVersionDifferenceWithinMultichassisGroupAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4304)
)
extendedSwVersionDifferenceWithinMultichassisGroupAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSwVersionDifferenceWithinMultichassisGroupAlarmEvent.setStatus(
        "current"
    )

extendedSwVersionMismatchAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4305)
)
extendedSwVersionMismatchAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedSwVersionMismatchAlarmEvent.setStatus(
        "current"
    )

extendedEmergencySignalActivatedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4307)
)
extendedEmergencySignalActivatedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEmergencySignalActivatedAlarmEvent.setStatus(
        "current"
    )

extendedEmergencySignalMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4308)
)
extendedEmergencySignalMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEmergencySignalMissingAlarmEvent.setStatus(
        "current"
    )

extendedUnableToAddEmergencySignalAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4309)
)
extendedUnableToAddEmergencySignalAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUnableToAddEmergencySignalAlarmEvent.setStatus(
        "current"
    )

extendedNetworkInformationTableNeedsToBeUpdatedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4310)
)
extendedNetworkInformationTableNeedsToBeUpdatedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNetworkInformationTableNeedsToBeUpdatedAlarmEvent.setStatus(
        "current"
    )

extendedNfsMountFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4311)
)
extendedNfsMountFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedNfsMountFailureAlarmEvent.setStatus(
        "current"
    )

extendedEthernetInputBufferOverflowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4312)
)
extendedEthernetInputBufferOverflowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedEthernetInputBufferOverflowAlarmEvent.setStatus(
        "current"
    )

extendedDvbAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4313)
)
extendedDvbAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDvbAlarmEvent.setStatus(
        "current"
    )

extendedPoweredOffAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4315)
)
extendedPoweredOffAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPoweredOffAlarmEvent.setStatus(
        "current"
    )

extendedPsu1NoModuleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4316)
)
extendedPsu1NoModuleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu1NoModuleAlarmEvent.setStatus(
        "current"
    )

extendedPsu2NoModuleAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4317)
)
extendedPsu2NoModuleAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu2NoModuleAlarmEvent.setStatus(
        "current"
    )

extendedPsu1VoltageMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4318)
)
extendedPsu1VoltageMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu1VoltageMissingAlarmEvent.setStatus(
        "current"
    )

extendedPsu2VoltageMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4319)
)
extendedPsu2VoltageMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu2VoltageMissingAlarmEvent.setStatus(
        "current"
    )

extendedPsu1VoltageLowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4320)
)
extendedPsu1VoltageLowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu1VoltageLowAlarmEvent.setStatus(
        "current"
    )

extendedPsu2VoltageLowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4321)
)
extendedPsu2VoltageLowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu2VoltageLowAlarmEvent.setStatus(
        "current"
    )

extendedPsu1FanFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4322)
)
extendedPsu1FanFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu1FanFailureAlarmEvent.setStatus(
        "current"
    )

extendedPsu2FanFailureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4323)
)
extendedPsu2FanFailureAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedPsu2FanFailureAlarmEvent.setStatus(
        "current"
    )

extendedBackupCableIsNotConnectedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4324)
)
extendedBackupCableIsNotConnectedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedBackupCableIsNotConnectedAlarmEvent.setStatus(
        "current"
    )

extendedUnableToAddMacAddressMappingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4325)
)
extendedUnableToAddMacAddressMappingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedUnableToAddMacAddressMappingAlarmEvent.setStatus(
        "current"
    )

extendedFpgaPllNotLockedAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4327)
)
extendedFpgaPllNotLockedAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFpgaPllNotLockedAlarmEvent.setStatus(
        "current"
    )

extendedFpgaRegisterMissmatchAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4328)
)
extendedFpgaRegisterMissmatchAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedFpgaRegisterMissmatchAlarmEvent.setStatus(
        "current"
    )

extendedDepiLicenseMissingAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4329)
)
extendedDepiLicenseMissingAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedDepiLicenseMissingAlarmEvent.setStatus(
        "current"
    )

extendedXfiPortOverflowAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4, 2, 2, 4330)
)
extendedXfiPortOverflowAlarmEvent.setObjects(
      *(("TELESTE-LUMINATO-MIB2", "severity"),
        ("TELESTE-LUMINATO-MIB2", "module"),
        ("TELESTE-LUMINATO-MIB2", "reason"),
        ("TELESTE-LUMINATO-MIB2", "description"),
        ("TELESTE-LUMINATO-MIB2", "paramTable"))
)
if mibBuilder.loadTexts:
    extendedXfiPortOverflowAlarmEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELESTE-LUMINATO-MIB2",
    **{"notifications": notifications,
       "params": params,
       "severity": severity,
       "module": module,
       "description": description,
       "reason": reason,
       "paramTable": paramTable,
       "paramEntry": paramEntry,
       "paramIdx": paramIdx,
       "paramValue": paramValue,
       "traps": traps,
       "generic": generic,
       "extendedAlarmEvent": extendedAlarmEvent,
       "specific": specific,
       "extendedPidMissingAlarmEvent": extendedPidMissingAlarmEvent,
       "extendedServiceMissingAlarmEvent": extendedServiceMissingAlarmEvent,
       "extendedPidConflictAlarmEvent": extendedPidConflictAlarmEvent,
       "extendedTemperatureTooHighAlarmEvent": extendedTemperatureTooHighAlarmEvent,
       "extendedTemperatureTooLowAlarmEvent": extendedTemperatureTooLowAlarmEvent,
       "extendedManualTableInsertionFailedAlarmEvent": extendedManualTableInsertionFailedAlarmEvent,
       "extendedAlertMessageAlarmEvent": extendedAlertMessageAlarmEvent,
       "extendedServicesPassthroughAlarmEvent": extendedServicesPassthroughAlarmEvent,
       "extendedEcmStreamCannotBeAttachedToIncompatibleCwgAlarmEvent": extendedEcmStreamCannotBeAttachedToIncompatibleCwgAlarmEvent,
       "extendedPsigTableInsertionFailedAlarmEvent": extendedPsigTableInsertionFailedAlarmEvent,
       "extendedPsiTableCaptureFailureAlarmEvent": extendedPsiTableCaptureFailureAlarmEvent,
       "extendedSignalMissingAlarmEvent": extendedSignalMissingAlarmEvent,
       "extendedNoTsSyncAlarmEvent": extendedNoTsSyncAlarmEvent,
       "extendedTsRxErrorsAlarmEvent": extendedTsRxErrorsAlarmEvent,
       "extendedTsInputBufferOverflowAlarmEvent": extendedTsInputBufferOverflowAlarmEvent,
       "extendedAsiLinkDownAlarmEvent": extendedAsiLinkDownAlarmEvent,
       "extendedForbiddenNetworkAlarmEvent": extendedForbiddenNetworkAlarmEvent,
       "extendedSidConflictAlarmEvent": extendedSidConflictAlarmEvent,
       "extendedLinkMissingAlarmEvent": extendedLinkMissingAlarmEvent,
       "extendedEcmMissingAlarmEvent": extendedEcmMissingAlarmEvent,
       "extendedScramblingConflictInSharedComponentAlarmEvent": extendedScramblingConflictInSharedComponentAlarmEvent,
       "extendedScrambledSharedComponentAlarmEvent": extendedScrambledSharedComponentAlarmEvent,
       "extendedUsedInputIsNotSptsAlarmEvent": extendedUsedInputIsNotSptsAlarmEvent,
       "extendedConfigurationErrorAlarmEvent": extendedConfigurationErrorAlarmEvent,
       "extendedDescramblingFailedAlarmEvent": extendedDescramblingFailedAlarmEvent,
       "extendedCwGroupConflictAlarmEvent": extendedCwGroupConflictAlarmEvent,
       "extendedInvalidSdtTemplateAlarmEvent": extendedInvalidSdtTemplateAlarmEvent,
       "extendedCannotDescrambleDueToCamRoutingAlarmEvent": extendedCannotDescrambleDueToCamRoutingAlarmEvent,
       "extendedRedundancyActivatedAlarmEvent": extendedRedundancyActivatedAlarmEvent,
       "extendedRtpInputPacketSequenceAnomaliesDetectedAlarmEvent": extendedRtpInputPacketSequenceAnomaliesDetectedAlarmEvent,
       "extendedRtpInputErrorsDroppedPacketsAlarmEvent": extendedRtpInputErrorsDroppedPacketsAlarmEvent,
       "extendedFecHasCorrectedPacketsAlarmEvent": extendedFecHasCorrectedPacketsAlarmEvent,
       "extendedFecInputAnomaliesDetectedAlarmEvent": extendedFecInputAnomaliesDetectedAlarmEvent,
       "extendedFecErrorCorrectionCapacityExceededAlarmEvent": extendedFecErrorCorrectionCapacityExceededAlarmEvent,
       "extendedTooManyServicesAlarmEvent": extendedTooManyServicesAlarmEvent,
       "extendedLowSignalLevelAlarmEvent": extendedLowSignalLevelAlarmEvent,
       "extendedSignalMutedAlarmEvent": extendedSignalMutedAlarmEvent,
       "extendedProidiomScramblingDisabledAlarmEvent": extendedProidiomScramblingDisabledAlarmEvent,
       "extendedVmxConnectionLostAlarmEvent": extendedVmxConnectionLostAlarmEvent,
       "extendedControlWordErrorAlarmEvent": extendedControlWordErrorAlarmEvent,
       "extendedOutputServiceCapacityExceededAlarmEvent": extendedOutputServiceCapacityExceededAlarmEvent,
       "extendedLowSignalQualityAlarmEvent": extendedLowSignalQualityAlarmEvent,
       "extendedModuleOffAlarmEvent": extendedModuleOffAlarmEvent,
       "extendedPidCapacityExceededAlarmEvent": extendedPidCapacityExceededAlarmEvent,
       "extendedPsiSiCaptureCapacityExceededAlarmEvent": extendedPsiSiCaptureCapacityExceededAlarmEvent,
       "extendedOutOfServiceIdsAlarmEvent": extendedOutOfServiceIdsAlarmEvent,
       "extendedCaModuleMissingAlarmEvent": extendedCaModuleMissingAlarmEvent,
       "extendedPsiSiInsertCapacityExceededAlarmEvent": extendedPsiSiInsertCapacityExceededAlarmEvent,
       "extendedMultiplexOversubscriptionPacketsDiscardedAlarmEvent": extendedMultiplexOversubscriptionPacketsDiscardedAlarmEvent,
       "extendedUnknownModuleAlarmEvent": extendedUnknownModuleAlarmEvent,
       "extendedMainVoltageTooHighAlarmEvent": extendedMainVoltageTooHighAlarmEvent,
       "extendedMainVoltageTooLowAlarmEvent": extendedMainVoltageTooLowAlarmEvent,
       "extendedCurrentTooHighAlarmEvent": extendedCurrentTooHighAlarmEvent,
       "extendedCurrentTooLowAlarmEvent": extendedCurrentTooLowAlarmEvent,
       "extendedDaemonInitializationFailedAlarmEvent": extendedDaemonInitializationFailedAlarmEvent,
       "extendedDeviceDriverFailureAlarmEvent": extendedDeviceDriverFailureAlarmEvent,
       "extendedHardwareFailureAlarmEvent": extendedHardwareFailureAlarmEvent,
       "extendedFanFailureAlarmEvent": extendedFanFailureAlarmEvent,
       "extendedRunningOnBackupPowerAlarmEvent": extendedRunningOnBackupPowerAlarmEvent,
       "extendedPowerSupplyOverloadedAlarmEvent": extendedPowerSupplyOverloadedAlarmEvent,
       "extendedBootingUpAlarmEvent": extendedBootingUpAlarmEvent,
       "extendedBootFailedRetryingAlarmEvent": extendedBootFailedRetryingAlarmEvent,
       "extendedBootFailedAlarmEvent": extendedBootFailedAlarmEvent,
       "extendedShuttingDownAlarmEvent": extendedShuttingDownAlarmEvent,
       "extendedConnectionLostAlarmEvent": extendedConnectionLostAlarmEvent,
       "extendedIncompatibleModuleDisabledAlarmEvent": extendedIncompatibleModuleDisabledAlarmEvent,
       "extendedFailedToBootAlarmEvent": extendedFailedToBootAlarmEvent,
       "extendedUpcTooLowInputPowerAlarmEvent": extendedUpcTooLowInputPowerAlarmEvent,
       "extendedUpcTooHighInputPowerAlarmEvent": extendedUpcTooHighInputPowerAlarmEvent,
       "extendedCalibrationDataMissingAlarmEvent": extendedCalibrationDataMissingAlarmEvent,
       "extendedCalibrationCheckSkippedAlarmEvent": extendedCalibrationCheckSkippedAlarmEvent,
       "extendedDescramblingFailureAlarmEvent": extendedDescramblingFailureAlarmEvent,
       "extendedBackupSwitchedOverToBackupDeviceAlarmEvent": extendedBackupSwitchedOverToBackupDeviceAlarmEvent,
       "extendedFailedToQuerySomeOfTheNitDataAlarmEvent": extendedFailedToQuerySomeOfTheNitDataAlarmEvent,
       "extendedNitWizardFailureAlarmEvent": extendedNitWizardFailureAlarmEvent,
       "extendedDuplicateFrequencyInTwoOrMoreSelectedQamOutputsAlarmEvent": extendedDuplicateFrequencyInTwoOrMoreSelectedQamOutputsAlarmEvent,
       "extendedCannotResolveTableVersionUsingDefaultAlarmEvent": extendedCannotResolveTableVersionUsingDefaultAlarmEvent,
       "extendedUnsupportedConfigurationAlarmEvent": extendedUnsupportedConfigurationAlarmEvent,
       "extendedFrequencyOutOfRangeAlarmEvent": extendedFrequencyOutOfRangeAlarmEvent,
       "extendedOutputPowerOutOfRangeAlarmEvent": extendedOutputPowerOutOfRangeAlarmEvent,
       "extendedSymbolrateOutOfRangeAlarmEvent": extendedSymbolrateOutOfRangeAlarmEvent,
       "extendedChannelDistanceTooNarrowAlarmEvent": extendedChannelDistanceTooNarrowAlarmEvent,
       "extendedInvalidLnbVoltageConfigurationAlarmEvent": extendedInvalidLnbVoltageConfigurationAlarmEvent,
       "extendedInvalidFecRateForSelectedModulationAlarmEvent": extendedInvalidFecRateForSelectedModulationAlarmEvent,
       "extendedLnbCurrentAlarmEvent": extendedLnbCurrentAlarmEvent,
       "extendedFrequencyOffsetAlarmEvent": extendedFrequencyOffsetAlarmEvent,
       "extendedRestartingDescramblingAlarmEvent": extendedRestartingDescramblingAlarmEvent,
       "extendedRebootingCamAlarmEvent": extendedRebootingCamAlarmEvent,
       "extendedEcmgFailureAlarmEvent": extendedEcmgFailureAlarmEvent,
       "extendedEcmStreamFailureAlarmEvent": extendedEcmStreamFailureAlarmEvent,
       "extendedEmmFailureAlarmEvent": extendedEmmFailureAlarmEvent,
       "extendedEmmStreamFailureAlarmEvent": extendedEmmStreamFailureAlarmEvent,
       "extendedEcmgNotConnectedAlarmEvent": extendedEcmgNotConnectedAlarmEvent,
       "extendedEmmNotConnectedAlarmEvent": extendedEmmNotConnectedAlarmEvent,
       "extendedScsNotLicensedAlarmEvent": extendedScsNotLicensedAlarmEvent,
       "extendedEcmgSwitchedToSpareServerAlarmEvent": extendedEcmgSwitchedToSpareServerAlarmEvent,
       "extendedUpdatedBootLoaderAvailableAlarmEvent": extendedUpdatedBootLoaderAvailableAlarmEvent,
       "extendedUpdatingStage1BootLoaderAlarmEvent": extendedUpdatingStage1BootLoaderAlarmEvent,
       "extendedUpdatingStage2BootLoaderAlarmEvent": extendedUpdatingStage2BootLoaderAlarmEvent,
       "extendedFailedToUpdateStage1BootLoaderAlarmEvent": extendedFailedToUpdateStage1BootLoaderAlarmEvent,
       "extendedFailedToUpdateStage2BootLoaderAlarmEvent": extendedFailedToUpdateStage2BootLoaderAlarmEvent,
       "extendedBackupActiveBackupAlarmEvent": extendedBackupActiveBackupAlarmEvent,
       "extendedConfiguringModuleAlarmEvent": extendedConfiguringModuleAlarmEvent,
       "extendedNoModuleAlarmEvent": extendedNoModuleAlarmEvent,
       "extendedProcessStartedAlarmEvent": extendedProcessStartedAlarmEvent,
       "extendedBackupLicenseMissingAlarmEvent": extendedBackupLicenseMissingAlarmEvent,
       "extendedMultiplexingLicenseMissingAlarmEvent": extendedMultiplexingLicenseMissingAlarmEvent,
       "extendedDemultiplexingLicenseMissingAlarmEvent": extendedDemultiplexingLicenseMissingAlarmEvent,
       "extendedDvbProcessingLicenseMissingAlarmEvent": extendedDvbProcessingLicenseMissingAlarmEvent,
       "extendedMsdLicenseMissingAlarmEvent": extendedMsdLicenseMissingAlarmEvent,
       "extendedDvbS2LicenseMissingAlarmEvent": extendedDvbS2LicenseMissingAlarmEvent,
       "extendedScramblingLicenseMissingAlarmEvent": extendedScramblingLicenseMissingAlarmEvent,
       "extendedScsLicenseMissingAlarmEvent": extendedScsLicenseMissingAlarmEvent,
       "extendedUserFromGroupAdminIsUsingCliAlarmEvent": extendedUserFromGroupAdminIsUsingCliAlarmEvent,
       "extendedUserFromGroupInstallIsUsingCliAlarmEvent": extendedUserFromGroupInstallIsUsingCliAlarmEvent,
       "extendedUserFromGroupOperIsUsingCliAlarmEvent": extendedUserFromGroupOperIsUsingCliAlarmEvent,
       "extendedUserFromGroupMonitorIsUsingCliAlarmEvent": extendedUserFromGroupMonitorIsUsingCliAlarmEvent,
       "extendedExtIoSignaledAlarmEvent": extendedExtIoSignaledAlarmEvent,
       "extendedExtIoBackupPowerSupplyFailureAlarmEvent": extendedExtIoBackupPowerSupplyFailureAlarmEvent,
       "extendedExtIoIntrusionDetectedAlarmEvent": extendedExtIoIntrusionDetectedAlarmEvent,
       "extendedRedundancyFailedAlarmEvent": extendedRedundancyFailedAlarmEvent,
       "extendedMultiplexOversubscriptionPacketsDelayedAlarmEvent": extendedMultiplexOversubscriptionPacketsDelayedAlarmEvent,
       "extendedCbrOutputOversubscriptionAlarmEvent": extendedCbrOutputOversubscriptionAlarmEvent,
       "extendedBackupHwDoesNotSupportSelectedDeviceRoleAlarmEvent": extendedBackupHwDoesNotSupportSelectedDeviceRoleAlarmEvent,
       "extendedSoftwareUpdateInProgressAlarmEvent": extendedSoftwareUpdateInProgressAlarmEvent,
       "extendedSoftwareUpdateReadyWaitingForRebootToCompleteAlarmEvent": extendedSoftwareUpdateReadyWaitingForRebootToCompleteAlarmEvent,
       "extendedSoftwareUpdateFailedAlarmEvent": extendedSoftwareUpdateFailedAlarmEvent,
       "extendedBackupModuleHwDoesNotSupportSelectedOnePlusOneBackupRoleAlarmEvent": extendedBackupModuleHwDoesNotSupportSelectedOnePlusOneBackupRoleAlarmEvent,
       "extendedEitProcessingLicenseMissingAlarmEvent": extendedEitProcessingLicenseMissingAlarmEvent,
       "extendedCbrOutputOversubscriptionPacketsDiscardedAlarmEvent": extendedCbrOutputOversubscriptionPacketsDiscardedAlarmEvent,
       "extendedIpInputCapacityExceededAlarmEvent": extendedIpInputCapacityExceededAlarmEvent,
       "extendedEitReinsertCapacityExceededAlarmEvent": extendedEitReinsertCapacityExceededAlarmEvent,
       "extendedDvbTimeMissingAlarmEvent": extendedDvbTimeMissingAlarmEvent,
       "extendedDvbT2LicenseMissingAlarmEvent": extendedDvbT2LicenseMissingAlarmEvent,
       "extendedDcFeedCurrentAlarmEvent": extendedDcFeedCurrentAlarmEvent,
       "extendedNotGeneratingTdtTotTableWaitingForCorrectSystemTimeAlarmEvent": extendedNotGeneratingTdtTotTableWaitingForCorrectSystemTimeAlarmEvent,
       "extendedDataPlpIdSelectionRequiredAlarmEvent": extendedDataPlpIdSelectionRequiredAlarmEvent,
       "extendedDataPlpIdSelectionNotValidAlarmEvent": extendedDataPlpIdSelectionNotValidAlarmEvent,
       "extendedHierarchyHpSelectedForNonAlarmEvent": extendedHierarchyHpSelectedForNonAlarmEvent,
       "extendedBackupVoltageTooHighAlarmEvent": extendedBackupVoltageTooHighAlarmEvent,
       "extendedBackupVoltageTooLowAlarmEvent": extendedBackupVoltageTooLowAlarmEvent,
       "extendedCamFailureActionTakenRestartingDescramblingAlarmEvent": extendedCamFailureActionTakenRestartingDescramblingAlarmEvent,
       "extendedCamFailureActionTakenRebootingCaModuleAlarmEvent": extendedCamFailureActionTakenRebootingCaModuleAlarmEvent,
       "extendedCaMenuIsOpenAlarmEvent": extendedCaMenuIsOpenAlarmEvent,
       "extendedNitSidConflictAlarmEvent": extendedNitSidConflictAlarmEvent,
       "extendedNotGeneratingSttTableWaitingForCorrectSystemTimeAlarmEvent": extendedNotGeneratingSttTableWaitingForCorrectSystemTimeAlarmEvent,
       "extendedNumberOfFecLicensesExceededAlarmEvent": extendedNumberOfFecLicensesExceededAlarmEvent,
       "extendedErrorCorrectionOverloadTooManySimultaneousMissingPacketsAlarmEvent": extendedErrorCorrectionOverloadTooManySimultaneousMissingPacketsAlarmEvent,
       "extendedFecPacketsDiscardedModuleBitrateTooHighAlarmEvent": extendedFecPacketsDiscardedModuleBitrateTooHighAlarmEvent,
       "extendedMediaPacketsDiscardedModuleBitrateTooHighAlarmEvent": extendedMediaPacketsDiscardedModuleBitrateTooHighAlarmEvent,
       "extendedSfpLinkDownAlarmEvent": extendedSfpLinkDownAlarmEvent,
       "extendedBackupsyncTurnedOffAlarmEvent": extendedBackupsyncTurnedOffAlarmEvent,
       "extendedBackupsyncManualModeAlarmEvent": extendedBackupsyncManualModeAlarmEvent,
       "extendedBackupsyncAutomaticModeAlarmEvent": extendedBackupsyncAutomaticModeAlarmEvent,
       "extendedBackupsyncConfigurationWillBeSynchronizedAutomaticallyAlarmEvent": extendedBackupsyncConfigurationWillBeSynchronizedAutomaticallyAlarmEvent,
       "extendedBackupsyncSynchronizingAlarmEvent": extendedBackupsyncSynchronizingAlarmEvent,
       "extendedBackupsyncSwCompatibilityCheckAlarmEvent": extendedBackupsyncSwCompatibilityCheckAlarmEvent,
       "extendedBackupsyncHwCompatibilityCheckAlarmEvent": extendedBackupsyncHwCompatibilityCheckAlarmEvent,
       "extendedBackupsyncConfigurationFaultAlarmEvent": extendedBackupsyncConfigurationFaultAlarmEvent,
       "extendedBackupsyncConnectionLostAlarmEvent": extendedBackupsyncConnectionLostAlarmEvent,
       "extendedBackupsyncAutosyncNotPossibleFromBackupToMainAlarmEvent": extendedBackupsyncAutosyncNotPossibleFromBackupToMainAlarmEvent,
       "extendedBackupsyncRebootingPairDeviceToNewConfigurationAlarmEvent": extendedBackupsyncRebootingPairDeviceToNewConfigurationAlarmEvent,
       "extendedBackupsyncCheckLicenseCompatibilityAlarmEvent": extendedBackupsyncCheckLicenseCompatibilityAlarmEvent,
       "extendedBackupsyncLicenseCompatibilityCheckAlarmEvent": extendedBackupsyncLicenseCompatibilityCheckAlarmEvent,
       "extendedDeviceFirstBootActionsAreInProgressAlarmEvent": extendedDeviceFirstBootActionsAreInProgressAlarmEvent,
       "extendedDeviceConfigurationBackupInProgressAlarmEvent": extendedDeviceConfigurationBackupInProgressAlarmEvent,
       "extendedDeviceConfigurationRestoreInProgressAlarmEvent": extendedDeviceConfigurationRestoreInProgressAlarmEvent,
       "extendedDeviceOtherSoftwareActivationAlarmEvent": extendedDeviceOtherSoftwareActivationAlarmEvent,
       "extendedTooManyOutputPidsConfiguredAlarmEvent": extendedTooManyOutputPidsConfiguredAlarmEvent,
       "extendedRebootRequestByUserAlarmEvent": extendedRebootRequestByUserAlarmEvent,
       "extendedRemovedFromTheChassisAlarmEvent": extendedRemovedFromTheChassisAlarmEvent,
       "extendedInsertedIntoTheChassisAlarmEvent": extendedInsertedIntoTheChassisAlarmEvent,
       "extendedPacketsDiscardedInIpMirrorOutputsAlarmEvent": extendedPacketsDiscardedInIpMirrorOutputsAlarmEvent,
       "extendedAesLicenseMissingAlarmEvent": extendedAesLicenseMissingAlarmEvent,
       "extendedSymbolRateTooHighForSelectedModulationSelectHighSpeedModulationModeToAvoidErrorsAlarmEvent": extendedSymbolRateTooHighForSelectedModulationSelectHighSpeedModulationModeToAvoidErrorsAlarmEvent,
       "extendedEcmResponsesDelayedAlarmEvent": extendedEcmResponsesDelayedAlarmEvent,
       "extendedDisconnectedHostInMultichassisGroupAlarmEvent": extendedDisconnectedHostInMultichassisGroupAlarmEvent,
       "extendedMultichassisConfigurationFailureAlarmEvent": extendedMultichassisConfigurationFailureAlarmEvent,
       "extendedSwVersionDifferenceWithinMultichassisGroupAlarmEvent": extendedSwVersionDifferenceWithinMultichassisGroupAlarmEvent,
       "extendedSwVersionMismatchAlarmEvent": extendedSwVersionMismatchAlarmEvent,
       "extendedEmergencySignalActivatedAlarmEvent": extendedEmergencySignalActivatedAlarmEvent,
       "extendedEmergencySignalMissingAlarmEvent": extendedEmergencySignalMissingAlarmEvent,
       "extendedUnableToAddEmergencySignalAlarmEvent": extendedUnableToAddEmergencySignalAlarmEvent,
       "extendedNetworkInformationTableNeedsToBeUpdatedAlarmEvent": extendedNetworkInformationTableNeedsToBeUpdatedAlarmEvent,
       "extendedNfsMountFailureAlarmEvent": extendedNfsMountFailureAlarmEvent,
       "extendedEthernetInputBufferOverflowAlarmEvent": extendedEthernetInputBufferOverflowAlarmEvent,
       "extendedDvbAlarmEvent": extendedDvbAlarmEvent,
       "extendedPoweredOffAlarmEvent": extendedPoweredOffAlarmEvent,
       "extendedPsu1NoModuleAlarmEvent": extendedPsu1NoModuleAlarmEvent,
       "extendedPsu2NoModuleAlarmEvent": extendedPsu2NoModuleAlarmEvent,
       "extendedPsu1VoltageMissingAlarmEvent": extendedPsu1VoltageMissingAlarmEvent,
       "extendedPsu2VoltageMissingAlarmEvent": extendedPsu2VoltageMissingAlarmEvent,
       "extendedPsu1VoltageLowAlarmEvent": extendedPsu1VoltageLowAlarmEvent,
       "extendedPsu2VoltageLowAlarmEvent": extendedPsu2VoltageLowAlarmEvent,
       "extendedPsu1FanFailureAlarmEvent": extendedPsu1FanFailureAlarmEvent,
       "extendedPsu2FanFailureAlarmEvent": extendedPsu2FanFailureAlarmEvent,
       "extendedBackupCableIsNotConnectedAlarmEvent": extendedBackupCableIsNotConnectedAlarmEvent,
       "extendedUnableToAddMacAddressMappingAlarmEvent": extendedUnableToAddMacAddressMappingAlarmEvent,
       "extendedFpgaPllNotLockedAlarmEvent": extendedFpgaPllNotLockedAlarmEvent,
       "extendedFpgaRegisterMissmatchAlarmEvent": extendedFpgaRegisterMissmatchAlarmEvent,
       "extendedDepiLicenseMissingAlarmEvent": extendedDepiLicenseMissingAlarmEvent,
       "extendedXfiPortOverflowAlarmEvent": extendedXfiPortOverflowAlarmEvent}
)
