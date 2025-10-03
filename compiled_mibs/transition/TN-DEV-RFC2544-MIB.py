# SNMP MIB module (TN-DEV-RFC2544-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-RFC2544-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:56 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY

tnDevRFC2544 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42)
)
if mibBuilder.loadTexts:
    tnDevRFC2544.setRevisions(
        ("2014-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevRFC2544ProfileTable_Object = MibTable
tnDevRFC2544ProfileTable = _TnDevRFC2544ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 1)
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileTable.setStatus("current")
_TnDevRFC2544ProfileEntry_Object = MibTableRow
tnDevRFC2544ProfileEntry = _TnDevRFC2544ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 1, 1)
)
tnDevRFC2544ProfileEntry.setIndexNames(
    (0, "TN-DEV-RFC2544-MIB", "tnDevRFC2544ProfileIndex"),
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileEntry.setStatus("current")


class _TnDevRFC2544ProfileIndex_Type(Integer32):
    """Custom type tnDevRFC2544ProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnDevRFC2544ProfileIndex_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileIndex_Object = MibTableColumn
tnDevRFC2544ProfileIndex = _TnDevRFC2544ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 1, 1, 1),
    _TnDevRFC2544ProfileIndex_Type()
)
tnDevRFC2544ProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileIndex.setStatus("current")


class _TnDevRFC2544ProfileName_Type(DisplayString):
    """Custom type tnDevRFC2544ProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnDevRFC2544ProfileName_Type.__name__ = "DisplayString"
_TnDevRFC2544ProfileName_Object = MibTableColumn
tnDevRFC2544ProfileName = _TnDevRFC2544ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 1, 1, 2),
    _TnDevRFC2544ProfileName_Type()
)
tnDevRFC2544ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileName.setStatus("current")
_TnDevRFC2544ProfileConfigurationCommonParametersTable_Object = MibTable
tnDevRFC2544ProfileConfigurationCommonParametersTable = _TnDevRFC2544ProfileConfigurationCommonParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2)
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersTable.setStatus("current")
_TnDevRFC2544ProfileConfigurationCommonParametersEntry_Object = MibTableRow
tnDevRFC2544ProfileConfigurationCommonParametersEntry = _TnDevRFC2544ProfileConfigurationCommonParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1)
)
tnDevRFC2544ProfileConfigurationCommonParametersEntry.setIndexNames(
    (0, "TN-DEV-RFC2544-MIB", "tnDevRFC2544ProfileConfigurationCommonParametersIndex"),
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersEntry.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersIndex_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersIndex_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersIndex_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersIndex = _TnDevRFC2544ProfileConfigurationCommonParametersIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 1),
    _TnDevRFC2544ProfileConfigurationCommonParametersIndex_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersIndex.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersDescription_Type(DisplayString):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersDescription_Type.__name__ = "DisplayString"
_TnDevRFC2544ProfileConfigurationCommonParametersDescription_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersDescription = _TnDevRFC2544ProfileConfigurationCommonParametersDescription_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 2),
    _TnDevRFC2544ProfileConfigurationCommonParametersDescription_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersDescription.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersMEGLevel_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersMEGLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersMEGLevel_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersMEGLevel_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersMEGLevel = _TnDevRFC2544ProfileConfigurationCommonParametersMEGLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 3),
    _TnDevRFC2544ProfileConfigurationCommonParametersMEGLevel_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersMEGLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersMEGLevel.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersEgressPort_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersEgressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersEgressPort_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersEgressPort_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersEgressPort = _TnDevRFC2544ProfileConfigurationCommonParametersEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 4),
    _TnDevRFC2544ProfileConfigurationCommonParametersEgressPort_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersEgressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersEgressPort.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck = _TnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 5),
    _TnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersDwellTime_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersDwellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersDwellTime_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersDwellTime_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersDwellTime = _TnDevRFC2544ProfileConfigurationCommonParametersDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 6),
    _TnDevRFC2544ProfileConfigurationCommonParametersDwellTime_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersDwellTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersDwellTime.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersType_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("portDownMEP", 0),
          ("vlanBasedDownMEP", 1))
    )


