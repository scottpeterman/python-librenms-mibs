# SNMP MIB module (CISCOSB-SSL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-SSL
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:55 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSsl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100)
)
if mibBuilder.loadTexts:
    rlSsl.setRevisions(
        ("2003-09-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlSslPublicKeyAlgorithm(TextualConvention, Integer32):
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
        *(("rsa", 1),
          ("dsa", 2),
          ("ec", 3),
          ("ecdsa", 4))
    )



class RlCaCertificateInstallType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("signer", 1),
          ("static", 2),
          ("dynamic", 3))
    )



class RlCaCertificateDisplayNonValidReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noReason", 0),
          ("premature", 1),
          ("expired", 2),
          ("revoked", 3),
          ("timeNotSet", 4),
          ("unknown", 5))
    )



class RlCaCertificateDisplayExtType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("publicKey", 0),
          ("signature", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlSslCertificateGenerationTable_Object = MibTable
rlSslCertificateGenerationTable = _RlSslCertificateGenerationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1)
)
if mibBuilder.loadTexts:
    rlSslCertificateGenerationTable.setStatus("current")
_RlSslCertificateGenerationEntry_Object = MibTableRow
rlSslCertificateGenerationEntry = _RlSslCertificateGenerationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1)
)
rlSslCertificateGenerationEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlSslCertificateGenerationIndex"),
)
if mibBuilder.loadTexts:
    rlSslCertificateGenerationEntry.setStatus("current")
_RlSslCertificateGenerationIndex_Type = Integer32
_RlSslCertificateGenerationIndex_Object = MibTableColumn
rlSslCertificateGenerationIndex = _RlSslCertificateGenerationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 1),
    _RlSslCertificateGenerationIndex_Type()
)
rlSslCertificateGenerationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationIndex.setStatus("current")
_RlSslCertificateGenerationId_Type = Integer32
_RlSslCertificateGenerationId_Object = MibTableColumn
rlSslCertificateGenerationId = _RlSslCertificateGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 2),
    _RlSslCertificateGenerationId_Type()
)
rlSslCertificateGenerationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationId.setStatus("current")


class _RlSslCertificateGenerationCountryName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_RlSslCertificateGenerationCountryName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationCountryName_Object = MibTableColumn
rlSslCertificateGenerationCountryName = _RlSslCertificateGenerationCountryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 3),
    _RlSslCertificateGenerationCountryName_Type()
)
rlSslCertificateGenerationCountryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationCountryName.setStatus("current")


class _RlSslCertificateGenerationStateOrProvinceName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationStateOrProvinceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationStateOrProvinceName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationStateOrProvinceName_Object = MibTableColumn
rlSslCertificateGenerationStateOrProvinceName = _RlSslCertificateGenerationStateOrProvinceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 4),
    _RlSslCertificateGenerationStateOrProvinceName_Type()
)
rlSslCertificateGenerationStateOrProvinceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationStateOrProvinceName.setStatus("current")


class _RlSslCertificateGenerationLocalityName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationLocalityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationLocalityName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationLocalityName_Object = MibTableColumn
rlSslCertificateGenerationLocalityName = _RlSslCertificateGenerationLocalityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 5),
    _RlSslCertificateGenerationLocalityName_Type()
)
rlSslCertificateGenerationLocalityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationLocalityName.setStatus("current")


class _RlSslCertificateGenerationOrganizationName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationOrganizationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationOrganizationName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationOrganizationName_Object = MibTableColumn
rlSslCertificateGenerationOrganizationName = _RlSslCertificateGenerationOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 6),
    _RlSslCertificateGenerationOrganizationName_Type()
)
rlSslCertificateGenerationOrganizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationOrganizationName.setStatus("current")


class _RlSslCertificateGenerationOrganizationUnitName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationOrganizationUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationOrganizationUnitName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationOrganizationUnitName_Object = MibTableColumn
rlSslCertificateGenerationOrganizationUnitName = _RlSslCertificateGenerationOrganizationUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 7),
    _RlSslCertificateGenerationOrganizationUnitName_Type()
)
rlSslCertificateGenerationOrganizationUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationOrganizationUnitName.setStatus("current")


class _RlSslCertificateGenerationCommonName_Type(DisplayString):
    """Custom type rlSslCertificateGenerationCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlSslCertificateGenerationCommonName_Type.__name__ = "DisplayString"
_RlSslCertificateGenerationCommonName_Object = MibTableColumn
rlSslCertificateGenerationCommonName = _RlSslCertificateGenerationCommonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 8),
    _RlSslCertificateGenerationCommonName_Type()
)
rlSslCertificateGenerationCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationCommonName.setStatus("current")
_RlSslCertificateGenerationValidDays_Type = Integer32
_RlSslCertificateGenerationValidDays_Object = MibTableColumn
rlSslCertificateGenerationValidDays = _RlSslCertificateGenerationValidDays_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 9),
    _RlSslCertificateGenerationValidDays_Type()
)
rlSslCertificateGenerationValidDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationValidDays.setStatus("current")


class _RlSslCertificateGenerationRsaKeyLength_Type(Integer32):
    """Custom type rlSslCertificateGenerationRsaKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 3072),
    )


