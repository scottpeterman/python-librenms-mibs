# SNMP MIB module (RUGGEDCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ros\RUGGEDCOM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:33 2025
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

ruggedcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004)
)
if mibBuilder.loadTexts:
    ruggedcom.setRevisions(
        ("2017-09-20 11:00",
         "2015-04-02 09:00",
         "2012-06-01 17:00",
         "2010-05-27 10:30",
         "2010-03-12 10:30",
         "2008-12-17 13:00",
         "2006-09-09 09:00",
         "2003-02-18 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuggedcomExperiment_ObjectIdentity = ObjectIdentity
ruggedcomExperiment = _RuggedcomExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 1)
)
if mibBuilder.loadTexts:
    ruggedcomExperiment.setStatus("current")
_RuggedcomProducts_ObjectIdentity = ObjectIdentity
ruggedcomProducts = _RuggedcomProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2)
)
if mibBuilder.loadTexts:
    ruggedcomProducts.setStatus("current")
_RuggedcomRX1XXX_ObjectIdentity = ObjectIdentity
ruggedcomRX1XXX = _RuggedcomRX1XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 4)
)
_RuggedcomRX1000_ObjectIdentity = ObjectIdentity
ruggedcomRX1000 = _RuggedcomRX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 4, 1)
)
_RuggedcomRX1100_ObjectIdentity = ObjectIdentity
ruggedcomRX1100 = _RuggedcomRX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 4, 2)
)
_RuggedcomRX5XXX_ObjectIdentity = ObjectIdentity
ruggedcomRX5XXX = _RuggedcomRX5XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 5)
)
_RuggedcomRX5000_ObjectIdentity = ObjectIdentity
ruggedcomRX5000 = _RuggedcomRX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 5, 1)
)
_RuggedcomMX5000_ObjectIdentity = ObjectIdentity
ruggedcomMX5000 = _RuggedcomMX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 5, 2)
)
_RuggedmaxProducts_ObjectIdentity = ObjectIdentity
ruggedmaxProducts = _RuggedmaxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 6)
)
_RuggedcomRX15XX_ObjectIdentity = ObjectIdentity
ruggedcomRX15XX = _RuggedcomRX15XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 8)
)
_RuggedcomRX1500_ObjectIdentity = ObjectIdentity
ruggedcomRX1500 = _RuggedcomRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 8, 1)
)
_RuggedcomRX1501_ObjectIdentity = ObjectIdentity
ruggedcomRX1501 = _RuggedcomRX1501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 8, 2)
)
_RuggedcomRX1510_ObjectIdentity = ObjectIdentity
ruggedcomRX1510 = _RuggedcomRX1510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 8, 11)
)
_RuggedcomRX1511_ObjectIdentity = ObjectIdentity
ruggedcomRX1511 = _RuggedcomRX1511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 8, 12)
)
_RuggedcomRX1512_ObjectIdentity = ObjectIdentity
ruggedcomRX1512 = _RuggedcomRX1512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 8, 13)
)
_RuggedcomRX1XXXrox2X_ObjectIdentity = ObjectIdentity
ruggedcomRX1XXXrox2X = _RuggedcomRX1XXXrox2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 9)
)
_RuggedcomRX1000rox2X_ObjectIdentity = ObjectIdentity
ruggedcomRX1000rox2X = _RuggedcomRX1000rox2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 9, 1)
)
_RuggedcomRX1100rox2X_ObjectIdentity = ObjectIdentity
ruggedcomRX1100rox2X = _RuggedcomRX1100rox2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 9, 2)
)
_RuggedcomAirModule_ObjectIdentity = ObjectIdentity
ruggedcomAirModule = _RuggedcomAirModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 10)
)
_RuggedcomMC_ObjectIdentity = ObjectIdentity
ruggedcomMC = _RuggedcomMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 11)
)
_RuggedcomOtherEnterprises_ObjectIdentity = ObjectIdentity
ruggedcomOtherEnterprises = _RuggedcomOtherEnterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 3)
)
if mibBuilder.loadTexts:
    ruggedcomOtherEnterprises.setStatus("current")
_RuggedcomMgmt_ObjectIdentity = ObjectIdentity
ruggedcomMgmt = _RuggedcomMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4)
)
if mibBuilder.loadTexts:
    ruggedcomMgmt.setStatus("current")
_RuggedcomTraps_ObjectIdentity = ObjectIdentity
ruggedcomTraps = _RuggedcomTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 5)
)
if mibBuilder.loadTexts:
    ruggedcomTraps.setStatus("current")
_RuggedcomAgentCapabilities_ObjectIdentity = ObjectIdentity
ruggedcomAgentCapabilities = _RuggedcomAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 6)
)
if mibBuilder.loadTexts:
    ruggedcomAgentCapabilities.setStatus("current")
_RuggedcomAgentCapability_ObjectIdentity = ObjectIdentity
ruggedcomAgentCapability = _RuggedcomAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30)
)
if mibBuilder.loadTexts:
    ruggedcomAgentCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-MIB",
    **{"ruggedcom": ruggedcom,
       "ruggedcomExperiment": ruggedcomExperiment,
       "ruggedcomProducts": ruggedcomProducts,
       "ruggedcomRX1XXX": ruggedcomRX1XXX,
       "ruggedcomRX1000": ruggedcomRX1000,
       "ruggedcomRX1100": ruggedcomRX1100,
       "ruggedcomRX5XXX": ruggedcomRX5XXX,
       "ruggedcomRX5000": ruggedcomRX5000,
       "ruggedcomMX5000": ruggedcomMX5000,
       "ruggedmaxProducts": ruggedmaxProducts,
       "ruggedcomRX15XX": ruggedcomRX15XX,
       "ruggedcomRX1500": ruggedcomRX1500,
       "ruggedcomRX1501": ruggedcomRX1501,
       "ruggedcomRX1510": ruggedcomRX1510,
       "ruggedcomRX1511": ruggedcomRX1511,
       "ruggedcomRX1512": ruggedcomRX1512,
       "ruggedcomRX1XXXrox2X": ruggedcomRX1XXXrox2X,
       "ruggedcomRX1000rox2X": ruggedcomRX1000rox2X,
       "ruggedcomRX1100rox2X": ruggedcomRX1100rox2X,
       "ruggedcomAirModule": ruggedcomAirModule,
       "ruggedcomMC": ruggedcomMC,
       "ruggedcomOtherEnterprises": ruggedcomOtherEnterprises,
       "ruggedcomMgmt": ruggedcomMgmt,
       "ruggedcomTraps": ruggedcomTraps,
       "ruggedcomAgentCapabilities": ruggedcomAgentCapabilities,
       "ruggedcomAgentCapability": ruggedcomAgentCapability}
)