_TnDevRFC2544ProfileConfigurationCommonParametersType_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersType_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersType = _TnDevRFC2544ProfileConfigurationCommonParametersType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 7),
    _TnDevRFC2544ProfileConfigurationCommonParametersType_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersType.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersVLANID_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersVLANID_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersVLANID_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersVLANID = _TnDevRFC2544ProfileConfigurationCommonParametersVLANID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 8),
    _TnDevRFC2544ProfileConfigurationCommonParametersVLANID_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersVLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersVLANID.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersPCP_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersPCP_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersPCP_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersPCP = _TnDevRFC2544ProfileConfigurationCommonParametersPCP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 9),
    _TnDevRFC2544ProfileConfigurationCommonParametersPCP_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersPCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersPCP.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersDEI_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersDEI_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersDEI_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersDEI = _TnDevRFC2544ProfileConfigurationCommonParametersDEI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 10),
    _TnDevRFC2544ProfileConfigurationCommonParametersDEI_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersDEI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersDEI.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersDMAC_Type(DisplayString):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersDMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersDMAC_Type.__name__ = "DisplayString"
_TnDevRFC2544ProfileConfigurationCommonParametersDMAC_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersDMAC = _TnDevRFC2544ProfileConfigurationCommonParametersDMAC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 11),
    _TnDevRFC2544ProfileConfigurationCommonParametersDMAC_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersDMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersDMAC.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask = _TnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 12),
    _TnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask.setStatus("current")


class _TnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask = _TnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 2, 1, 13),
    _TnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask_Type()
)
tnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask.setStatus("current")
_TnDevRFC2544ProfileConfigurationThroughputTestParametersTable_Object = MibTable
tnDevRFC2544ProfileConfigurationThroughputTestParametersTable = _TnDevRFC2544ProfileConfigurationThroughputTestParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3)
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersTable.setStatus("current")
_TnDevRFC2544ProfileConfigurationThroughputTestParametersEntry_Object = MibTableRow
tnDevRFC2544ProfileConfigurationThroughputTestParametersEntry = _TnDevRFC2544ProfileConfigurationThroughputTestParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3, 1)
)
tnDevRFC2544ProfileConfigurationThroughputTestParametersEntry.setIndexNames(
    (0, "TN-DEV-RFC2544-MIB", "tnDevRFC2544ProfileConfigurationThroughputTestParametersIndex"),
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersEntry.setStatus("current")


class _TnDevRFC2544ProfileConfigurationThroughputTestParametersIndex_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationThroughputTestParametersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnDevRFC2544ProfileConfigurationThroughputTestParametersIndex_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationThroughputTestParametersIndex_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationThroughputTestParametersIndex = _TnDevRFC2544ProfileConfigurationThroughputTestParametersIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3, 1, 1),
    _TnDevRFC2544ProfileConfigurationThroughputTestParametersIndex_Type()
)
tnDevRFC2544ProfileConfigurationThroughputTestParametersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersIndex.setStatus("current")


class _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration = _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3, 1, 2),
    _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration_Type()
)
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration.setStatus("current")


class _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate_Object = MibScalar
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate = _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3, 1, 3),
    _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate_Type()
)
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate.setStatus("current")


class _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate_Object = MibScalar
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate = _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3, 1, 4),
    _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate_Type()
)
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate.setStatus("current")


class _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy_Object = MibScalar
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy = _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3, 1, 5),
    _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy_Type()
)
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy.setStatus("current")