_RlSslCertificateGenerationRsaKeyLength_Type.__name__ = "Integer32"
_RlSslCertificateGenerationRsaKeyLength_Object = MibTableColumn
rlSslCertificateGenerationRsaKeyLength = _RlSslCertificateGenerationRsaKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 10),
    _RlSslCertificateGenerationRsaKeyLength_Type()
)
rlSslCertificateGenerationRsaKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationRsaKeyLength.setStatus("current")
_RlSslCertificateGenerationPassphrase_Type = DisplayString
_RlSslCertificateGenerationPassphrase_Object = MibTableColumn
rlSslCertificateGenerationPassphrase = _RlSslCertificateGenerationPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 11),
    _RlSslCertificateGenerationPassphrase_Type()
)
rlSslCertificateGenerationPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationPassphrase.setStatus("current")


class _RlSslCertificateGenerationAction_Type(Integer32):
    """Custom type rlSslCertificateGenerationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("generateRsaKeyAndSelfSignedCertificate", 1),
          ("generateSelfSignedCertificate", 2),
          ("generatePkcs12", 3),
          ("generateCertificateRequest", 4),
          ("generateEcKeyAndSelfSignedCertificate", 5))
    )


_RlSslCertificateGenerationAction_Type.__name__ = "Integer32"
_RlSslCertificateGenerationAction_Object = MibTableColumn
rlSslCertificateGenerationAction = _RlSslCertificateGenerationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 12),
    _RlSslCertificateGenerationAction_Type()
)
rlSslCertificateGenerationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationAction.setStatus("current")


class _RlSslCertificateGenerationEcKeyCurve_Type(Integer32):
    """Custom type rlSslCertificateGenerationEcKeyCurve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RlSslCertificateGenerationEcKeyCurve_Type.__name__ = "Integer32"
_RlSslCertificateGenerationEcKeyCurve_Object = MibTableColumn
rlSslCertificateGenerationEcKeyCurve = _RlSslCertificateGenerationEcKeyCurve_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 13),
    _RlSslCertificateGenerationEcKeyCurve_Type()
)
rlSslCertificateGenerationEcKeyCurve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateGenerationEcKeyCurve.setStatus("current")
_RlSslCertificateExportTable_Object = MibTable
rlSslCertificateExportTable = _RlSslCertificateExportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2)
)
if mibBuilder.loadTexts:
    rlSslCertificateExportTable.setStatus("current")
_RlSslCertificateExportEntry_Object = MibTableRow
rlSslCertificateExportEntry = _RlSslCertificateExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1)
)
rlSslCertificateExportEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlSslCertificateExportId"),
    (0, "CISCOSB-SSL", "rlSslCertificateExportType"),
    (0, "CISCOSB-SSL", "rlSslCertificateExportFragmentId"),
)
if mibBuilder.loadTexts:
    rlSslCertificateExportEntry.setStatus("current")
_RlSslCertificateExportId_Type = Integer32
_RlSslCertificateExportId_Object = MibTableColumn
rlSslCertificateExportId = _RlSslCertificateExportId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 1),
    _RlSslCertificateExportId_Type()
)
rlSslCertificateExportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportId.setStatus("current")


class _RlSslCertificateExportType_Type(Integer32):
    """Custom type rlSslCertificateExportType based on Integer32"""
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
        *(("certificateRequestPemFormat", 1),
          ("certificatePemFormat", 2),
          ("certificateOpenSslFormat", 3),
          ("certificateAndKeyPkcs12", 4))
    )


_RlSslCertificateExportType_Type.__name__ = "Integer32"
_RlSslCertificateExportType_Object = MibTableColumn
rlSslCertificateExportType = _RlSslCertificateExportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 2),
    _RlSslCertificateExportType_Type()
)
rlSslCertificateExportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportType.setStatus("current")
_RlSslCertificateExportFragmentId_Type = Integer32
_RlSslCertificateExportFragmentId_Object = MibTableColumn
rlSslCertificateExportFragmentId = _RlSslCertificateExportFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 3),
    _RlSslCertificateExportFragmentId_Type()
)
rlSslCertificateExportFragmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportFragmentId.setStatus("current")
_RlSslCertificateExportFragmentText_Type = OctetString
_RlSslCertificateExportFragmentText_Object = MibTableColumn
rlSslCertificateExportFragmentText = _RlSslCertificateExportFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 4),
    _RlSslCertificateExportFragmentText_Type()
)
rlSslCertificateExportFragmentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSslCertificateExportFragmentText.setStatus("current")
_RlSslCertificateSave_Type = Integer32
_RlSslCertificateSave_Object = MibScalar
rlSslCertificateSave = _RlSslCertificateSave_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 3),
    _RlSslCertificateSave_Type()
)
rlSslCertificateSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateSave.setStatus("current")


