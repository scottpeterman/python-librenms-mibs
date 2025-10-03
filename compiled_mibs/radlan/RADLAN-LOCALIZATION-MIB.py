# SNMP MIB module (RADLAN-LOCALIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radlan\RADLAN-LOCALIZATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:21 2025
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlLocalization = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 103)
)
if mibBuilder.loadTexts:
    rlLocalization.setRevisions(
        ("2005-03-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlLanguage(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("original", 1),
          ("translated", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlLocalizationMibVersion_Type = Integer32
_RlLocalizationMibVersion_Object = MibScalar
rlLocalizationMibVersion = _RlLocalizationMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 103, 1),
    _RlLocalizationMibVersion_Type()
)
rlLocalizationMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationMibVersion.setStatus("current")
_RlLocalizationLanguage_Type = RlLanguage
_RlLocalizationLanguage_Object = MibScalar
rlLocalizationLanguage = _RlLocalizationLanguage_Object(
    (1, 3, 6, 1, 4, 1, 89, 103, 5),
    _RlLocalizationLanguage_Type()
)
rlLocalizationLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLocalizationLanguage.setStatus("current")
_RlWEBlocalizationLanguage_Type = RlLanguage
_RlWEBlocalizationLanguage_Object = MibScalar
rlWEBlocalizationLanguage = _RlWEBlocalizationLanguage_Object(
    (1, 3, 6, 1, 4, 1, 89, 103, 6),
    _RlWEBlocalizationLanguage_Type()
)
rlWEBlocalizationLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWEBlocalizationLanguage.setStatus("current")


class _RlLocalizationFiles_Type(Integer32):
    """Custom type rlLocalizationFiles based on Integer32"""
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
        *(("no-translated-files", 1),
          ("two-messages-files", 2),
          ("two-web-files", 3),
          ("two-messages-and-web-files", 4))
    )


_RlLocalizationFiles_Type.__name__ = "Integer32"
_RlLocalizationFiles_Object = MibScalar
rlLocalizationFiles = _RlLocalizationFiles_Object(
    (1, 3, 6, 1, 4, 1, 89, 103, 7),
    _RlLocalizationFiles_Type()
)
rlLocalizationFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationFiles.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-LOCALIZATION-MIB",
    **{"RlLanguage": RlLanguage,
       "rlLocalization": rlLocalization,
       "rlLocalizationMibVersion": rlLocalizationMibVersion,
       "rlLocalizationLanguage": rlLocalizationLanguage,
       "rlWEBlocalizationLanguage": rlWEBlocalizationLanguage,
       "rlLocalizationFiles": rlLocalizationFiles}
)