class _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss_Object = MibScalar
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss = _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 3, 1, 6),
    _TnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss_Type()
)
tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss.setStatus("current")
_TnDevRFC2544ProfileConfigurationLatencyTestParametersTable_Object = MibTable
tnDevRFC2544ProfileConfigurationLatencyTestParametersTable = _TnDevRFC2544ProfileConfigurationLatencyTestParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4)
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationLatencyTestParametersTable.setStatus("current")
_TnDevRFC2544ProfileConfigurationFrameLossTestParametersTable_Object = MibTable
tnDevRFC2544ProfileConfigurationFrameLossTestParametersTable = _TnDevRFC2544ProfileConfigurationFrameLossTestParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4)
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationFrameLossTestParametersTable.setStatus("current")
_TnDevRFC2544ProfileConfigurationLatencyTestParametersEntry_Object = MibTableRow
tnDevRFC2544ProfileConfigurationLatencyTestParametersEntry = _TnDevRFC2544ProfileConfigurationLatencyTestParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1)
)
tnDevRFC2544ProfileConfigurationLatencyTestParametersEntry.setIndexNames(
    (0, "TN-DEV-RFC2544-MIB", "tnDevRFC2544ProfileConfigurationLatencyTestParametersIndex"),
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationLatencyTestParametersEntry.setStatus("current")
_TnDevRFC2544ProfileConfigurationFrameLossTestParametersEntry_Object = MibTableRow
tnDevRFC2544ProfileConfigurationFrameLossTestParametersEntry = _TnDevRFC2544ProfileConfigurationFrameLossTestParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1)
)
tnDevRFC2544ProfileConfigurationFrameLossTestParametersEntry.setIndexNames(
    (0, "TN-DEV-RFC2544-MIB", "tnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex"),
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationFrameLossTestParametersEntry.setStatus("current")


class _TnDevRFC2544ProfileConfigurationLatencyTestParametersIndex_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationLatencyTestParametersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnDevRFC2544ProfileConfigurationLatencyTestParametersIndex_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationLatencyTestParametersIndex_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationLatencyTestParametersIndex = _TnDevRFC2544ProfileConfigurationLatencyTestParametersIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 1),
    _TnDevRFC2544ProfileConfigurationLatencyTestParametersIndex_Type()
)
tnDevRFC2544ProfileConfigurationLatencyTestParametersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationLatencyTestParametersIndex.setStatus("current")


class _TnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex = _TnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 1),
    _TnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex_Type()
)
tnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex.setStatus("current")


class _TnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_TnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration = _TnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 2),
    _TnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration_Type()
)
tnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration.setStatus("current")


class _TnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration = _TnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 2),
    _TnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration_Type()
)
tnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration.setStatus("current")


class _TnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval = _TnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 3),
    _TnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval_Type()
)
tnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval.setStatus("current")


class _TnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate = _TnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 3),
    _TnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate_Type()
)
tnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate.setStatus("current")


class _TnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss = _TnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 4),
    _TnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss_Type()
)
tnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss.setStatus("current")


class _TnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate = _TnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 4),
    _TnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate_Type()
)
tnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate.setStatus("current")


class _TnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep = _TnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 4, 1, 5),
    _TnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep_Type()
)
tnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep.setStatus("current")
_TnDevRFC2544ProfileConfigurationBackToBackTestParametersTable_Object = MibTable
tnDevRFC2544ProfileConfigurationBackToBackTestParametersTable = _TnDevRFC2544ProfileConfigurationBackToBackTestParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 5)
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationBackToBackTestParametersTable.setStatus("current")
_TnDevRFC2544ProfileConfigurationBackToBackTestParametersEntry_Object = MibTableRow
tnDevRFC2544ProfileConfigurationBackToBackTestParametersEntry = _TnDevRFC2544ProfileConfigurationBackToBackTestParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 5, 1)
)
tnDevRFC2544ProfileConfigurationBackToBackTestParametersEntry.setIndexNames(
    (0, "TN-DEV-RFC2544-MIB", "tnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex"),
)
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationBackToBackTestParametersEntry.setStatus("current")


class _TnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex = _TnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 5, 1, 1),
    _TnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex_Type()
)
tnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex.setStatus("current")


class _TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration = _TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 5, 1, 2),
    _TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration_Type()
)
tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration.setStatus("current")