class _RlSslCertificateSaveFormat_Type(Integer32):
    """Custom type rlSslCertificateSaveFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("x509", 1),
          ("pkcs12", 2))
    )


_RlSslCertificateSaveFormat_Type.__name__ = "Integer32"
_RlSslCertificateSaveFormat_Object = MibScalar
rlSslCertificateSaveFormat = _RlSslCertificateSaveFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 4),
    _RlSslCertificateSaveFormat_Type()
)
rlSslCertificateSaveFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateSaveFormat.setStatus("current")


class _RlSslImportedPKCS12CertificatePassphrase_Type(DisplayString):
    """Custom type rlSslImportedPKCS12CertificatePassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 96),
    )


_RlSslImportedPKCS12CertificatePassphrase_Type.__name__ = "DisplayString"
_RlSslImportedPKCS12CertificatePassphrase_Object = MibScalar
rlSslImportedPKCS12CertificatePassphrase = _RlSslImportedPKCS12CertificatePassphrase_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 5),
    _RlSslImportedPKCS12CertificatePassphrase_Type()
)
rlSslImportedPKCS12CertificatePassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslImportedPKCS12CertificatePassphrase.setStatus("current")
_RlSslCertificateImportTable_Object = MibTable
rlSslCertificateImportTable = _RlSslCertificateImportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6)
)
if mibBuilder.loadTexts:
    rlSslCertificateImportTable.setStatus("current")
_RlSslCertificateImportEntry_Object = MibTableRow
rlSslCertificateImportEntry = _RlSslCertificateImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1)
)
rlSslCertificateImportEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlSslCertificateImportId"),
    (0, "CISCOSB-SSL", "rlSslCertificateImportFormat"),
    (0, "CISCOSB-SSL", "rlSslCertificateImportFragmentId"),
)
if mibBuilder.loadTexts:
    rlSslCertificateImportEntry.setStatus("current")
_RlSslCertificateImportId_Type = Integer32
_RlSslCertificateImportId_Object = MibTableColumn
rlSslCertificateImportId = _RlSslCertificateImportId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 1),
    _RlSslCertificateImportId_Type()
)
rlSslCertificateImportId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportId.setStatus("current")


class _RlSslCertificateImportFormat_Type(Integer32):
    """Custom type rlSslCertificateImportFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("x509", 1),
          ("pkcs12", 2))
    )


_RlSslCertificateImportFormat_Type.__name__ = "Integer32"
_RlSslCertificateImportFormat_Object = MibTableColumn
rlSslCertificateImportFormat = _RlSslCertificateImportFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 2),
    _RlSslCertificateImportFormat_Type()
)
rlSslCertificateImportFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFormat.setStatus("current")
_RlSslCertificateImportFragmentId_Type = Integer32
_RlSslCertificateImportFragmentId_Object = MibTableColumn
rlSslCertificateImportFragmentId = _RlSslCertificateImportFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 3),
    _RlSslCertificateImportFragmentId_Type()
)
rlSslCertificateImportFragmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFragmentId.setStatus("current")
_RlSslCertificateImportFragmentText_Type = OctetString
_RlSslCertificateImportFragmentText_Object = MibTableColumn
rlSslCertificateImportFragmentText = _RlSslCertificateImportFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 4),
    _RlSslCertificateImportFragmentText_Type()
)
rlSslCertificateImportFragmentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFragmentText.setStatus("current")
_RlSslCertificateImportFragmentStatus_Type = RowStatus
_RlSslCertificateImportFragmentStatus_Object = MibTableColumn
rlSslCertificateImportFragmentStatus = _RlSslCertificateImportFragmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 5),
    _RlSslCertificateImportFragmentStatus_Type()
)
rlSslCertificateImportFragmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateImportFragmentStatus.setStatus("current")


class _RlSslSSLv2Enable_Type(Integer32):
    """Custom type rlSslSSLv2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlSslSSLv2Enable_Type.__name__ = "Integer32"
_RlSslSSLv2Enable_Object = MibScalar
rlSslSSLv2Enable = _RlSslSSLv2Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 7),
    _RlSslSSLv2Enable_Type()
)
rlSslSSLv2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslSSLv2Enable.setStatus("current")
_RlSslImportExportSelfKeyTable_Object = MibTable
rlSslImportExportSelfKeyTable = _RlSslImportExportSelfKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8)
)
if mibBuilder.loadTexts:
    rlSslImportExportSelfKeyTable.setStatus("current")
_RlSslImportExportSelfKeyEntry_Object = MibTableRow
rlSslImportExportSelfKeyEntry = _RlSslImportExportSelfKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1)
)
rlSslImportExportSelfKeyEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlSslImportExportSelfKeyFormat"),
    (0, "CISCOSB-SSL", "rlSslImportExportSelfKeyIndex"),
    (0, "CISCOSB-SSL", "rlSslImportExportSelfKeyFragmentId"),
)
if mibBuilder.loadTexts:
    rlSslImportExportSelfKeyEntry.setStatus("current")


