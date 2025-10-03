# SNMP MIB module (SIAE-FEATUREKEYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-FEATUREKEYS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:54 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

featureKeys = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101)
)
if mibBuilder.loadTexts:
    featureKeys.setRevisions(
        ("2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _FeatureKeysMibVersion_Type(Integer32):
    """Custom type featureKeysMibVersion based on Integer32"""
    defaultValue = 1


_FeatureKeysMibVersion_Type.__name__ = "Integer32"
_FeatureKeysMibVersion_Object = MibScalar
featureKeysMibVersion = _FeatureKeysMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 1),
    _FeatureKeysMibVersion_Type()
)
featureKeysMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureKeysMibVersion.setStatus("current")
_FeatureKeysRadioMap_Type = OctetString
_FeatureKeysRadioMap_Object = MibScalar
featureKeysRadioMap = _FeatureKeysRadioMap_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 2),
    _FeatureKeysRadioMap_Type()
)
featureKeysRadioMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureKeysRadioMap.setStatus("current")
_FeatureKeysLineMap_Type = OctetString
_FeatureKeysLineMap_Object = MibScalar
featureKeysLineMap = _FeatureKeysLineMap_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 3),
    _FeatureKeysLineMap_Type()
)
featureKeysLineMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureKeysLineMap.setStatus("current")


class _FeatureKeysActionRequest_Type(Integer32):
    """Custom type featureKeysActionRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("upload", 2))
    )


_FeatureKeysActionRequest_Type.__name__ = "Integer32"
_FeatureKeysActionRequest_Object = MibScalar
featureKeysActionRequest = _FeatureKeysActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 4),
    _FeatureKeysActionRequest_Type()
)
featureKeysActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureKeysActionRequest.setStatus("current")


class _FeatureKeysCertificateName_Type(DisplayString):
    """Custom type featureKeysCertificateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FeatureKeysCertificateName_Type.__name__ = "DisplayString"
_FeatureKeysCertificateName_Object = MibScalar
featureKeysCertificateName = _FeatureKeysCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 5),
    _FeatureKeysCertificateName_Type()
)
featureKeysCertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureKeysCertificateName.setStatus("current")
_FeatureKeysCertificateRemoteIpAddress_Type = IpAddress
_FeatureKeysCertificateRemoteIpAddress_Object = MibScalar
featureKeysCertificateRemoteIpAddress = _FeatureKeysCertificateRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 6),
    _FeatureKeysCertificateRemoteIpAddress_Type()
)
featureKeysCertificateRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureKeysCertificateRemoteIpAddress.setStatus("current")


class _FeatureKeysLastOperationState_Type(Integer32):
    """Custom type featureKeysLastOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("downloadCompleted", 2),
          ("downloadTransferring", 3),
          ("downloadVerifying", 4),
          ("downloadInterrupted", 5),
          ("setSuccess", 6),
          ("setFailure", 7))
    )


_FeatureKeysLastOperationState_Type.__name__ = "Integer32"
_FeatureKeysLastOperationState_Object = MibScalar
featureKeysLastOperationState = _FeatureKeysLastOperationState_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 7),
    _FeatureKeysLastOperationState_Type()
)
featureKeysLastOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureKeysLastOperationState.setStatus("current")


class _FeatureKeysLastOperationFailure_Type(Integer32):
    """Custom type featureKeysLastOperationFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noFailure", 1),
          ("transfer", 2),
          ("serialNo", 3),
          ("verifySign", 4),
          ("primaryDigest", 5),
          ("secondaryDigest", 6))
    )


_FeatureKeysLastOperationFailure_Type.__name__ = "Integer32"
_FeatureKeysLastOperationFailure_Object = MibScalar
featureKeysLastOperationFailure = _FeatureKeysLastOperationFailure_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 101, 8),
    _FeatureKeysLastOperationFailure_Type()
)
featureKeysLastOperationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureKeysLastOperationFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-FEATUREKEYS-MIB",
    **{"featureKeys": featureKeys,
       "featureKeysMibVersion": featureKeysMibVersion,
       "featureKeysRadioMap": featureKeysRadioMap,
       "featureKeysLineMap": featureKeysLineMap,
       "featureKeysActionRequest": featureKeysActionRequest,
       "featureKeysCertificateName": featureKeysCertificateName,
       "featureKeysCertificateRemoteIpAddress": featureKeysCertificateRemoteIpAddress,
       "featureKeysLastOperationState": featureKeysLastOperationState,
       "featureKeysLastOperationFailure": featureKeysLastOperationFailure}
)