class _TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount_Type(Integer32):
    """Custom type tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount_Type.__name__ = "Integer32"
_TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount_Object = MibTableColumn
tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount = _TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 42, 5, 1, 3),
    _TnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount_Type()
)
tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-RFC2544-MIB",
    **{"tnDevRFC2544": tnDevRFC2544,
       "tnDevRFC2544ProfileTable": tnDevRFC2544ProfileTable,
       "tnDevRFC2544ProfileEntry": tnDevRFC2544ProfileEntry,
       "tnDevRFC2544ProfileIndex": tnDevRFC2544ProfileIndex,
       "tnDevRFC2544ProfileName": tnDevRFC2544ProfileName,
       "tnDevRFC2544ProfileConfigurationCommonParametersTable": tnDevRFC2544ProfileConfigurationCommonParametersTable,
       "tnDevRFC2544ProfileConfigurationCommonParametersEntry": tnDevRFC2544ProfileConfigurationCommonParametersEntry,
       "tnDevRFC2544ProfileConfigurationCommonParametersIndex": tnDevRFC2544ProfileConfigurationCommonParametersIndex,
       "tnDevRFC2544ProfileConfigurationCommonParametersDescription": tnDevRFC2544ProfileConfigurationCommonParametersDescription,
       "tnDevRFC2544ProfileConfigurationCommonParametersMEGLevel": tnDevRFC2544ProfileConfigurationCommonParametersMEGLevel,
       "tnDevRFC2544ProfileConfigurationCommonParametersEgressPort": tnDevRFC2544ProfileConfigurationCommonParametersEgressPort,
       "tnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck": tnDevRFC2544ProfileConfigurationCommonParametersSequenceNumberCheck,
       "tnDevRFC2544ProfileConfigurationCommonParametersDwellTime": tnDevRFC2544ProfileConfigurationCommonParametersDwellTime,
       "tnDevRFC2544ProfileConfigurationCommonParametersType": tnDevRFC2544ProfileConfigurationCommonParametersType,
       "tnDevRFC2544ProfileConfigurationCommonParametersVLANID": tnDevRFC2544ProfileConfigurationCommonParametersVLANID,
       "tnDevRFC2544ProfileConfigurationCommonParametersPCP": tnDevRFC2544ProfileConfigurationCommonParametersPCP,
       "tnDevRFC2544ProfileConfigurationCommonParametersDEI": tnDevRFC2544ProfileConfigurationCommonParametersDEI,
       "tnDevRFC2544ProfileConfigurationCommonParametersDMAC": tnDevRFC2544ProfileConfigurationCommonParametersDMAC,
       "tnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask": tnDevRFC2544ProfileConfigurationCommonParametersFrameSizeMask,
       "tnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask": tnDevRFC2544ProfileConfigurationCommonParametersTestsToRunMask,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersTable": tnDevRFC2544ProfileConfigurationThroughputTestParametersTable,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersEntry": tnDevRFC2544ProfileConfigurationThroughputTestParametersEntry,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersIndex": tnDevRFC2544ProfileConfigurationThroughputTestParametersIndex,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration": tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialDuration,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate": tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMinimumRate,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate": tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialMaximumRate,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy": tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAccuracy,
       "tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss": tnDevRFC2544ProfileConfigurationThroughputTestParametersTrialAllowedFrameLoss,
       "tnDevRFC2544ProfileConfigurationLatencyTestParametersTable": tnDevRFC2544ProfileConfigurationLatencyTestParametersTable,
       "tnDevRFC2544ProfileConfigurationFrameLossTestParametersTable": tnDevRFC2544ProfileConfigurationFrameLossTestParametersTable,
       "tnDevRFC2544ProfileConfigurationLatencyTestParametersEntry": tnDevRFC2544ProfileConfigurationLatencyTestParametersEntry,
       "tnDevRFC2544ProfileConfigurationFrameLossTestParametersEntry": tnDevRFC2544ProfileConfigurationFrameLossTestParametersEntry,
       "tnDevRFC2544ProfileConfigurationLatencyTestParametersIndex": tnDevRFC2544ProfileConfigurationLatencyTestParametersIndex,
       "tnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex": tnDevRFC2544ProfileConfigurationFrameLossTestParametersIndex,
       "tnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration": tnDevRFC2544ProfileConfigurationLatencyTestParametersTrialDuration,
       "tnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration": tnDevRFC2544ProfileConfigurationFrameLossTestParametersTrialDuration,
       "tnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval": tnDevRFC2544ProfileConfigurationLatencyTestParametersDelayMeasurementInterval,
       "tnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate": tnDevRFC2544ProfileConfigurationFrameLossTestParametersMinimumRate,
       "tnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss": tnDevRFC2544ProfileConfigurationLatencyTestParametersAllowedFrameLoss,
       "tnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate": tnDevRFC2544ProfileConfigurationFrameLossTestParametersMaximumRate,
       "tnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep": tnDevRFC2544ProfileConfigurationFrameLossTestParametersRateStep,
       "tnDevRFC2544ProfileConfigurationBackToBackTestParametersTable": tnDevRFC2544ProfileConfigurationBackToBackTestParametersTable,
       "tnDevRFC2544ProfileConfigurationBackToBackTestParametersEntry": tnDevRFC2544ProfileConfigurationBackToBackTestParametersEntry,
       "tnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex": tnDevRFC2544ProfileConfigurationBackToBackTestParametersIndex,
       "tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration": tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialDuration,
       "tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount": tnDevRFC2544ProfileConfigurationBackToBackTestParametersTrialCount}
)