class _RlSslImportExportSelfKeyFormat_Type(Integer32):
    """Custom type rlSslImportExportSelfKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("uuencoded-format", 1)
    )


_RlSslImportExportSelfKeyFormat_Type.__name__ = "Integer32"
_RlSslImportExportSelfKeyFormat_Object = MibTableColumn
rlSslImportExportSelfKeyFormat = _RlSslImportExportSelfKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 1),
    _RlSslImportExportSelfKeyFormat_Type()
)
rlSslImportExportSelfKeyFormat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSslImportExportSelfKeyFormat.setStatus("current")
_RlSslImportExportSelfKeyIndex_Type = Integer32
_RlSslImportExportSelfKeyIndex_Object = MibTableColumn
rlSslImportExportSelfKeyIndex = _RlSslImportExportSelfKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 2),
    _RlSslImportExportSelfKeyIndex_Type()
)
rlSslImportExportSelfKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSslImportExportSelfKeyIndex.setStatus("current")
_RlSslImportExportSelfKeyFragmentId_Type = Integer32
_RlSslImportExportSelfKeyFragmentId_Object = MibTableColumn
rlSslImportExportSelfKeyFragmentId = _RlSslImportExportSelfKeyFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 3),
    _RlSslImportExportSelfKeyFragmentId_Type()
)
rlSslImportExportSelfKeyFragmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSslImportExportSelfKeyFragmentId.setStatus("current")
_RlSslImportExportSelfKeyAlgorithm_Type = RlSslPublicKeyAlgorithm
_RlSslImportExportSelfKeyAlgorithm_Object = MibTableColumn
rlSslImportExportSelfKeyAlgorithm = _RlSslImportExportSelfKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 4),
    _RlSslImportExportSelfKeyAlgorithm_Type()
)
rlSslImportExportSelfKeyAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslImportExportSelfKeyAlgorithm.setStatus("current")
_RlSslImportExportSelfKeyFragmentText_Type = OctetString
_RlSslImportExportSelfKeyFragmentText_Object = MibTableColumn
rlSslImportExportSelfKeyFragmentText = _RlSslImportExportSelfKeyFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 5),
    _RlSslImportExportSelfKeyFragmentText_Type()
)
rlSslImportExportSelfKeyFragmentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslImportExportSelfKeyFragmentText.setStatus("current")
_RlSslCertificateSave2_Type = Integer32
_RlSslCertificateSave2_Object = MibScalar
rlSslCertificateSave2 = _RlSslCertificateSave2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 9),
    _RlSslCertificateSave2_Type()
)
rlSslCertificateSave2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslCertificateSave2.setStatus("current")
_RlSslisCertificate1Default_Type = TruthValue
_RlSslisCertificate1Default_Object = MibScalar
rlSslisCertificate1Default = _RlSslisCertificate1Default_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 10),
    _RlSslisCertificate1Default_Type()
)
rlSslisCertificate1Default.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslisCertificate1Default.setStatus("current")
_RlSslisCertificate2Default_Type = TruthValue
_RlSslisCertificate2Default_Object = MibScalar
rlSslisCertificate2Default = _RlSslisCertificate2Default_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 11),
    _RlSslisCertificate2Default_Type()
)
rlSslisCertificate2Default.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSslisCertificate2Default.setStatus("current")
_RlCaCertificateInstallTable_Object = MibTable
rlCaCertificateInstallTable = _RlCaCertificateInstallTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12)
)
if mibBuilder.loadTexts:
    rlCaCertificateInstallTable.setStatus("current")
_RlCaCertificateInstallEntry_Object = MibTableRow
rlCaCertificateInstallEntry = _RlCaCertificateInstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1)
)
rlCaCertificateInstallEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlCaCertificateInstallType"),
    (0, "CISCOSB-SSL", "rlCaCertificateInstallOwner"),
    (0, "CISCOSB-SSL", "rlCaCertificateInstallName"),
    (0, "CISCOSB-SSL", "rlCaCertificateInstallFragmentId"),
)
if mibBuilder.loadTexts:
    rlCaCertificateInstallEntry.setStatus("current")
_RlCaCertificateInstallType_Type = RlCaCertificateInstallType
_RlCaCertificateInstallType_Object = MibTableColumn
rlCaCertificateInstallType = _RlCaCertificateInstallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1, 1),
    _RlCaCertificateInstallType_Type()
)
rlCaCertificateInstallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateInstallType.setStatus("current")
_RlCaCertificateInstallOwner_Type = DisplayString
_RlCaCertificateInstallOwner_Object = MibTableColumn
rlCaCertificateInstallOwner = _RlCaCertificateInstallOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1, 2),
    _RlCaCertificateInstallOwner_Type()
)
rlCaCertificateInstallOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateInstallOwner.setStatus("current")
_RlCaCertificateInstallName_Type = DisplayString
_RlCaCertificateInstallName_Object = MibTableColumn
rlCaCertificateInstallName = _RlCaCertificateInstallName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1, 3),
    _RlCaCertificateInstallName_Type()
)
rlCaCertificateInstallName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateInstallName.setStatus("current")
_RlCaCertificateInstallFragmentId_Type = Integer32
_RlCaCertificateInstallFragmentId_Object = MibTableColumn
rlCaCertificateInstallFragmentId = _RlCaCertificateInstallFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1, 4),
    _RlCaCertificateInstallFragmentId_Type()
)
rlCaCertificateInstallFragmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateInstallFragmentId.setStatus("current")
_RlCaCertificateInstallFragmentPEMText_Type = OctetString
_RlCaCertificateInstallFragmentPEMText_Object = MibTableColumn
rlCaCertificateInstallFragmentPEMText = _RlCaCertificateInstallFragmentPEMText_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1, 5),
    _RlCaCertificateInstallFragmentPEMText_Type()
)
rlCaCertificateInstallFragmentPEMText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateInstallFragmentPEMText.setStatus("current")
_RlCaCertificateInstallFragmentStatus_Type = RowStatus
_RlCaCertificateInstallFragmentStatus_Object = MibTableColumn
rlCaCertificateInstallFragmentStatus = _RlCaCertificateInstallFragmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1, 6),
    _RlCaCertificateInstallFragmentStatus_Type()
)
rlCaCertificateInstallFragmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateInstallFragmentStatus.setStatus("current")
_RlCaCertificateInstallIsLastFragment_Type = TruthValue
_RlCaCertificateInstallIsLastFragment_Object = MibTableColumn
rlCaCertificateInstallIsLastFragment = _RlCaCertificateInstallIsLastFragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 12, 1, 7),
    _RlCaCertificateInstallIsLastFragment_Type()
)
rlCaCertificateInstallIsLastFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateInstallIsLastFragment.setStatus("current")
_RlCaCertificateDisplayTable_Object = MibTable
rlCaCertificateDisplayTable = _RlCaCertificateDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13)
)
if mibBuilder.loadTexts:
    rlCaCertificateDisplayTable.setStatus("current")
_RlCaCertificateDisplayEntry_Object = MibTableRow
rlCaCertificateDisplayEntry = _RlCaCertificateDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1)
)
rlCaCertificateDisplayEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlCaCertificateDisplayType"),
    (0, "CISCOSB-SSL", "rlCaCertificateDisplayOwner"),
    (0, "CISCOSB-SSL", "rlCaCertificateDisplayName"),
)
if mibBuilder.loadTexts:
    rlCaCertificateDisplayEntry.setStatus("current")
_RlCaCertificateDisplayType_Type = RlCaCertificateInstallType
_RlCaCertificateDisplayType_Object = MibTableColumn
rlCaCertificateDisplayType = _RlCaCertificateDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 1),
    _RlCaCertificateDisplayType_Type()
)
rlCaCertificateDisplayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayType.setStatus("current")
_RlCaCertificateDisplayOwner_Type = DisplayString
_RlCaCertificateDisplayOwner_Object = MibTableColumn
rlCaCertificateDisplayOwner = _RlCaCertificateDisplayOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 2),
    _RlCaCertificateDisplayOwner_Type()
)
rlCaCertificateDisplayOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayOwner.setStatus("current")
_RlCaCertificateDisplayName_Type = DisplayString
_RlCaCertificateDisplayName_Object = MibTableColumn
rlCaCertificateDisplayName = _RlCaCertificateDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 3),
    _RlCaCertificateDisplayName_Type()
)
rlCaCertificateDisplayName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayName.setStatus("current")
_RlCaCertificateDisplayVersion_Type = DisplayString
_RlCaCertificateDisplayVersion_Object = MibTableColumn
rlCaCertificateDisplayVersion = _RlCaCertificateDisplayVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 4),
    _RlCaCertificateDisplayVersion_Type()
)
rlCaCertificateDisplayVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayVersion.setStatus("current")
_RlCaCertificateDisplaySerialNumber_Type = OctetString
_RlCaCertificateDisplaySerialNumber_Object = MibTableColumn
rlCaCertificateDisplaySerialNumber = _RlCaCertificateDisplaySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 5),
    _RlCaCertificateDisplaySerialNumber_Type()
)
rlCaCertificateDisplaySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplaySerialNumber.setStatus("current")
_RlCaCertificateDisplayIssuerName_Type = DisplayString
_RlCaCertificateDisplayIssuerName_Object = MibTableColumn
rlCaCertificateDisplayIssuerName = _RlCaCertificateDisplayIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 6),
    _RlCaCertificateDisplayIssuerName_Type()
)
rlCaCertificateDisplayIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayIssuerName.setStatus("current")
_RlCaCertificateDisplaySubjectName_Type = DisplayString
_RlCaCertificateDisplaySubjectName_Object = MibTableColumn
rlCaCertificateDisplaySubjectName = _RlCaCertificateDisplaySubjectName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 7),
    _RlCaCertificateDisplaySubjectName_Type()
)
rlCaCertificateDisplaySubjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplaySubjectName.setStatus("current")
_RlCaCertificateDisplayNotBefore_Type = DisplayString
_RlCaCertificateDisplayNotBefore_Object = MibTableColumn
rlCaCertificateDisplayNotBefore = _RlCaCertificateDisplayNotBefore_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 8),
    _RlCaCertificateDisplayNotBefore_Type()
)
rlCaCertificateDisplayNotBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayNotBefore.setStatus("current")
_RlCaCertificateDisplayNotAfter_Type = DisplayString
_RlCaCertificateDisplayNotAfter_Object = MibTableColumn
rlCaCertificateDisplayNotAfter = _RlCaCertificateDisplayNotAfter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 9),
    _RlCaCertificateDisplayNotAfter_Type()
)
rlCaCertificateDisplayNotAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayNotAfter.setStatus("current")


class _RlCaCertificateDisplayValid_Type(TruthValue):
    """Custom type rlCaCertificateDisplayValid based on TruthValue"""
    defaultValue = 1


_RlCaCertificateDisplayValid_Type.__name__ = "TruthValue"
_RlCaCertificateDisplayValid_Object = MibTableColumn
rlCaCertificateDisplayValid = _RlCaCertificateDisplayValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 10),
    _RlCaCertificateDisplayValid_Type()
)
rlCaCertificateDisplayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayValid.setStatus("current")
_RlCaCertificateDisplayNonValidReason_Type = RlCaCertificateDisplayNonValidReason
_RlCaCertificateDisplayNonValidReason_Object = MibTableColumn
rlCaCertificateDisplayNonValidReason = _RlCaCertificateDisplayNonValidReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 11),
    _RlCaCertificateDisplayNonValidReason_Type()
)
rlCaCertificateDisplayNonValidReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayNonValidReason.setStatus("current")
_RlCaCertificateDisplaySignatureAlgorithm_Type = DisplayString
_RlCaCertificateDisplaySignatureAlgorithm_Object = MibTableColumn
rlCaCertificateDisplaySignatureAlgorithm = _RlCaCertificateDisplaySignatureAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 12),
    _RlCaCertificateDisplaySignatureAlgorithm_Type()
)
rlCaCertificateDisplaySignatureAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplaySignatureAlgorithm.setStatus("current")
_RlCaCertificateDisplayPublicKeyAlgorithm_Type = DisplayString
_RlCaCertificateDisplayPublicKeyAlgorithm_Object = MibTableColumn
rlCaCertificateDisplayPublicKeyAlgorithm = _RlCaCertificateDisplayPublicKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 13),
    _RlCaCertificateDisplayPublicKeyAlgorithm_Type()
)
rlCaCertificateDisplayPublicKeyAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayPublicKeyAlgorithm.setStatus("current")
_RlCaCertificateDisplayFingerprintAlgorithm_Type = DisplayString
_RlCaCertificateDisplayFingerprintAlgorithm_Object = MibTableColumn
rlCaCertificateDisplayFingerprintAlgorithm = _RlCaCertificateDisplayFingerprintAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 14),
    _RlCaCertificateDisplayFingerprintAlgorithm_Type()
)
rlCaCertificateDisplayFingerprintAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayFingerprintAlgorithm.setStatus("current")
_RlCaCertificateDisplayFingerprint_Type = OctetString
_RlCaCertificateDisplayFingerprint_Object = MibTableColumn
rlCaCertificateDisplayFingerprint = _RlCaCertificateDisplayFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 15),
    _RlCaCertificateDisplayFingerprint_Type()
)
rlCaCertificateDisplayFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayFingerprint.setStatus("current")
_RlCaCertificateDisplayPublicKeySize_Type = Integer32
_RlCaCertificateDisplayPublicKeySize_Object = MibTableColumn
rlCaCertificateDisplayPublicKeySize = _RlCaCertificateDisplayPublicKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 13, 1, 16),
    _RlCaCertificateDisplayPublicKeySize_Type()
)
rlCaCertificateDisplayPublicKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayPublicKeySize.setStatus("current")
_RlCaCertificateRevocationTable_Object = MibTable
rlCaCertificateRevocationTable = _RlCaCertificateRevocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 14)
)
if mibBuilder.loadTexts:
    rlCaCertificateRevocationTable.setStatus("current")
_RlCaCertificateRevocationEntry_Object = MibTableRow
rlCaCertificateRevocationEntry = _RlCaCertificateRevocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 14, 1)
)
rlCaCertificateRevocationEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlCaCertificateRevocationIssuerName"),
    (0, "CISCOSB-SSL", "rlCaCertificateRevocationSerialNumber"),
)
if mibBuilder.loadTexts:
    rlCaCertificateRevocationEntry.setStatus("current")
_RlCaCertificateRevocationIssuerName_Type = DisplayString
_RlCaCertificateRevocationIssuerName_Object = MibTableColumn
rlCaCertificateRevocationIssuerName = _RlCaCertificateRevocationIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 14, 1, 1),
    _RlCaCertificateRevocationIssuerName_Type()
)
rlCaCertificateRevocationIssuerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateRevocationIssuerName.setStatus("current")


class _RlCaCertificateRevocationSerialNumber_Type(OctetString):
    """Custom type rlCaCertificateRevocationSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlCaCertificateRevocationSerialNumber_Type.__name__ = "OctetString"
