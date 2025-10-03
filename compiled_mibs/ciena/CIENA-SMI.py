# SNMP MIB module (CIENA-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:18 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciena = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271)
)
if mibBuilder.loadTexts:
    ciena.setRevisions(
        ("2020-11-24 00:00",
         "2017-06-07 00:00",
         "2015-07-15 00:00",
         "2013-04-22 00:00",
         "2012-12-26 00:00",
         "2010-09-27 23:17")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCommon_ObjectIdentity = ObjectIdentity
cienaCommon = _CienaCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1)
)
if mibBuilder.loadTexts:
    cienaCommon.setStatus("current")
_CienaProducts_ObjectIdentity = ObjectIdentity
cienaProducts = _CienaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2)
)
if mibBuilder.loadTexts:
    cienaProducts.setStatus("current")
_CienaCes_ObjectIdentity = ObjectIdentity
cienaCes = _CienaCes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2)
)
if mibBuilder.loadTexts:
    cienaCes.setStatus("current")
_CienaCesConfig_ObjectIdentity = ObjectIdentity
cienaCesConfig = _CienaCesConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesConfig.setStatus("current")
_CienaCesNotifications_ObjectIdentity = ObjectIdentity
cienaCesNotifications = _CienaCesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesNotifications.setStatus("current")
_CienaCesNotificationsControlModule_ObjectIdentity = ObjectIdentity
cienaCesNotificationsControlModule = _CienaCesNotificationsControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesNotificationsControlModule.setStatus("current")
_CienaCesStatistics_ObjectIdentity = ObjectIdentity
cienaCesStatistics = _CienaCesStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesStatistics.setStatus("current")
_CienaRls_ObjectIdentity = ObjectIdentity
cienaRls = _CienaRls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 4)
)
if mibBuilder.loadTexts:
    cienaRls.setStatus("current")
_CienaGenericMIBs_ObjectIdentity = ObjectIdentity
cienaGenericMIBs = _CienaGenericMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 29)
)
if mibBuilder.loadTexts:
    cienaGenericMIBs.setStatus("current")
_CienaPro_ObjectIdentity = ObjectIdentity
cienaPro = _CienaPro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 30)
)
if mibBuilder.loadTexts:
    cienaPro.setStatus("current")
_CienaOpterametro_ObjectIdentity = ObjectIdentity
cienaOpterametro = _CienaOpterametro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 68)
)
if mibBuilder.loadTexts:
    cienaOpterametro.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-SMI",
    **{"ciena": ciena,
       "cienaCommon": cienaCommon,
       "cienaProducts": cienaProducts,
       "cienaCes": cienaCes,
       "cienaCesConfig": cienaCesConfig,
       "cienaCesNotifications": cienaCesNotifications,
       "cienaCesNotificationsControlModule": cienaCesNotificationsControlModule,
       "cienaCesStatistics": cienaCesStatistics,
       "cienaRls": cienaRls,
       "cienaGenericMIBs": cienaGenericMIBs,
       "cienaPro": cienaPro,
       "cienaOpterametro": cienaOpterametro}
)