_RlCaCertificateRevocationSerialNumber_Object = MibTableColumn
rlCaCertificateRevocationSerialNumber = _RlCaCertificateRevocationSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 14, 1, 2),
    _RlCaCertificateRevocationSerialNumber_Type()
)
rlCaCertificateRevocationSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateRevocationSerialNumber.setStatus("current")
_RlCaCertificateRevocationRowStatus_Type = RowStatus
_RlCaCertificateRevocationRowStatus_Object = MibTableColumn
rlCaCertificateRevocationRowStatus = _RlCaCertificateRevocationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 14, 1, 3),
    _RlCaCertificateRevocationRowStatus_Type()
)
rlCaCertificateRevocationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCaCertificateRevocationRowStatus.setStatus("current")
_RlCaCertificateDisplayExtTable_Object = MibTable
rlCaCertificateDisplayExtTable = _RlCaCertificateDisplayExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 15)
)
if mibBuilder.loadTexts:
    rlCaCertificateDisplayExtTable.setStatus("current")
_RlCaCertificateDisplayExtEntry_Object = MibTableRow
rlCaCertificateDisplayExtEntry = _RlCaCertificateDisplayExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 15, 1)
)
rlCaCertificateDisplayExtEntry.setIndexNames(
    (0, "CISCOSB-SSL", "rlCaCertificateDisplayType"),
    (0, "CISCOSB-SSL", "rlCaCertificateDisplayOwner"),
    (0, "CISCOSB-SSL", "rlCaCertificateDisplayName"),
    (0, "CISCOSB-SSL", "rlCaCetrificateDisplayExtType"),
    (0, "CISCOSB-SSL", "rlCaCertificateDisplayExtFragmentId"),
)
if mibBuilder.loadTexts:
    rlCaCertificateDisplayExtEntry.setStatus("current")
_RlCaCetrificateDisplayExtType_Type = RlCaCertificateDisplayExtType
_RlCaCetrificateDisplayExtType_Object = MibTableColumn
rlCaCetrificateDisplayExtType = _RlCaCetrificateDisplayExtType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 15, 1, 1),
    _RlCaCetrificateDisplayExtType_Type()
)
rlCaCetrificateDisplayExtType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCaCetrificateDisplayExtType.setStatus("current")
_RlCaCertificateDisplayExtFragmentId_Type = Integer32
_RlCaCertificateDisplayExtFragmentId_Object = MibTableColumn
rlCaCertificateDisplayExtFragmentId = _RlCaCertificateDisplayExtFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 15, 1, 2),
    _RlCaCertificateDisplayExtFragmentId_Type()
)
rlCaCertificateDisplayExtFragmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayExtFragmentId.setStatus("current")
_RlCaCertificateDisplayExtFragmentData_Type = OctetString
_RlCaCertificateDisplayExtFragmentData_Object = MibTableColumn
rlCaCertificateDisplayExtFragmentData = _RlCaCertificateDisplayExtFragmentData_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 15, 1, 3),
    _RlCaCertificateDisplayExtFragmentData_Type()
)
rlCaCertificateDisplayExtFragmentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCaCertificateDisplayExtFragmentData.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SSL",
    **{"RlSslPublicKeyAlgorithm": RlSslPublicKeyAlgorithm,
       "RlCaCertificateInstallType": RlCaCertificateInstallType,
       "RlCaCertificateDisplayNonValidReason": RlCaCertificateDisplayNonValidReason,
       "RlCaCertificateDisplayExtType": RlCaCertificateDisplayExtType,
       "rlSsl": rlSsl,
       "rlSslCertificateGenerationTable": rlSslCertificateGenerationTable,
       "rlSslCertificateGenerationEntry": rlSslCertificateGenerationEntry,
       "rlSslCertificateGenerationIndex": rlSslCertificateGenerationIndex,
       "rlSslCertificateGenerationId": rlSslCertificateGenerationId,
       "rlSslCertificateGenerationCountryName": rlSslCertificateGenerationCountryName,
       "rlSslCertificateGenerationStateOrProvinceName": rlSslCertificateGenerationStateOrProvinceName,
       "rlSslCertificateGenerationLocalityName": rlSslCertificateGenerationLocalityName,
       "rlSslCertificateGenerationOrganizationName": rlSslCertificateGenerationOrganizationName,
       "rlSslCertificateGenerationOrganizationUnitName": rlSslCertificateGenerationOrganizationUnitName,
       "rlSslCertificateGenerationCommonName": rlSslCertificateGenerationCommonName,
       "rlSslCertificateGenerationValidDays": rlSslCertificateGenerationValidDays,
       "rlSslCertificateGenerationRsaKeyLength": rlSslCertificateGenerationRsaKeyLength,
       "rlSslCertificateGenerationPassphrase": rlSslCertificateGenerationPassphrase,
       "rlSslCertificateGenerationAction": rlSslCertificateGenerationAction,
       "rlSslCertificateGenerationEcKeyCurve": rlSslCertificateGenerationEcKeyCurve,
       "rlSslCertificateExportTable": rlSslCertificateExportTable,
       "rlSslCertificateExportEntry": rlSslCertificateExportEntry,
       "rlSslCertificateExportId": rlSslCertificateExportId,
       "rlSslCertificateExportType": rlSslCertificateExportType,
       "rlSslCertificateExportFragmentId": rlSslCertificateExportFragmentId,
       "rlSslCertificateExportFragmentText": rlSslCertificateExportFragmentText,
       "rlSslCertificateSave": rlSslCertificateSave,
       "rlSslCertificateSaveFormat": rlSslCertificateSaveFormat,
       "rlSslImportedPKCS12CertificatePassphrase": rlSslImportedPKCS12CertificatePassphrase,
       "rlSslCertificateImportTable": rlSslCertificateImportTable,
       "rlSslCertificateImportEntry": rlSslCertificateImportEntry,
       "rlSslCertificateImportId": rlSslCertificateImportId,
       "rlSslCertificateImportFormat": rlSslCertificateImportFormat,
       "rlSslCertificateImportFragmentId": rlSslCertificateImportFragmentId,
       "rlSslCertificateImportFragmentText": rlSslCertificateImportFragmentText,
       "rlSslCertificateImportFragmentStatus": rlSslCertificateImportFragmentStatus,
       "rlSslSSLv2Enable": rlSslSSLv2Enable,
       "rlSslImportExportSelfKeyTable": rlSslImportExportSelfKeyTable,
       "rlSslImportExportSelfKeyEntry": rlSslImportExportSelfKeyEntry,
       "rlSslImportExportSelfKeyFormat": rlSslImportExportSelfKeyFormat,
       "rlSslImportExportSelfKeyIndex": rlSslImportExportSelfKeyIndex,
       "rlSslImportExportSelfKeyFragmentId": rlSslImportExportSelfKeyFragmentId,
       "rlSslImportExportSelfKeyAlgorithm": rlSslImportExportSelfKeyAlgorithm,
       "rlSslImportExportSelfKeyFragmentText": rlSslImportExportSelfKeyFragmentText,
       "rlSslCertificateSave2": rlSslCertificateSave2,
       "rlSslisCertificate1Default": rlSslisCertificate1Default,
       "rlSslisCertificate2Default": rlSslisCertificate2Default,
       "rlCaCertificateInstallTable": rlCaCertificateInstallTable,
       "rlCaCertificateInstallEntry": rlCaCertificateInstallEntry,
       "rlCaCertificateInstallType": rlCaCertificateInstallType,
       "rlCaCertificateInstallOwner": rlCaCertificateInstallOwner,
       "rlCaCertificateInstallName": rlCaCertificateInstallName,
       "rlCaCertificateInstallFragmentId": rlCaCertificateInstallFragmentId,
       "rlCaCertificateInstallFragmentPEMText": rlCaCertificateInstallFragmentPEMText,
       "rlCaCertificateInstallFragmentStatus": rlCaCertificateInstallFragmentStatus,
       "rlCaCertificateInstallIsLastFragment": rlCaCertificateInstallIsLastFragment,
       "rlCaCertificateDisplayTable": rlCaCertificateDisplayTable,
       "rlCaCertificateDisplayEntry": rlCaCertificateDisplayEntry,
       "rlCaCertificateDisplayType": rlCaCertificateDisplayType,
       "rlCaCertificateDisplayOwner": rlCaCertificateDisplayOwner,
       "rlCaCertificateDisplayName": rlCaCertificateDisplayName,
       "rlCaCertificateDisplayVersion": rlCaCertificateDisplayVersion,
       "rlCaCertificateDisplaySerialNumber": rlCaCertificateDisplaySerialNumber,
       "rlCaCertificateDisplayIssuerName": rlCaCertificateDisplayIssuerName,
       "rlCaCertificateDisplaySubjectName": rlCaCertificateDisplaySubjectName,
       "rlCaCertificateDisplayNotBefore": rlCaCertificateDisplayNotBefore,
       "rlCaCertificateDisplayNotAfter": rlCaCertificateDisplayNotAfter,
       "rlCaCertificateDisplayValid": rlCaCertificateDisplayValid,
       "rlCaCertificateDisplayNonValidReason": rlCaCertificateDisplayNonValidReason,
       "rlCaCertificateDisplaySignatureAlgorithm": rlCaCertificateDisplaySignatureAlgorithm,
       "rlCaCertificateDisplayPublicKeyAlgorithm": rlCaCertificateDisplayPublicKeyAlgorithm,
       "rlCaCertificateDisplayFingerprintAlgorithm": rlCaCertificateDisplayFingerprintAlgorithm,
       "rlCaCertificateDisplayFingerprint": rlCaCertificateDisplayFingerprint,
       "rlCaCertificateDisplayPublicKeySize": rlCaCertificateDisplayPublicKeySize,
       "rlCaCertificateRevocationTable": rlCaCertificateRevocationTable,
       "rlCaCertificateRevocationEntry": rlCaCertificateRevocationEntry,
       "rlCaCertificateRevocationIssuerName": rlCaCertificateRevocationIssuerName,
       "rlCaCertificateRevocationSerialNumber": rlCaCertificateRevocationSerialNumber,
       "rlCaCertificateRevocationRowStatus": rlCaCertificateRevocationRowStatus,
       "rlCaCertificateDisplayExtTable": rlCaCertificateDisplayExtTable,
       "rlCaCertificateDisplayExtEntry": rlCaCertificateDisplayExtEntry,
       "rlCaCetrificateDisplayExtType": rlCaCetrificateDisplayExtType,
       "rlCaCertificateDisplayExtFragmentId": rlCaCertificateDisplayExtFragmentId,
       "rlCaCertificateDisplayExtFragmentData": rlCaCertificateDisplayExtFragmentData}
)
