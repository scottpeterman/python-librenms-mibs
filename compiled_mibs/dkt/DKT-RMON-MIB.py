# SNMP MIB module (DKT-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dkt\DKT-RMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:29 2025
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

(dkt,) = mibBuilder.importSymbols(
    "DKT-MIB",
    "dkt")

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

rmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RmonHistogramMode_Type(Integer32):
    """Custom type rmonHistogramMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RmonHistogramMode_Type.__name__ = "Integer32"
_RmonHistogramMode_Object = MibScalar
rmonHistogramMode = _RmonHistogramMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 1),
    _RmonHistogramMode_Type()
)
rmonHistogramMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistogramMode.setStatus("current")


class _RmonFlushAllCounter_Type(Integer32):
    """Custom type rmonFlushAllCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RmonFlushAllCounter_Type.__name__ = "Integer32"
_RmonFlushAllCounter_Object = MibScalar
rmonFlushAllCounter = _RmonFlushAllCounter_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 2),
    _RmonFlushAllCounter_Type()
)
rmonFlushAllCounter.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    rmonFlushAllCounter.setStatus("current")


class _RmonFlushPortCounter_Type(Integer32):
    """Custom type rmonFlushPortCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RmonFlushPortCounter_Type.__name__ = "Integer32"
_RmonFlushPortCounter_Object = MibScalar
rmonFlushPortCounter = _RmonFlushPortCounter_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 3),
    _RmonFlushPortCounter_Type()
)
rmonFlushPortCounter.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    rmonFlushPortCounter.setStatus("current")
_RmonPorts_ObjectIdentity = ObjectIdentity
rmonPorts = _RmonPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4)
)
_RmonCPUPort_ObjectIdentity = ObjectIdentity
rmonCPUPort = _RmonCPUPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1)
)
_RmonCPUPortGetInGoodOctetsLo_Type = Integer32
_RmonCPUPortGetInGoodOctetsLo_Object = MibScalar
rmonCPUPortGetInGoodOctetsLo = _RmonCPUPortGetInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 1),
    _RmonCPUPortGetInGoodOctetsLo_Type()
)
rmonCPUPortGetInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInGoodOctetsLo.setStatus("current")
_RmonCPUPortGetInGoodOctetsHi_Type = Integer32
_RmonCPUPortGetInGoodOctetsHi_Object = MibScalar
rmonCPUPortGetInGoodOctetsHi = _RmonCPUPortGetInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 2),
    _RmonCPUPortGetInGoodOctetsHi_Type()
)
rmonCPUPortGetInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInGoodOctetsHi.setStatus("current")
_RmonCPUPortGetInBadOctets_Type = Integer32
_RmonCPUPortGetInBadOctets_Object = MibScalar
rmonCPUPortGetInBadOctets = _RmonCPUPortGetInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 3),
    _RmonCPUPortGetInBadOctets_Type()
)
rmonCPUPortGetInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInBadOctets.setStatus("current")
_RmonCPUPortGetOutFCSErr_Type = Integer32
_RmonCPUPortGetOutFCSErr_Object = MibScalar
rmonCPUPortGetOutFCSErr = _RmonCPUPortGetOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 4),
    _RmonCPUPortGetOutFCSErr_Type()
)
rmonCPUPortGetOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOutFCSErr.setStatus("current")
_RmonCPUPortGetInUnicasts_Type = Integer32
_RmonCPUPortGetInUnicasts_Object = MibScalar
rmonCPUPortGetInUnicasts = _RmonCPUPortGetInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 5),
    _RmonCPUPortGetInUnicasts_Type()
)
rmonCPUPortGetInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInUnicasts.setStatus("current")
_RmonCPUPortGetDeferred_Type = Integer32
_RmonCPUPortGetDeferred_Object = MibScalar
rmonCPUPortGetDeferred = _RmonCPUPortGetDeferred_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 6),
    _RmonCPUPortGetDeferred_Type()
)
rmonCPUPortGetDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetDeferred.setStatus("current")
_RmonCPUPortGetInBroadcasts_Type = Integer32
_RmonCPUPortGetInBroadcasts_Object = MibScalar
rmonCPUPortGetInBroadcasts = _RmonCPUPortGetInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 7),
    _RmonCPUPortGetInBroadcasts_Type()
)
rmonCPUPortGetInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInBroadcasts.setStatus("current")
_RmonCPUPortGetInMulticasts_Type = Integer32
_RmonCPUPortGetInMulticasts_Object = MibScalar
rmonCPUPortGetInMulticasts = _RmonCPUPortGetInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 8),
    _RmonCPUPortGetInMulticasts_Type()
)
rmonCPUPortGetInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInMulticasts.setStatus("current")
_RmonCPUPortGetOctets64_Type = Integer32
_RmonCPUPortGetOctets64_Object = MibScalar
rmonCPUPortGetOctets64 = _RmonCPUPortGetOctets64_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 9),
    _RmonCPUPortGetOctets64_Type()
)
rmonCPUPortGetOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOctets64.setStatus("current")
_RmonCPUPortGetOctets127_Type = Integer32
_RmonCPUPortGetOctets127_Object = MibScalar
rmonCPUPortGetOctets127 = _RmonCPUPortGetOctets127_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 10),
    _RmonCPUPortGetOctets127_Type()
)
rmonCPUPortGetOctets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOctets127.setStatus("current")
_RmonCPUPortGetOctets255_Type = Integer32
_RmonCPUPortGetOctets255_Object = MibScalar
rmonCPUPortGetOctets255 = _RmonCPUPortGetOctets255_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 11),
    _RmonCPUPortGetOctets255_Type()
)
rmonCPUPortGetOctets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOctets255.setStatus("current")
_RmonCPUPortGetOctets511_Type = Integer32
_RmonCPUPortGetOctets511_Object = MibScalar
rmonCPUPortGetOctets511 = _RmonCPUPortGetOctets511_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 12),
    _RmonCPUPortGetOctets511_Type()
)
rmonCPUPortGetOctets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOctets511.setStatus("current")
_RmonCPUPortGetOctets1023_Type = Integer32
_RmonCPUPortGetOctets1023_Object = MibScalar
rmonCPUPortGetOctets1023 = _RmonCPUPortGetOctets1023_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 13),
    _RmonCPUPortGetOctets1023_Type()
)
rmonCPUPortGetOctets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOctets1023.setStatus("current")
_RmonCPUPortGetOctetsMax_Type = Integer32
_RmonCPUPortGetOctetsMax_Object = MibScalar
rmonCPUPortGetOctetsMax = _RmonCPUPortGetOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 14),
    _RmonCPUPortGetOctetsMax_Type()
)
rmonCPUPortGetOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOctetsMax.setStatus("current")
_RmonCPUPortGetOutOctetsLo_Type = Integer32
_RmonCPUPortGetOutOctetsLo_Object = MibScalar
rmonCPUPortGetOutOctetsLo = _RmonCPUPortGetOutOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 15),
    _RmonCPUPortGetOutOctetsLo_Type()
)
rmonCPUPortGetOutOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOutOctetsLo.setStatus("current")
_RmonCPUPortGetOutOctetsHi_Type = Integer32
_RmonCPUPortGetOutOctetsHi_Object = MibScalar
rmonCPUPortGetOutOctetsHi = _RmonCPUPortGetOutOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 16),
    _RmonCPUPortGetOutOctetsHi_Type()
)
rmonCPUPortGetOutOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOutOctetsHi.setStatus("current")
_RmonCPUPortGetOutUnicasts_Type = Integer32
_RmonCPUPortGetOutUnicasts_Object = MibScalar
rmonCPUPortGetOutUnicasts = _RmonCPUPortGetOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 17),
    _RmonCPUPortGetOutUnicasts_Type()
)
rmonCPUPortGetOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOutUnicasts.setStatus("current")
_RmonCPUPortGetExcessive_Type = Integer32
_RmonCPUPortGetExcessive_Object = MibScalar
rmonCPUPortGetExcessive = _RmonCPUPortGetExcessive_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 18),
    _RmonCPUPortGetExcessive_Type()
)
rmonCPUPortGetExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetExcessive.setStatus("current")
_RmonCPUPortGetOutMulticasts_Type = Integer32
_RmonCPUPortGetOutMulticasts_Object = MibScalar
rmonCPUPortGetOutMulticasts = _RmonCPUPortGetOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 19),
    _RmonCPUPortGetOutMulticasts_Type()
)
rmonCPUPortGetOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOutMulticasts.setStatus("current")
_RmonCPUPortGetOutBroadcasts_Type = Integer32
_RmonCPUPortGetOutBroadcasts_Object = MibScalar
rmonCPUPortGetOutBroadcasts = _RmonCPUPortGetOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 20),
    _RmonCPUPortGetOutBroadcasts_Type()
)
rmonCPUPortGetOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOutBroadcasts.setStatus("current")
_RmonCPUPortGetSingle_Type = Integer32
_RmonCPUPortGetSingle_Object = MibScalar
rmonCPUPortGetSingle = _RmonCPUPortGetSingle_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 21),
    _RmonCPUPortGetSingle_Type()
)
rmonCPUPortGetSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetSingle.setStatus("current")
_RmonCPUPortGetOutPause_Type = Integer32
_RmonCPUPortGetOutPause_Object = MibScalar
rmonCPUPortGetOutPause = _RmonCPUPortGetOutPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 22),
    _RmonCPUPortGetOutPause_Type()
)
rmonCPUPortGetOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOutPause.setStatus("current")
_RmonCPUPortGetInPause_Type = Integer32
_RmonCPUPortGetInPause_Object = MibScalar
rmonCPUPortGetInPause = _RmonCPUPortGetInPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 23),
    _RmonCPUPortGetInPause_Type()
)
rmonCPUPortGetInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInPause.setStatus("current")
_RmonCPUPortGetMultiple_Type = Integer32
_RmonCPUPortGetMultiple_Object = MibScalar
rmonCPUPortGetMultiple = _RmonCPUPortGetMultiple_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 24),
    _RmonCPUPortGetMultiple_Type()
)
rmonCPUPortGetMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetMultiple.setStatus("current")
_RmonCPUPortGetUndersize_Type = Integer32
_RmonCPUPortGetUndersize_Object = MibScalar
rmonCPUPortGetUndersize = _RmonCPUPortGetUndersize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 25),
    _RmonCPUPortGetUndersize_Type()
)
rmonCPUPortGetUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetUndersize.setStatus("current")
_RmonCPUPortGetFragments_Type = Integer32
_RmonCPUPortGetFragments_Object = MibScalar
rmonCPUPortGetFragments = _RmonCPUPortGetFragments_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 26),
    _RmonCPUPortGetFragments_Type()
)
rmonCPUPortGetFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetFragments.setStatus("current")
_RmonCPUPortGetOversize_Type = Integer32
_RmonCPUPortGetOversize_Object = MibScalar
rmonCPUPortGetOversize = _RmonCPUPortGetOversize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 27),
    _RmonCPUPortGetOversize_Type()
)
rmonCPUPortGetOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetOversize.setStatus("current")
_RmonCPUPortGetJabber_Type = Integer32
_RmonCPUPortGetJabber_Object = MibScalar
rmonCPUPortGetJabber = _RmonCPUPortGetJabber_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 28),
    _RmonCPUPortGetJabber_Type()
)
rmonCPUPortGetJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetJabber.setStatus("current")
_RmonCPUPortGetInMACRcvErr_Type = Integer32
_RmonCPUPortGetInMACRcvErr_Object = MibScalar
rmonCPUPortGetInMACRcvErr = _RmonCPUPortGetInMACRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 29),
    _RmonCPUPortGetInMACRcvErr_Type()
)
rmonCPUPortGetInMACRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInMACRcvErr.setStatus("current")
_RmonCPUPortGetInFCSErr_Type = Integer32
_RmonCPUPortGetInFCSErr_Object = MibScalar
rmonCPUPortGetInFCSErr = _RmonCPUPortGetInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 30),
    _RmonCPUPortGetInFCSErr_Type()
)
rmonCPUPortGetInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetInFCSErr.setStatus("current")
_RmonCPUPortGetCollisions_Type = Integer32
_RmonCPUPortGetCollisions_Object = MibScalar
rmonCPUPortGetCollisions = _RmonCPUPortGetCollisions_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 31),
    _RmonCPUPortGetCollisions_Type()
)
rmonCPUPortGetCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetCollisions.setStatus("current")
_RmonCPUPortGetLate_Type = Integer32
_RmonCPUPortGetLate_Object = MibScalar
rmonCPUPortGetLate = _RmonCPUPortGetLate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 1, 32),
    _RmonCPUPortGetLate_Type()
)
rmonCPUPortGetLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonCPUPortGetLate.setStatus("current")
_RmonWANPort_ObjectIdentity = ObjectIdentity
rmonWANPort = _RmonWANPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2)
)
_RmonWANPortGetInGoodOctetsLo_Type = Integer32
_RmonWANPortGetInGoodOctetsLo_Object = MibScalar
rmonWANPortGetInGoodOctetsLo = _RmonWANPortGetInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 1),
    _RmonWANPortGetInGoodOctetsLo_Type()
)
rmonWANPortGetInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInGoodOctetsLo.setStatus("current")
_RmonWANPortGetInGoodOctetsHi_Type = Integer32
_RmonWANPortGetInGoodOctetsHi_Object = MibScalar
rmonWANPortGetInGoodOctetsHi = _RmonWANPortGetInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 2),
    _RmonWANPortGetInGoodOctetsHi_Type()
)
rmonWANPortGetInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInGoodOctetsHi.setStatus("current")
_RmonWANPortGetInBadOctets_Type = Integer32
_RmonWANPortGetInBadOctets_Object = MibScalar
rmonWANPortGetInBadOctets = _RmonWANPortGetInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 3),
    _RmonWANPortGetInBadOctets_Type()
)
rmonWANPortGetInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInBadOctets.setStatus("current")
_RmonWANPortGetOutFCSErr_Type = Integer32
_RmonWANPortGetOutFCSErr_Object = MibScalar
rmonWANPortGetOutFCSErr = _RmonWANPortGetOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 4),
    _RmonWANPortGetOutFCSErr_Type()
)
rmonWANPortGetOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOutFCSErr.setStatus("current")
_RmonWANPortGetInUnicasts_Type = Integer32
_RmonWANPortGetInUnicasts_Object = MibScalar
rmonWANPortGetInUnicasts = _RmonWANPortGetInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 5),
    _RmonWANPortGetInUnicasts_Type()
)
rmonWANPortGetInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInUnicasts.setStatus("current")
_RmonWANPortGetDeferred_Type = Integer32
_RmonWANPortGetDeferred_Object = MibScalar
rmonWANPortGetDeferred = _RmonWANPortGetDeferred_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 6),
    _RmonWANPortGetDeferred_Type()
)
rmonWANPortGetDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetDeferred.setStatus("current")
_RmonWANPortGetInBroadcasts_Type = Integer32
_RmonWANPortGetInBroadcasts_Object = MibScalar
rmonWANPortGetInBroadcasts = _RmonWANPortGetInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 7),
    _RmonWANPortGetInBroadcasts_Type()
)
rmonWANPortGetInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInBroadcasts.setStatus("current")
_RmonWANPortGetInMulticasts_Type = Integer32
_RmonWANPortGetInMulticasts_Object = MibScalar
rmonWANPortGetInMulticasts = _RmonWANPortGetInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 8),
    _RmonWANPortGetInMulticasts_Type()
)
rmonWANPortGetInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInMulticasts.setStatus("current")
_RmonWANPortGetOctets64_Type = Integer32
_RmonWANPortGetOctets64_Object = MibScalar
rmonWANPortGetOctets64 = _RmonWANPortGetOctets64_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 9),
    _RmonWANPortGetOctets64_Type()
)
rmonWANPortGetOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOctets64.setStatus("current")
_RmonWANPortGetOctets127_Type = Integer32
_RmonWANPortGetOctets127_Object = MibScalar
rmonWANPortGetOctets127 = _RmonWANPortGetOctets127_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 10),
    _RmonWANPortGetOctets127_Type()
)
rmonWANPortGetOctets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOctets127.setStatus("current")
_RmonWANPortGetOctets255_Type = Integer32
_RmonWANPortGetOctets255_Object = MibScalar
rmonWANPortGetOctets255 = _RmonWANPortGetOctets255_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 11),
    _RmonWANPortGetOctets255_Type()
)
rmonWANPortGetOctets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOctets255.setStatus("current")
_RmonWANPortGetOctets511_Type = Integer32
_RmonWANPortGetOctets511_Object = MibScalar
rmonWANPortGetOctets511 = _RmonWANPortGetOctets511_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 12),
    _RmonWANPortGetOctets511_Type()
)
rmonWANPortGetOctets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOctets511.setStatus("current")
_RmonWANPortGetOctets1023_Type = Integer32
_RmonWANPortGetOctets1023_Object = MibScalar
rmonWANPortGetOctets1023 = _RmonWANPortGetOctets1023_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 13),
    _RmonWANPortGetOctets1023_Type()
)
rmonWANPortGetOctets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOctets1023.setStatus("current")
_RmonWANPortGetOctetsMax_Type = Integer32
_RmonWANPortGetOctetsMax_Object = MibScalar
rmonWANPortGetOctetsMax = _RmonWANPortGetOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 14),
    _RmonWANPortGetOctetsMax_Type()
)
rmonWANPortGetOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOctetsMax.setStatus("current")
_RmonWANPortGetOutOctetsLo_Type = Integer32
_RmonWANPortGetOutOctetsLo_Object = MibScalar
rmonWANPortGetOutOctetsLo = _RmonWANPortGetOutOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 15),
    _RmonWANPortGetOutOctetsLo_Type()
)
rmonWANPortGetOutOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOutOctetsLo.setStatus("current")
_RmonWANPortGetOutOctetsHi_Type = Integer32
_RmonWANPortGetOutOctetsHi_Object = MibScalar
rmonWANPortGetOutOctetsHi = _RmonWANPortGetOutOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 16),
    _RmonWANPortGetOutOctetsHi_Type()
)
rmonWANPortGetOutOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOutOctetsHi.setStatus("current")
_RmonWANPortGetOutUnicasts_Type = Integer32
_RmonWANPortGetOutUnicasts_Object = MibScalar
rmonWANPortGetOutUnicasts = _RmonWANPortGetOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 17),
    _RmonWANPortGetOutUnicasts_Type()
)
rmonWANPortGetOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOutUnicasts.setStatus("current")
_RmonWANPortGetExcessive_Type = Integer32
_RmonWANPortGetExcessive_Object = MibScalar
rmonWANPortGetExcessive = _RmonWANPortGetExcessive_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 18),
    _RmonWANPortGetExcessive_Type()
)
rmonWANPortGetExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetExcessive.setStatus("current")
_RmonWANPortGetOutMulticasts_Type = Integer32
_RmonWANPortGetOutMulticasts_Object = MibScalar
rmonWANPortGetOutMulticasts = _RmonWANPortGetOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 19),
    _RmonWANPortGetOutMulticasts_Type()
)
rmonWANPortGetOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOutMulticasts.setStatus("current")
_RmonWANPortGetOutBroadcasts_Type = Integer32
_RmonWANPortGetOutBroadcasts_Object = MibScalar
rmonWANPortGetOutBroadcasts = _RmonWANPortGetOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 20),
    _RmonWANPortGetOutBroadcasts_Type()
)
rmonWANPortGetOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOutBroadcasts.setStatus("current")
_RmonWANPortGetSingle_Type = Integer32
_RmonWANPortGetSingle_Object = MibScalar
rmonWANPortGetSingle = _RmonWANPortGetSingle_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 21),
    _RmonWANPortGetSingle_Type()
)
rmonWANPortGetSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetSingle.setStatus("current")
_RmonWANPortGetOutPause_Type = Integer32
_RmonWANPortGetOutPause_Object = MibScalar
rmonWANPortGetOutPause = _RmonWANPortGetOutPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 22),
    _RmonWANPortGetOutPause_Type()
)
rmonWANPortGetOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOutPause.setStatus("current")
_RmonWANPortGetInPause_Type = Integer32
_RmonWANPortGetInPause_Object = MibScalar
rmonWANPortGetInPause = _RmonWANPortGetInPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 23),
    _RmonWANPortGetInPause_Type()
)
rmonWANPortGetInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInPause.setStatus("current")
_RmonWANPortGetMultiple_Type = Integer32
_RmonWANPortGetMultiple_Object = MibScalar
rmonWANPortGetMultiple = _RmonWANPortGetMultiple_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 24),
    _RmonWANPortGetMultiple_Type()
)
rmonWANPortGetMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetMultiple.setStatus("current")
_RmonWANPortGetUndersize_Type = Integer32
_RmonWANPortGetUndersize_Object = MibScalar
rmonWANPortGetUndersize = _RmonWANPortGetUndersize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 25),
    _RmonWANPortGetUndersize_Type()
)
rmonWANPortGetUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetUndersize.setStatus("current")
_RmonWANPortGetFragments_Type = Integer32
_RmonWANPortGetFragments_Object = MibScalar
rmonWANPortGetFragments = _RmonWANPortGetFragments_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 26),
    _RmonWANPortGetFragments_Type()
)
rmonWANPortGetFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetFragments.setStatus("current")
_RmonWANPortGetOversize_Type = Integer32
_RmonWANPortGetOversize_Object = MibScalar
rmonWANPortGetOversize = _RmonWANPortGetOversize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 27),
    _RmonWANPortGetOversize_Type()
)
rmonWANPortGetOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetOversize.setStatus("current")
_RmonWANPortGetJabber_Type = Integer32
_RmonWANPortGetJabber_Object = MibScalar
rmonWANPortGetJabber = _RmonWANPortGetJabber_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 28),
    _RmonWANPortGetJabber_Type()
)
rmonWANPortGetJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetJabber.setStatus("current")
_RmonWANPortGetInMACRcvErr_Type = Integer32
_RmonWANPortGetInMACRcvErr_Object = MibScalar
rmonWANPortGetInMACRcvErr = _RmonWANPortGetInMACRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 29),
    _RmonWANPortGetInMACRcvErr_Type()
)
rmonWANPortGetInMACRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInMACRcvErr.setStatus("current")
_RmonWANPortGetInFCSErr_Type = Integer32
_RmonWANPortGetInFCSErr_Object = MibScalar
rmonWANPortGetInFCSErr = _RmonWANPortGetInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 30),
    _RmonWANPortGetInFCSErr_Type()
)
rmonWANPortGetInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetInFCSErr.setStatus("current")
_RmonWANPortGetCollisions_Type = Integer32
_RmonWANPortGetCollisions_Object = MibScalar
rmonWANPortGetCollisions = _RmonWANPortGetCollisions_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 31),
    _RmonWANPortGetCollisions_Type()
)
rmonWANPortGetCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetCollisions.setStatus("current")
_RmonWANPortGetLate_Type = Integer32
_RmonWANPortGetLate_Object = MibScalar
rmonWANPortGetLate = _RmonWANPortGetLate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 2, 32),
    _RmonWANPortGetLate_Type()
)
rmonWANPortGetLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonWANPortGetLate.setStatus("current")
_RmonLAN1Port_ObjectIdentity = ObjectIdentity
rmonLAN1Port = _RmonLAN1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3)
)
_RmonLAN1PortGetInGoodOctetsLo_Type = Integer32
_RmonLAN1PortGetInGoodOctetsLo_Object = MibScalar
rmonLAN1PortGetInGoodOctetsLo = _RmonLAN1PortGetInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 1),
    _RmonLAN1PortGetInGoodOctetsLo_Type()
)
rmonLAN1PortGetInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInGoodOctetsLo.setStatus("current")
_RmonLAN1PortGetInGoodOctetsHi_Type = Integer32
_RmonLAN1PortGetInGoodOctetsHi_Object = MibScalar
rmonLAN1PortGetInGoodOctetsHi = _RmonLAN1PortGetInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 2),
    _RmonLAN1PortGetInGoodOctetsHi_Type()
)
rmonLAN1PortGetInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInGoodOctetsHi.setStatus("current")
_RmonLAN1PortGetInBadOctets_Type = Integer32
_RmonLAN1PortGetInBadOctets_Object = MibScalar
rmonLAN1PortGetInBadOctets = _RmonLAN1PortGetInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 3),
    _RmonLAN1PortGetInBadOctets_Type()
)
rmonLAN1PortGetInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInBadOctets.setStatus("current")
_RmonLAN1PortGetOutFCSErr_Type = Integer32
_RmonLAN1PortGetOutFCSErr_Object = MibScalar
rmonLAN1PortGetOutFCSErr = _RmonLAN1PortGetOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 4),
    _RmonLAN1PortGetOutFCSErr_Type()
)
rmonLAN1PortGetOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOutFCSErr.setStatus("current")
_RmonLAN1PortGetInUnicasts_Type = Integer32
_RmonLAN1PortGetInUnicasts_Object = MibScalar
rmonLAN1PortGetInUnicasts = _RmonLAN1PortGetInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 5),
    _RmonLAN1PortGetInUnicasts_Type()
)
rmonLAN1PortGetInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInUnicasts.setStatus("current")
_RmonLAN1PortGetDeferred_Type = Integer32
_RmonLAN1PortGetDeferred_Object = MibScalar
rmonLAN1PortGetDeferred = _RmonLAN1PortGetDeferred_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 6),
    _RmonLAN1PortGetDeferred_Type()
)
rmonLAN1PortGetDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetDeferred.setStatus("current")
_RmonLAN1PortGetInBroadcasts_Type = Integer32
_RmonLAN1PortGetInBroadcasts_Object = MibScalar
rmonLAN1PortGetInBroadcasts = _RmonLAN1PortGetInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 7),
    _RmonLAN1PortGetInBroadcasts_Type()
)
rmonLAN1PortGetInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInBroadcasts.setStatus("current")
_RmonLAN1PortGetInMulticasts_Type = Integer32
_RmonLAN1PortGetInMulticasts_Object = MibScalar
rmonLAN1PortGetInMulticasts = _RmonLAN1PortGetInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 8),
    _RmonLAN1PortGetInMulticasts_Type()
)
rmonLAN1PortGetInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInMulticasts.setStatus("current")
_RmonLAN1PortGetOctets64_Type = Integer32
_RmonLAN1PortGetOctets64_Object = MibScalar
rmonLAN1PortGetOctets64 = _RmonLAN1PortGetOctets64_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 9),
    _RmonLAN1PortGetOctets64_Type()
)
rmonLAN1PortGetOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOctets64.setStatus("current")
_RmonLAN1PortGetOctets127_Type = Integer32
_RmonLAN1PortGetOctets127_Object = MibScalar
rmonLAN1PortGetOctets127 = _RmonLAN1PortGetOctets127_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 10),
    _RmonLAN1PortGetOctets127_Type()
)
rmonLAN1PortGetOctets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOctets127.setStatus("current")
_RmonLAN1PortGetOctets255_Type = Integer32
_RmonLAN1PortGetOctets255_Object = MibScalar
rmonLAN1PortGetOctets255 = _RmonLAN1PortGetOctets255_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 11),
    _RmonLAN1PortGetOctets255_Type()
)
rmonLAN1PortGetOctets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOctets255.setStatus("current")
_RmonLAN1PortGetOctets511_Type = Integer32
_RmonLAN1PortGetOctets511_Object = MibScalar
rmonLAN1PortGetOctets511 = _RmonLAN1PortGetOctets511_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 12),
    _RmonLAN1PortGetOctets511_Type()
)
rmonLAN1PortGetOctets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOctets511.setStatus("current")
_RmonLAN1PortGetOctets1023_Type = Integer32
_RmonLAN1PortGetOctets1023_Object = MibScalar
rmonLAN1PortGetOctets1023 = _RmonLAN1PortGetOctets1023_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 13),
    _RmonLAN1PortGetOctets1023_Type()
)
rmonLAN1PortGetOctets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOctets1023.setStatus("current")
_RmonLAN1PortGetOctetsMax_Type = Integer32
_RmonLAN1PortGetOctetsMax_Object = MibScalar
rmonLAN1PortGetOctetsMax = _RmonLAN1PortGetOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 14),
    _RmonLAN1PortGetOctetsMax_Type()
)
rmonLAN1PortGetOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOctetsMax.setStatus("current")
_RmonLAN1PortGetOutOctetsLo_Type = Integer32
_RmonLAN1PortGetOutOctetsLo_Object = MibScalar
rmonLAN1PortGetOutOctetsLo = _RmonLAN1PortGetOutOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 15),
    _RmonLAN1PortGetOutOctetsLo_Type()
)
rmonLAN1PortGetOutOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOutOctetsLo.setStatus("current")
_RmonLAN1PortGetOutOctetsHi_Type = Integer32
_RmonLAN1PortGetOutOctetsHi_Object = MibScalar
rmonLAN1PortGetOutOctetsHi = _RmonLAN1PortGetOutOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 16),
    _RmonLAN1PortGetOutOctetsHi_Type()
)
rmonLAN1PortGetOutOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOutOctetsHi.setStatus("current")
_RmonLAN1PortGetOutUnicasts_Type = Integer32
_RmonLAN1PortGetOutUnicasts_Object = MibScalar
rmonLAN1PortGetOutUnicasts = _RmonLAN1PortGetOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 17),
    _RmonLAN1PortGetOutUnicasts_Type()
)
rmonLAN1PortGetOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOutUnicasts.setStatus("current")
_RmonLAN1PortGetExcessive_Type = Integer32
_RmonLAN1PortGetExcessive_Object = MibScalar
rmonLAN1PortGetExcessive = _RmonLAN1PortGetExcessive_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 18),
    _RmonLAN1PortGetExcessive_Type()
)
rmonLAN1PortGetExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetExcessive.setStatus("current")
_RmonLAN1PortGetOutMulticasts_Type = Integer32
_RmonLAN1PortGetOutMulticasts_Object = MibScalar
rmonLAN1PortGetOutMulticasts = _RmonLAN1PortGetOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 19),
    _RmonLAN1PortGetOutMulticasts_Type()
)
rmonLAN1PortGetOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOutMulticasts.setStatus("current")
_RmonLAN1PortGetOutBroadcasts_Type = Integer32
_RmonLAN1PortGetOutBroadcasts_Object = MibScalar
rmonLAN1PortGetOutBroadcasts = _RmonLAN1PortGetOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 20),
    _RmonLAN1PortGetOutBroadcasts_Type()
)
rmonLAN1PortGetOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOutBroadcasts.setStatus("current")
_RmonLAN1PortGetSingle_Type = Integer32
_RmonLAN1PortGetSingle_Object = MibScalar
rmonLAN1PortGetSingle = _RmonLAN1PortGetSingle_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 21),
    _RmonLAN1PortGetSingle_Type()
)
rmonLAN1PortGetSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetSingle.setStatus("current")
_RmonLAN1PortGetOutPause_Type = Integer32
_RmonLAN1PortGetOutPause_Object = MibScalar
rmonLAN1PortGetOutPause = _RmonLAN1PortGetOutPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 22),
    _RmonLAN1PortGetOutPause_Type()
)
rmonLAN1PortGetOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOutPause.setStatus("current")
_RmonLAN1PortGetInPause_Type = Integer32
_RmonLAN1PortGetInPause_Object = MibScalar
rmonLAN1PortGetInPause = _RmonLAN1PortGetInPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 23),
    _RmonLAN1PortGetInPause_Type()
)
rmonLAN1PortGetInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInPause.setStatus("current")
_RmonLAN1PortGetMultiple_Type = Integer32
_RmonLAN1PortGetMultiple_Object = MibScalar
rmonLAN1PortGetMultiple = _RmonLAN1PortGetMultiple_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 24),
    _RmonLAN1PortGetMultiple_Type()
)
rmonLAN1PortGetMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetMultiple.setStatus("current")
_RmonLAN1PortGetUndersize_Type = Integer32
_RmonLAN1PortGetUndersize_Object = MibScalar
rmonLAN1PortGetUndersize = _RmonLAN1PortGetUndersize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 25),
    _RmonLAN1PortGetUndersize_Type()
)
rmonLAN1PortGetUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetUndersize.setStatus("current")
_RmonLAN1PortGetFragments_Type = Integer32
_RmonLAN1PortGetFragments_Object = MibScalar
rmonLAN1PortGetFragments = _RmonLAN1PortGetFragments_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 26),
    _RmonLAN1PortGetFragments_Type()
)
rmonLAN1PortGetFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetFragments.setStatus("current")
_RmonLAN1PortGetOversize_Type = Integer32
_RmonLAN1PortGetOversize_Object = MibScalar
rmonLAN1PortGetOversize = _RmonLAN1PortGetOversize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 27),
    _RmonLAN1PortGetOversize_Type()
)
rmonLAN1PortGetOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetOversize.setStatus("current")
_RmonLAN1PortGetJabber_Type = Integer32
_RmonLAN1PortGetJabber_Object = MibScalar
rmonLAN1PortGetJabber = _RmonLAN1PortGetJabber_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 28),
    _RmonLAN1PortGetJabber_Type()
)
rmonLAN1PortGetJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetJabber.setStatus("current")
_RmonLAN1PortGetInMACRcvErr_Type = Integer32
_RmonLAN1PortGetInMACRcvErr_Object = MibScalar
rmonLAN1PortGetInMACRcvErr = _RmonLAN1PortGetInMACRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 29),
    _RmonLAN1PortGetInMACRcvErr_Type()
)
rmonLAN1PortGetInMACRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInMACRcvErr.setStatus("current")
_RmonLAN1PortGetInFCSErr_Type = Integer32
_RmonLAN1PortGetInFCSErr_Object = MibScalar
rmonLAN1PortGetInFCSErr = _RmonLAN1PortGetInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 30),
    _RmonLAN1PortGetInFCSErr_Type()
)
rmonLAN1PortGetInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetInFCSErr.setStatus("current")
_RmonLAN1PortGetCollisions_Type = Integer32
_RmonLAN1PortGetCollisions_Object = MibScalar
rmonLAN1PortGetCollisions = _RmonLAN1PortGetCollisions_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 31),
    _RmonLAN1PortGetCollisions_Type()
)
rmonLAN1PortGetCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetCollisions.setStatus("current")
_RmonLAN1PortGetLate_Type = Integer32
_RmonLAN1PortGetLate_Object = MibScalar
rmonLAN1PortGetLate = _RmonLAN1PortGetLate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 3, 32),
    _RmonLAN1PortGetLate_Type()
)
rmonLAN1PortGetLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN1PortGetLate.setStatus("current")
_RmonLAN2Port_ObjectIdentity = ObjectIdentity
rmonLAN2Port = _RmonLAN2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4)
)
_RmonLAN2PortGetInGoodOctetsLo_Type = Integer32
_RmonLAN2PortGetInGoodOctetsLo_Object = MibScalar
rmonLAN2PortGetInGoodOctetsLo = _RmonLAN2PortGetInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 1),
    _RmonLAN2PortGetInGoodOctetsLo_Type()
)
rmonLAN2PortGetInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInGoodOctetsLo.setStatus("current")
_RmonLAN2PortGetInGoodOctetsHi_Type = Integer32
_RmonLAN2PortGetInGoodOctetsHi_Object = MibScalar
rmonLAN2PortGetInGoodOctetsHi = _RmonLAN2PortGetInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 2),
    _RmonLAN2PortGetInGoodOctetsHi_Type()
)
rmonLAN2PortGetInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInGoodOctetsHi.setStatus("current")
_RmonLAN2PortGetInBadOctets_Type = Integer32
_RmonLAN2PortGetInBadOctets_Object = MibScalar
rmonLAN2PortGetInBadOctets = _RmonLAN2PortGetInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 3),
    _RmonLAN2PortGetInBadOctets_Type()
)
rmonLAN2PortGetInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInBadOctets.setStatus("current")
_RmonLAN2PortGetOutFCSErr_Type = Integer32
_RmonLAN2PortGetOutFCSErr_Object = MibScalar
rmonLAN2PortGetOutFCSErr = _RmonLAN2PortGetOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 4),
    _RmonLAN2PortGetOutFCSErr_Type()
)
rmonLAN2PortGetOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOutFCSErr.setStatus("current")
_RmonLAN2PortGetInUnicasts_Type = Integer32
_RmonLAN2PortGetInUnicasts_Object = MibScalar
rmonLAN2PortGetInUnicasts = _RmonLAN2PortGetInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 5),
    _RmonLAN2PortGetInUnicasts_Type()
)
rmonLAN2PortGetInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInUnicasts.setStatus("current")
_RmonLAN2PortGetDeferred_Type = Integer32
_RmonLAN2PortGetDeferred_Object = MibScalar
rmonLAN2PortGetDeferred = _RmonLAN2PortGetDeferred_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 6),
    _RmonLAN2PortGetDeferred_Type()
)
rmonLAN2PortGetDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetDeferred.setStatus("current")
_RmonLAN2PortGetInBroadcasts_Type = Integer32
_RmonLAN2PortGetInBroadcasts_Object = MibScalar
rmonLAN2PortGetInBroadcasts = _RmonLAN2PortGetInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 7),
    _RmonLAN2PortGetInBroadcasts_Type()
)
rmonLAN2PortGetInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInBroadcasts.setStatus("current")
_RmonLAN2PortGetInMulticasts_Type = Integer32
_RmonLAN2PortGetInMulticasts_Object = MibScalar
rmonLAN2PortGetInMulticasts = _RmonLAN2PortGetInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 8),
    _RmonLAN2PortGetInMulticasts_Type()
)
rmonLAN2PortGetInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInMulticasts.setStatus("current")
_RmonLAN2PortGetOctets64_Type = Integer32
_RmonLAN2PortGetOctets64_Object = MibScalar
rmonLAN2PortGetOctets64 = _RmonLAN2PortGetOctets64_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 9),
    _RmonLAN2PortGetOctets64_Type()
)
rmonLAN2PortGetOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOctets64.setStatus("current")
_RmonLAN2PortGetOctets127_Type = Integer32
_RmonLAN2PortGetOctets127_Object = MibScalar
rmonLAN2PortGetOctets127 = _RmonLAN2PortGetOctets127_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 10),
    _RmonLAN2PortGetOctets127_Type()
)
rmonLAN2PortGetOctets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOctets127.setStatus("current")
_RmonLAN2PortGetOctets255_Type = Integer32
_RmonLAN2PortGetOctets255_Object = MibScalar
rmonLAN2PortGetOctets255 = _RmonLAN2PortGetOctets255_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 11),
    _RmonLAN2PortGetOctets255_Type()
)
rmonLAN2PortGetOctets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOctets255.setStatus("current")
_RmonLAN2PortGetOctets511_Type = Integer32
_RmonLAN2PortGetOctets511_Object = MibScalar
rmonLAN2PortGetOctets511 = _RmonLAN2PortGetOctets511_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 12),
    _RmonLAN2PortGetOctets511_Type()
)
rmonLAN2PortGetOctets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOctets511.setStatus("current")
_RmonLAN2PortGetOctets1023_Type = Integer32
_RmonLAN2PortGetOctets1023_Object = MibScalar
rmonLAN2PortGetOctets1023 = _RmonLAN2PortGetOctets1023_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 13),
    _RmonLAN2PortGetOctets1023_Type()
)
rmonLAN2PortGetOctets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOctets1023.setStatus("current")
_RmonLAN2PortGetOctetsMax_Type = Integer32
_RmonLAN2PortGetOctetsMax_Object = MibScalar
rmonLAN2PortGetOctetsMax = _RmonLAN2PortGetOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 14),
    _RmonLAN2PortGetOctetsMax_Type()
)
rmonLAN2PortGetOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOctetsMax.setStatus("current")
_RmonLAN2PortGetOutOctetsLo_Type = Integer32
_RmonLAN2PortGetOutOctetsLo_Object = MibScalar
rmonLAN2PortGetOutOctetsLo = _RmonLAN2PortGetOutOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 15),
    _RmonLAN2PortGetOutOctetsLo_Type()
)
rmonLAN2PortGetOutOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOutOctetsLo.setStatus("current")
_RmonLAN2PortGetOutOctetsHi_Type = Integer32
_RmonLAN2PortGetOutOctetsHi_Object = MibScalar
rmonLAN2PortGetOutOctetsHi = _RmonLAN2PortGetOutOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 16),
    _RmonLAN2PortGetOutOctetsHi_Type()
)
rmonLAN2PortGetOutOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOutOctetsHi.setStatus("current")
_RmonLAN2PortGetOutUnicasts_Type = Integer32
_RmonLAN2PortGetOutUnicasts_Object = MibScalar
rmonLAN2PortGetOutUnicasts = _RmonLAN2PortGetOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 17),
    _RmonLAN2PortGetOutUnicasts_Type()
)
rmonLAN2PortGetOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOutUnicasts.setStatus("current")
_RmonLAN2PortGetExcessive_Type = Integer32
_RmonLAN2PortGetExcessive_Object = MibScalar
rmonLAN2PortGetExcessive = _RmonLAN2PortGetExcessive_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 18),
    _RmonLAN2PortGetExcessive_Type()
)
rmonLAN2PortGetExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetExcessive.setStatus("current")
_RmonLAN2PortGetOutMulticasts_Type = Integer32
_RmonLAN2PortGetOutMulticasts_Object = MibScalar
rmonLAN2PortGetOutMulticasts = _RmonLAN2PortGetOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 19),
    _RmonLAN2PortGetOutMulticasts_Type()
)
rmonLAN2PortGetOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOutMulticasts.setStatus("current")
_RmonLAN2PortGetOutBroadcasts_Type = Integer32
_RmonLAN2PortGetOutBroadcasts_Object = MibScalar
rmonLAN2PortGetOutBroadcasts = _RmonLAN2PortGetOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 20),
    _RmonLAN2PortGetOutBroadcasts_Type()
)
rmonLAN2PortGetOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOutBroadcasts.setStatus("current")
_RmonLAN2PortGetSingle_Type = Integer32
_RmonLAN2PortGetSingle_Object = MibScalar
rmonLAN2PortGetSingle = _RmonLAN2PortGetSingle_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 21),
    _RmonLAN2PortGetSingle_Type()
)
rmonLAN2PortGetSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetSingle.setStatus("current")
_RmonLAN2PortGetOutPause_Type = Integer32
_RmonLAN2PortGetOutPause_Object = MibScalar
rmonLAN2PortGetOutPause = _RmonLAN2PortGetOutPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 22),
    _RmonLAN2PortGetOutPause_Type()
)
rmonLAN2PortGetOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOutPause.setStatus("current")
_RmonLAN2PortGetInPause_Type = Integer32
_RmonLAN2PortGetInPause_Object = MibScalar
rmonLAN2PortGetInPause = _RmonLAN2PortGetInPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 23),
    _RmonLAN2PortGetInPause_Type()
)
rmonLAN2PortGetInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInPause.setStatus("current")
_RmonLAN2PortGetMultiple_Type = Integer32
_RmonLAN2PortGetMultiple_Object = MibScalar
rmonLAN2PortGetMultiple = _RmonLAN2PortGetMultiple_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 24),
    _RmonLAN2PortGetMultiple_Type()
)
rmonLAN2PortGetMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetMultiple.setStatus("current")
_RmonLAN2PortGetUndersize_Type = Integer32
_RmonLAN2PortGetUndersize_Object = MibScalar
rmonLAN2PortGetUndersize = _RmonLAN2PortGetUndersize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 25),
    _RmonLAN2PortGetUndersize_Type()
)
rmonLAN2PortGetUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetUndersize.setStatus("current")
_RmonLAN2PortGetFragments_Type = Integer32
_RmonLAN2PortGetFragments_Object = MibScalar
rmonLAN2PortGetFragments = _RmonLAN2PortGetFragments_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 26),
    _RmonLAN2PortGetFragments_Type()
)
rmonLAN2PortGetFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetFragments.setStatus("current")
_RmonLAN2PortGetOversize_Type = Integer32
_RmonLAN2PortGetOversize_Object = MibScalar
rmonLAN2PortGetOversize = _RmonLAN2PortGetOversize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 27),
    _RmonLAN2PortGetOversize_Type()
)
rmonLAN2PortGetOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetOversize.setStatus("current")
_RmonLAN2PortGetJabber_Type = Integer32
_RmonLAN2PortGetJabber_Object = MibScalar
rmonLAN2PortGetJabber = _RmonLAN2PortGetJabber_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 28),
    _RmonLAN2PortGetJabber_Type()
)
rmonLAN2PortGetJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetJabber.setStatus("current")
_RmonLAN2PortGetInMACRcvErr_Type = Integer32
_RmonLAN2PortGetInMACRcvErr_Object = MibScalar
rmonLAN2PortGetInMACRcvErr = _RmonLAN2PortGetInMACRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 29),
    _RmonLAN2PortGetInMACRcvErr_Type()
)
rmonLAN2PortGetInMACRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInMACRcvErr.setStatus("current")
_RmonLAN2PortGetInFCSErr_Type = Integer32
_RmonLAN2PortGetInFCSErr_Object = MibScalar
rmonLAN2PortGetInFCSErr = _RmonLAN2PortGetInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 30),
    _RmonLAN2PortGetInFCSErr_Type()
)
rmonLAN2PortGetInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetInFCSErr.setStatus("current")
_RmonLAN2PortGetCollisions_Type = Integer32
_RmonLAN2PortGetCollisions_Object = MibScalar
rmonLAN2PortGetCollisions = _RmonLAN2PortGetCollisions_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 31),
    _RmonLAN2PortGetCollisions_Type()
)
rmonLAN2PortGetCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetCollisions.setStatus("current")
_RmonLAN2PortGetLate_Type = Integer32
_RmonLAN2PortGetLate_Object = MibScalar
rmonLAN2PortGetLate = _RmonLAN2PortGetLate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 4, 32),
    _RmonLAN2PortGetLate_Type()
)
rmonLAN2PortGetLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN2PortGetLate.setStatus("current")
_RmonLAN3Port_ObjectIdentity = ObjectIdentity
rmonLAN3Port = _RmonLAN3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5)
)
_RmonLAN3PortGetInGoodOctetsLo_Type = Integer32
_RmonLAN3PortGetInGoodOctetsLo_Object = MibScalar
rmonLAN3PortGetInGoodOctetsLo = _RmonLAN3PortGetInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 1),
    _RmonLAN3PortGetInGoodOctetsLo_Type()
)
rmonLAN3PortGetInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInGoodOctetsLo.setStatus("current")
_RmonLAN3PortGetInGoodOctetsHi_Type = Integer32
_RmonLAN3PortGetInGoodOctetsHi_Object = MibScalar
rmonLAN3PortGetInGoodOctetsHi = _RmonLAN3PortGetInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 2),
    _RmonLAN3PortGetInGoodOctetsHi_Type()
)
rmonLAN3PortGetInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInGoodOctetsHi.setStatus("current")
_RmonLAN3PortGetInBadOctets_Type = Integer32
_RmonLAN3PortGetInBadOctets_Object = MibScalar
rmonLAN3PortGetInBadOctets = _RmonLAN3PortGetInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 3),
    _RmonLAN3PortGetInBadOctets_Type()
)
rmonLAN3PortGetInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInBadOctets.setStatus("current")
_RmonLAN3PortGetOutFCSErr_Type = Integer32
_RmonLAN3PortGetOutFCSErr_Object = MibScalar
rmonLAN3PortGetOutFCSErr = _RmonLAN3PortGetOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 4),
    _RmonLAN3PortGetOutFCSErr_Type()
)
rmonLAN3PortGetOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOutFCSErr.setStatus("current")
_RmonLAN3PortGetInUnicasts_Type = Integer32
_RmonLAN3PortGetInUnicasts_Object = MibScalar
rmonLAN3PortGetInUnicasts = _RmonLAN3PortGetInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 5),
    _RmonLAN3PortGetInUnicasts_Type()
)
rmonLAN3PortGetInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInUnicasts.setStatus("current")
_RmonLAN3PortGetDeferred_Type = Integer32
_RmonLAN3PortGetDeferred_Object = MibScalar
rmonLAN3PortGetDeferred = _RmonLAN3PortGetDeferred_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 6),
    _RmonLAN3PortGetDeferred_Type()
)
rmonLAN3PortGetDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetDeferred.setStatus("current")
_RmonLAN3PortGetInBroadcasts_Type = Integer32
_RmonLAN3PortGetInBroadcasts_Object = MibScalar
rmonLAN3PortGetInBroadcasts = _RmonLAN3PortGetInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 7),
    _RmonLAN3PortGetInBroadcasts_Type()
)
rmonLAN3PortGetInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInBroadcasts.setStatus("current")
_RmonLAN3PortGetInMulticasts_Type = Integer32
_RmonLAN3PortGetInMulticasts_Object = MibScalar
rmonLAN3PortGetInMulticasts = _RmonLAN3PortGetInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 8),
    _RmonLAN3PortGetInMulticasts_Type()
)
rmonLAN3PortGetInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInMulticasts.setStatus("current")
_RmonLAN3PortGetOctets64_Type = Integer32
_RmonLAN3PortGetOctets64_Object = MibScalar
rmonLAN3PortGetOctets64 = _RmonLAN3PortGetOctets64_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 9),
    _RmonLAN3PortGetOctets64_Type()
)
rmonLAN3PortGetOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOctets64.setStatus("current")
_RmonLAN3PortGetOctets127_Type = Integer32
_RmonLAN3PortGetOctets127_Object = MibScalar
rmonLAN3PortGetOctets127 = _RmonLAN3PortGetOctets127_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 10),
    _RmonLAN3PortGetOctets127_Type()
)
rmonLAN3PortGetOctets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOctets127.setStatus("current")
_RmonLAN3PortGetOctets255_Type = Integer32
_RmonLAN3PortGetOctets255_Object = MibScalar
rmonLAN3PortGetOctets255 = _RmonLAN3PortGetOctets255_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 11),
    _RmonLAN3PortGetOctets255_Type()
)
rmonLAN3PortGetOctets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOctets255.setStatus("current")
_RmonLAN3PortGetOctets511_Type = Integer32
_RmonLAN3PortGetOctets511_Object = MibScalar
rmonLAN3PortGetOctets511 = _RmonLAN3PortGetOctets511_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 12),
    _RmonLAN3PortGetOctets511_Type()
)
rmonLAN3PortGetOctets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOctets511.setStatus("current")
_RmonLAN3PortGetOctets1023_Type = Integer32
_RmonLAN3PortGetOctets1023_Object = MibScalar
rmonLAN3PortGetOctets1023 = _RmonLAN3PortGetOctets1023_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 13),
    _RmonLAN3PortGetOctets1023_Type()
)
rmonLAN3PortGetOctets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOctets1023.setStatus("current")
_RmonLAN3PortGetOctetsMax_Type = Integer32
_RmonLAN3PortGetOctetsMax_Object = MibScalar
rmonLAN3PortGetOctetsMax = _RmonLAN3PortGetOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 14),
    _RmonLAN3PortGetOctetsMax_Type()
)
rmonLAN3PortGetOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOctetsMax.setStatus("current")
_RmonLAN3PortGetOutOctetsLo_Type = Integer32
_RmonLAN3PortGetOutOctetsLo_Object = MibScalar
rmonLAN3PortGetOutOctetsLo = _RmonLAN3PortGetOutOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 15),
    _RmonLAN3PortGetOutOctetsLo_Type()
)
rmonLAN3PortGetOutOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOutOctetsLo.setStatus("current")
_RmonLAN3PortGetOutOctetsHi_Type = Integer32
_RmonLAN3PortGetOutOctetsHi_Object = MibScalar
rmonLAN3PortGetOutOctetsHi = _RmonLAN3PortGetOutOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 16),
    _RmonLAN3PortGetOutOctetsHi_Type()
)
rmonLAN3PortGetOutOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOutOctetsHi.setStatus("current")
_RmonLAN3PortGetOutUnicasts_Type = Integer32
_RmonLAN3PortGetOutUnicasts_Object = MibScalar
rmonLAN3PortGetOutUnicasts = _RmonLAN3PortGetOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 17),
    _RmonLAN3PortGetOutUnicasts_Type()
)
rmonLAN3PortGetOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOutUnicasts.setStatus("current")
_RmonLAN3PortGetExcessive_Type = Integer32
_RmonLAN3PortGetExcessive_Object = MibScalar
rmonLAN3PortGetExcessive = _RmonLAN3PortGetExcessive_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 18),
    _RmonLAN3PortGetExcessive_Type()
)
rmonLAN3PortGetExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetExcessive.setStatus("current")
_RmonLAN3PortGetOutMulticasts_Type = Integer32
_RmonLAN3PortGetOutMulticasts_Object = MibScalar
rmonLAN3PortGetOutMulticasts = _RmonLAN3PortGetOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 19),
    _RmonLAN3PortGetOutMulticasts_Type()
)
rmonLAN3PortGetOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOutMulticasts.setStatus("current")
_RmonLAN3PortGetOutBroadcasts_Type = Integer32
_RmonLAN3PortGetOutBroadcasts_Object = MibScalar
rmonLAN3PortGetOutBroadcasts = _RmonLAN3PortGetOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 20),
    _RmonLAN3PortGetOutBroadcasts_Type()
)
rmonLAN3PortGetOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOutBroadcasts.setStatus("current")
_RmonLAN3PortGetSingle_Type = Integer32
_RmonLAN3PortGetSingle_Object = MibScalar
rmonLAN3PortGetSingle = _RmonLAN3PortGetSingle_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 21),
    _RmonLAN3PortGetSingle_Type()
)
rmonLAN3PortGetSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetSingle.setStatus("current")
_RmonLAN3PortGetOutPause_Type = Integer32
_RmonLAN3PortGetOutPause_Object = MibScalar
rmonLAN3PortGetOutPause = _RmonLAN3PortGetOutPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 22),
    _RmonLAN3PortGetOutPause_Type()
)
rmonLAN3PortGetOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOutPause.setStatus("current")
_RmonLAN3PortGetInPause_Type = Integer32
_RmonLAN3PortGetInPause_Object = MibScalar
rmonLAN3PortGetInPause = _RmonLAN3PortGetInPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 23),
    _RmonLAN3PortGetInPause_Type()
)
rmonLAN3PortGetInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInPause.setStatus("current")
_RmonLAN3PortGetMultiple_Type = Integer32
_RmonLAN3PortGetMultiple_Object = MibScalar
rmonLAN3PortGetMultiple = _RmonLAN3PortGetMultiple_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 24),
    _RmonLAN3PortGetMultiple_Type()
)
rmonLAN3PortGetMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetMultiple.setStatus("current")
_RmonLAN3PortGetUndersize_Type = Integer32
_RmonLAN3PortGetUndersize_Object = MibScalar
rmonLAN3PortGetUndersize = _RmonLAN3PortGetUndersize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 25),
    _RmonLAN3PortGetUndersize_Type()
)
rmonLAN3PortGetUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetUndersize.setStatus("current")
_RmonLAN3PortGetFragments_Type = Integer32
_RmonLAN3PortGetFragments_Object = MibScalar
rmonLAN3PortGetFragments = _RmonLAN3PortGetFragments_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 26),
    _RmonLAN3PortGetFragments_Type()
)
rmonLAN3PortGetFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetFragments.setStatus("current")
_RmonLAN3PortGetOversize_Type = Integer32
_RmonLAN3PortGetOversize_Object = MibScalar
rmonLAN3PortGetOversize = _RmonLAN3PortGetOversize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 27),
    _RmonLAN3PortGetOversize_Type()
)
rmonLAN3PortGetOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetOversize.setStatus("current")
_RmonLAN3PortGetJabber_Type = Integer32
_RmonLAN3PortGetJabber_Object = MibScalar
rmonLAN3PortGetJabber = _RmonLAN3PortGetJabber_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 28),
    _RmonLAN3PortGetJabber_Type()
)
rmonLAN3PortGetJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetJabber.setStatus("current")
_RmonLAN3PortGetInMACRcvErr_Type = Integer32
_RmonLAN3PortGetInMACRcvErr_Object = MibScalar
rmonLAN3PortGetInMACRcvErr = _RmonLAN3PortGetInMACRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 29),
    _RmonLAN3PortGetInMACRcvErr_Type()
)
rmonLAN3PortGetInMACRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInMACRcvErr.setStatus("current")
_RmonLAN3PortGetInFCSErr_Type = Integer32
_RmonLAN3PortGetInFCSErr_Object = MibScalar
rmonLAN3PortGetInFCSErr = _RmonLAN3PortGetInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 30),
    _RmonLAN3PortGetInFCSErr_Type()
)
rmonLAN3PortGetInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetInFCSErr.setStatus("current")
_RmonLAN3PortGetCollisions_Type = Integer32
_RmonLAN3PortGetCollisions_Object = MibScalar
rmonLAN3PortGetCollisions = _RmonLAN3PortGetCollisions_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 31),
    _RmonLAN3PortGetCollisions_Type()
)
rmonLAN3PortGetCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetCollisions.setStatus("current")
_RmonLAN3PortGetLate_Type = Integer32
_RmonLAN3PortGetLate_Object = MibScalar
rmonLAN3PortGetLate = _RmonLAN3PortGetLate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 5, 32),
    _RmonLAN3PortGetLate_Type()
)
rmonLAN3PortGetLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN3PortGetLate.setStatus("current")
_RmonLAN4Port_ObjectIdentity = ObjectIdentity
rmonLAN4Port = _RmonLAN4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6)
)
_RmonLAN4PortGetInGoodOctetsLo_Type = Integer32
_RmonLAN4PortGetInGoodOctetsLo_Object = MibScalar
rmonLAN4PortGetInGoodOctetsLo = _RmonLAN4PortGetInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 1),
    _RmonLAN4PortGetInGoodOctetsLo_Type()
)
rmonLAN4PortGetInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInGoodOctetsLo.setStatus("current")
_RmonLAN4PortGetInGoodOctetsHi_Type = Integer32
_RmonLAN4PortGetInGoodOctetsHi_Object = MibScalar
rmonLAN4PortGetInGoodOctetsHi = _RmonLAN4PortGetInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 2),
    _RmonLAN4PortGetInGoodOctetsHi_Type()
)
rmonLAN4PortGetInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInGoodOctetsHi.setStatus("current")
_RmonLAN4PortGetInBadOctets_Type = Integer32
_RmonLAN4PortGetInBadOctets_Object = MibScalar
rmonLAN4PortGetInBadOctets = _RmonLAN4PortGetInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 3),
    _RmonLAN4PortGetInBadOctets_Type()
)
rmonLAN4PortGetInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInBadOctets.setStatus("current")
_RmonLAN4PortGetOutFCSErr_Type = Integer32
_RmonLAN4PortGetOutFCSErr_Object = MibScalar
rmonLAN4PortGetOutFCSErr = _RmonLAN4PortGetOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 4),
    _RmonLAN4PortGetOutFCSErr_Type()
)
rmonLAN4PortGetOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOutFCSErr.setStatus("current")
_RmonLAN4PortGetInUnicasts_Type = Integer32
_RmonLAN4PortGetInUnicasts_Object = MibScalar
rmonLAN4PortGetInUnicasts = _RmonLAN4PortGetInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 5),
    _RmonLAN4PortGetInUnicasts_Type()
)
rmonLAN4PortGetInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInUnicasts.setStatus("current")
_RmonLAN4PortGetDeferred_Type = Integer32
_RmonLAN4PortGetDeferred_Object = MibScalar
rmonLAN4PortGetDeferred = _RmonLAN4PortGetDeferred_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 6),
    _RmonLAN4PortGetDeferred_Type()
)
rmonLAN4PortGetDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetDeferred.setStatus("current")
_RmonLAN4PortGetInBroadcasts_Type = Integer32
_RmonLAN4PortGetInBroadcasts_Object = MibScalar
rmonLAN4PortGetInBroadcasts = _RmonLAN4PortGetInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 7),
    _RmonLAN4PortGetInBroadcasts_Type()
)
rmonLAN4PortGetInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInBroadcasts.setStatus("current")
_RmonLAN4PortGetInMulticasts_Type = Integer32
_RmonLAN4PortGetInMulticasts_Object = MibScalar
rmonLAN4PortGetInMulticasts = _RmonLAN4PortGetInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 8),
    _RmonLAN4PortGetInMulticasts_Type()
)
rmonLAN4PortGetInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInMulticasts.setStatus("current")
_RmonLAN4PortGetOctets64_Type = Integer32
_RmonLAN4PortGetOctets64_Object = MibScalar
rmonLAN4PortGetOctets64 = _RmonLAN4PortGetOctets64_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 9),
    _RmonLAN4PortGetOctets64_Type()
)
rmonLAN4PortGetOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOctets64.setStatus("current")
_RmonLAN4PortGetOctets127_Type = Integer32
_RmonLAN4PortGetOctets127_Object = MibScalar
rmonLAN4PortGetOctets127 = _RmonLAN4PortGetOctets127_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 10),
    _RmonLAN4PortGetOctets127_Type()
)
rmonLAN4PortGetOctets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOctets127.setStatus("current")
_RmonLAN4PortGetOctets255_Type = Integer32
_RmonLAN4PortGetOctets255_Object = MibScalar
rmonLAN4PortGetOctets255 = _RmonLAN4PortGetOctets255_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 11),
    _RmonLAN4PortGetOctets255_Type()
)
rmonLAN4PortGetOctets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOctets255.setStatus("current")
_RmonLAN4PortGetOctets511_Type = Integer32
_RmonLAN4PortGetOctets511_Object = MibScalar
rmonLAN4PortGetOctets511 = _RmonLAN4PortGetOctets511_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 12),
    _RmonLAN4PortGetOctets511_Type()
)
rmonLAN4PortGetOctets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOctets511.setStatus("current")
_RmonLAN4PortGetOctets1023_Type = Integer32
_RmonLAN4PortGetOctets1023_Object = MibScalar
rmonLAN4PortGetOctets1023 = _RmonLAN4PortGetOctets1023_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 13),
    _RmonLAN4PortGetOctets1023_Type()
)
rmonLAN4PortGetOctets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOctets1023.setStatus("current")
_RmonLAN4PortGetOctetsMax_Type = Integer32
_RmonLAN4PortGetOctetsMax_Object = MibScalar
rmonLAN4PortGetOctetsMax = _RmonLAN4PortGetOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 14),
    _RmonLAN4PortGetOctetsMax_Type()
)
rmonLAN4PortGetOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOctetsMax.setStatus("current")
_RmonLAN4PortGetOutOctetsLo_Type = Integer32
_RmonLAN4PortGetOutOctetsLo_Object = MibScalar
rmonLAN4PortGetOutOctetsLo = _RmonLAN4PortGetOutOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 15),
    _RmonLAN4PortGetOutOctetsLo_Type()
)
rmonLAN4PortGetOutOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOutOctetsLo.setStatus("current")
_RmonLAN4PortGetOutOctetsHi_Type = Integer32
_RmonLAN4PortGetOutOctetsHi_Object = MibScalar
rmonLAN4PortGetOutOctetsHi = _RmonLAN4PortGetOutOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 16),
    _RmonLAN4PortGetOutOctetsHi_Type()
)
rmonLAN4PortGetOutOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOutOctetsHi.setStatus("current")
_RmonLAN4PortGetOutUnicasts_Type = Integer32
_RmonLAN4PortGetOutUnicasts_Object = MibScalar
rmonLAN4PortGetOutUnicasts = _RmonLAN4PortGetOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 17),
    _RmonLAN4PortGetOutUnicasts_Type()
)
rmonLAN4PortGetOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOutUnicasts.setStatus("current")
_RmonLAN4PortGetExcessive_Type = Integer32
_RmonLAN4PortGetExcessive_Object = MibScalar
rmonLAN4PortGetExcessive = _RmonLAN4PortGetExcessive_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 18),
    _RmonLAN4PortGetExcessive_Type()
)
rmonLAN4PortGetExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetExcessive.setStatus("current")
_RmonLAN4PortGetOutMulticasts_Type = Integer32
_RmonLAN4PortGetOutMulticasts_Object = MibScalar
rmonLAN4PortGetOutMulticasts = _RmonLAN4PortGetOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 19),
    _RmonLAN4PortGetOutMulticasts_Type()
)
rmonLAN4PortGetOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOutMulticasts.setStatus("current")
_RmonLAN4PortGetOutBroadcasts_Type = Integer32
_RmonLAN4PortGetOutBroadcasts_Object = MibScalar
rmonLAN4PortGetOutBroadcasts = _RmonLAN4PortGetOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 20),
    _RmonLAN4PortGetOutBroadcasts_Type()
)
rmonLAN4PortGetOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOutBroadcasts.setStatus("current")
_RmonLAN4PortGetSingle_Type = Integer32
_RmonLAN4PortGetSingle_Object = MibScalar
rmonLAN4PortGetSingle = _RmonLAN4PortGetSingle_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 21),
    _RmonLAN4PortGetSingle_Type()
)
rmonLAN4PortGetSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetSingle.setStatus("current")
_RmonLAN4PortGetOutPause_Type = Integer32
_RmonLAN4PortGetOutPause_Object = MibScalar
rmonLAN4PortGetOutPause = _RmonLAN4PortGetOutPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 22),
    _RmonLAN4PortGetOutPause_Type()
)
rmonLAN4PortGetOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOutPause.setStatus("current")
_RmonLAN4PortGetInPause_Type = Integer32
_RmonLAN4PortGetInPause_Object = MibScalar
rmonLAN4PortGetInPause = _RmonLAN4PortGetInPause_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 23),
    _RmonLAN4PortGetInPause_Type()
)
rmonLAN4PortGetInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInPause.setStatus("current")
_RmonLAN4PortGetMultiple_Type = Integer32
_RmonLAN4PortGetMultiple_Object = MibScalar
rmonLAN4PortGetMultiple = _RmonLAN4PortGetMultiple_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 24),
    _RmonLAN4PortGetMultiple_Type()
)
rmonLAN4PortGetMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetMultiple.setStatus("current")
_RmonLAN4PortGetUndersize_Type = Integer32
_RmonLAN4PortGetUndersize_Object = MibScalar
rmonLAN4PortGetUndersize = _RmonLAN4PortGetUndersize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 25),
    _RmonLAN4PortGetUndersize_Type()
)
rmonLAN4PortGetUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetUndersize.setStatus("current")
_RmonLAN4PortGetFragments_Type = Integer32
_RmonLAN4PortGetFragments_Object = MibScalar
rmonLAN4PortGetFragments = _RmonLAN4PortGetFragments_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 26),
    _RmonLAN4PortGetFragments_Type()
)
rmonLAN4PortGetFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetFragments.setStatus("current")
_RmonLAN4PortGetOversize_Type = Integer32
_RmonLAN4PortGetOversize_Object = MibScalar
rmonLAN4PortGetOversize = _RmonLAN4PortGetOversize_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 27),
    _RmonLAN4PortGetOversize_Type()
)
rmonLAN4PortGetOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetOversize.setStatus("current")
_RmonLAN4PortGetJabber_Type = Integer32
_RmonLAN4PortGetJabber_Object = MibScalar
rmonLAN4PortGetJabber = _RmonLAN4PortGetJabber_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 28),
    _RmonLAN4PortGetJabber_Type()
)
rmonLAN4PortGetJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetJabber.setStatus("current")
_RmonLAN4PortGetInMACRcvErr_Type = Integer32
_RmonLAN4PortGetInMACRcvErr_Object = MibScalar
rmonLAN4PortGetInMACRcvErr = _RmonLAN4PortGetInMACRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 29),
    _RmonLAN4PortGetInMACRcvErr_Type()
)
rmonLAN4PortGetInMACRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInMACRcvErr.setStatus("current")
_RmonLAN4PortGetInFCSErr_Type = Integer32
_RmonLAN4PortGetInFCSErr_Object = MibScalar
rmonLAN4PortGetInFCSErr = _RmonLAN4PortGetInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 30),
    _RmonLAN4PortGetInFCSErr_Type()
)
rmonLAN4PortGetInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetInFCSErr.setStatus("current")
_RmonLAN4PortGetCollisions_Type = Integer32
_RmonLAN4PortGetCollisions_Object = MibScalar
rmonLAN4PortGetCollisions = _RmonLAN4PortGetCollisions_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 31),
    _RmonLAN4PortGetCollisions_Type()
)
rmonLAN4PortGetCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetCollisions.setStatus("current")
_RmonLAN4PortGetLate_Type = Integer32
_RmonLAN4PortGetLate_Object = MibScalar
rmonLAN4PortGetLate = _RmonLAN4PortGetLate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 13, 4, 6, 32),
    _RmonLAN4PortGetLate_Type()
)
rmonLAN4PortGetLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLAN4PortGetLate.setStatus("current")

# Managed Objects groups

rmonModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27304, 13, 5)
)
rmonModuleGroup.setObjects(
      *(("DKT-RMON-MIB", "rmonHistogramMode"),
        ("DKT-RMON-MIB", "rmonFlushAllCounter"),
        ("DKT-RMON-MIB", "rmonFlushPortCounter"),
        ("DKT-RMON-MIB", "rmonPorts"),
        ("DKT-RMON-MIB", "rmonCPUPort"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInGoodOctetsLo"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInGoodOctetsHi"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInBadOctets"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOutFCSErr"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInUnicasts"),
        ("DKT-RMON-MIB", "rmonCPUPortGetDeferred"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInBroadcasts"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInMulticasts"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOctets64"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOctets127"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOctets255"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOctets511"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOctets1023"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOctetsMax"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOutOctetsLo"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOutOctetsHi"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOutUnicasts"),
        ("DKT-RMON-MIB", "rmonCPUPortGetExcessive"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOutMulticasts"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOutBroadcasts"),
        ("DKT-RMON-MIB", "rmonCPUPortGetSingle"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOutPause"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInPause"),
        ("DKT-RMON-MIB", "rmonCPUPortGetMultiple"),
        ("DKT-RMON-MIB", "rmonCPUPortGetUndersize"),
        ("DKT-RMON-MIB", "rmonCPUPortGetFragments"),
        ("DKT-RMON-MIB", "rmonCPUPortGetOversize"),
        ("DKT-RMON-MIB", "rmonCPUPortGetJabber"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInMACRcvErr"),
        ("DKT-RMON-MIB", "rmonCPUPortGetInFCSErr"),
        ("DKT-RMON-MIB", "rmonCPUPortGetCollisions"),
        ("DKT-RMON-MIB", "rmonCPUPortGetLate"),
        ("DKT-RMON-MIB", "rmonWANPort"),
        ("DKT-RMON-MIB", "rmonWANPortGetInGoodOctetsLo"),
        ("DKT-RMON-MIB", "rmonWANPortGetInGoodOctetsHi"),
        ("DKT-RMON-MIB", "rmonWANPortGetInBadOctets"),
        ("DKT-RMON-MIB", "rmonWANPortGetOutFCSErr"),
        ("DKT-RMON-MIB", "rmonWANPortGetInUnicasts"),
        ("DKT-RMON-MIB", "rmonWANPortGetDeferred"),
        ("DKT-RMON-MIB", "rmonWANPortGetInBroadcasts"),
        ("DKT-RMON-MIB", "rmonWANPortGetInMulticasts"),
        ("DKT-RMON-MIB", "rmonWANPortGetOctets64"),
        ("DKT-RMON-MIB", "rmonWANPortGetOctets127"),
        ("DKT-RMON-MIB", "rmonWANPortGetOctets255"),
        ("DKT-RMON-MIB", "rmonWANPortGetOctets511"),
        ("DKT-RMON-MIB", "rmonWANPortGetOctets1023"),
        ("DKT-RMON-MIB", "rmonWANPortGetOctetsMax"),
        ("DKT-RMON-MIB", "rmonWANPortGetOutOctetsLo"),
        ("DKT-RMON-MIB", "rmonWANPortGetOutOctetsHi"),
        ("DKT-RMON-MIB", "rmonWANPortGetOutUnicasts"),
        ("DKT-RMON-MIB", "rmonWANPortGetExcessive"),
        ("DKT-RMON-MIB", "rmonWANPortGetOutMulticasts"),
        ("DKT-RMON-MIB", "rmonWANPortGetOutBroadcasts"),
        ("DKT-RMON-MIB", "rmonWANPortGetSingle"),
        ("DKT-RMON-MIB", "rmonWANPortGetOutPause"),
        ("DKT-RMON-MIB", "rmonWANPortGetInPause"),
        ("DKT-RMON-MIB", "rmonWANPortGetMultiple"),
        ("DKT-RMON-MIB", "rmonWANPortGetUndersize"),
        ("DKT-RMON-MIB", "rmonWANPortGetFragments"),
        ("DKT-RMON-MIB", "rmonWANPortGetOversize"),
        ("DKT-RMON-MIB", "rmonWANPortGetJabber"),
        ("DKT-RMON-MIB", "rmonWANPortGetInMACRcvErr"),
        ("DKT-RMON-MIB", "rmonWANPortGetInFCSErr"),
        ("DKT-RMON-MIB", "rmonWANPortGetCollisions"),
        ("DKT-RMON-MIB", "rmonWANPortGetLate"),
        ("DKT-RMON-MIB", "rmonLAN1Port"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInGoodOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInGoodOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInBadOctets"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOutFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetDeferred"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOctets64"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOctets127"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOctets255"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOctets511"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOctets1023"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOctetsMax"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOutOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOutOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOutUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetExcessive"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOutMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOutBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetSingle"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOutPause"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInPause"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetMultiple"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetUndersize"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetFragments"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetOversize"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetJabber"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInMACRcvErr"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetInFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetCollisions"),
        ("DKT-RMON-MIB", "rmonLAN1PortGetLate"),
        ("DKT-RMON-MIB", "rmonLAN2Port"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInGoodOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInGoodOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInBadOctets"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOutFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetDeferred"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOctets64"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOctets127"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOctets255"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOctets511"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOctets1023"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOctetsMax"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOutOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOutOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOutUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetExcessive"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOutMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOutBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetSingle"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOutPause"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInPause"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetMultiple"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetUndersize"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetFragments"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetOversize"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetJabber"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInMACRcvErr"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetInFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetCollisions"),
        ("DKT-RMON-MIB", "rmonLAN2PortGetLate"),
        ("DKT-RMON-MIB", "rmonLAN3Port"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInGoodOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInGoodOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInBadOctets"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOutFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetDeferred"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOctets64"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOctets127"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOctets255"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOctets511"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOctets1023"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOctetsMax"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOutOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOutOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOutUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetExcessive"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOutMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOutBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetSingle"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOutPause"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInPause"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetMultiple"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetUndersize"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetFragments"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetOversize"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetJabber"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInMACRcvErr"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetInFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetCollisions"),
        ("DKT-RMON-MIB", "rmonLAN3PortGetLate"),
        ("DKT-RMON-MIB", "rmonLAN4Port"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInGoodOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInGoodOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInBadOctets"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOutFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetDeferred"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOctets64"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOctets127"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOctets255"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOctets511"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOctets1023"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOctetsMax"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOutOctetsLo"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOutOctetsHi"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOutUnicasts"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetExcessive"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOutMulticasts"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOutBroadcasts"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetSingle"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOutPause"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInPause"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetMultiple"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetUndersize"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetFragments"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetOversize"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetJabber"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInMACRcvErr"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetInFCSErr"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetCollisions"),
        ("DKT-RMON-MIB", "rmonLAN4PortGetLate"))
)
if mibBuilder.loadTexts:
    rmonModuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKT-RMON-MIB",
    **{"rmonMIB": rmonMIB,
       "rmonHistogramMode": rmonHistogramMode,
       "rmonFlushAllCounter": rmonFlushAllCounter,
       "rmonFlushPortCounter": rmonFlushPortCounter,
       "rmonPorts": rmonPorts,
       "rmonCPUPort": rmonCPUPort,
       "rmonCPUPortGetInGoodOctetsLo": rmonCPUPortGetInGoodOctetsLo,
       "rmonCPUPortGetInGoodOctetsHi": rmonCPUPortGetInGoodOctetsHi,
       "rmonCPUPortGetInBadOctets": rmonCPUPortGetInBadOctets,
       "rmonCPUPortGetOutFCSErr": rmonCPUPortGetOutFCSErr,
       "rmonCPUPortGetInUnicasts": rmonCPUPortGetInUnicasts,
       "rmonCPUPortGetDeferred": rmonCPUPortGetDeferred,
       "rmonCPUPortGetInBroadcasts": rmonCPUPortGetInBroadcasts,
       "rmonCPUPortGetInMulticasts": rmonCPUPortGetInMulticasts,
       "rmonCPUPortGetOctets64": rmonCPUPortGetOctets64,
       "rmonCPUPortGetOctets127": rmonCPUPortGetOctets127,
       "rmonCPUPortGetOctets255": rmonCPUPortGetOctets255,
       "rmonCPUPortGetOctets511": rmonCPUPortGetOctets511,
       "rmonCPUPortGetOctets1023": rmonCPUPortGetOctets1023,
       "rmonCPUPortGetOctetsMax": rmonCPUPortGetOctetsMax,
       "rmonCPUPortGetOutOctetsLo": rmonCPUPortGetOutOctetsLo,
       "rmonCPUPortGetOutOctetsHi": rmonCPUPortGetOutOctetsHi,
       "rmonCPUPortGetOutUnicasts": rmonCPUPortGetOutUnicasts,
       "rmonCPUPortGetExcessive": rmonCPUPortGetExcessive,
       "rmonCPUPortGetOutMulticasts": rmonCPUPortGetOutMulticasts,
       "rmonCPUPortGetOutBroadcasts": rmonCPUPortGetOutBroadcasts,
       "rmonCPUPortGetSingle": rmonCPUPortGetSingle,
       "rmonCPUPortGetOutPause": rmonCPUPortGetOutPause,
       "rmonCPUPortGetInPause": rmonCPUPortGetInPause,
       "rmonCPUPortGetMultiple": rmonCPUPortGetMultiple,
       "rmonCPUPortGetUndersize": rmonCPUPortGetUndersize,
       "rmonCPUPortGetFragments": rmonCPUPortGetFragments,
       "rmonCPUPortGetOversize": rmonCPUPortGetOversize,
       "rmonCPUPortGetJabber": rmonCPUPortGetJabber,
       "rmonCPUPortGetInMACRcvErr": rmonCPUPortGetInMACRcvErr,
       "rmonCPUPortGetInFCSErr": rmonCPUPortGetInFCSErr,
       "rmonCPUPortGetCollisions": rmonCPUPortGetCollisions,
       "rmonCPUPortGetLate": rmonCPUPortGetLate,
       "rmonWANPort": rmonWANPort,
       "rmonWANPortGetInGoodOctetsLo": rmonWANPortGetInGoodOctetsLo,
       "rmonWANPortGetInGoodOctetsHi": rmonWANPortGetInGoodOctetsHi,
       "rmonWANPortGetInBadOctets": rmonWANPortGetInBadOctets,
       "rmonWANPortGetOutFCSErr": rmonWANPortGetOutFCSErr,
       "rmonWANPortGetInUnicasts": rmonWANPortGetInUnicasts,
       "rmonWANPortGetDeferred": rmonWANPortGetDeferred,
       "rmonWANPortGetInBroadcasts": rmonWANPortGetInBroadcasts,
       "rmonWANPortGetInMulticasts": rmonWANPortGetInMulticasts,
       "rmonWANPortGetOctets64": rmonWANPortGetOctets64,
       "rmonWANPortGetOctets127": rmonWANPortGetOctets127,
       "rmonWANPortGetOctets255": rmonWANPortGetOctets255,
       "rmonWANPortGetOctets511": rmonWANPortGetOctets511,
       "rmonWANPortGetOctets1023": rmonWANPortGetOctets1023,
       "rmonWANPortGetOctetsMax": rmonWANPortGetOctetsMax,
       "rmonWANPortGetOutOctetsLo": rmonWANPortGetOutOctetsLo,
       "rmonWANPortGetOutOctetsHi": rmonWANPortGetOutOctetsHi,
       "rmonWANPortGetOutUnicasts": rmonWANPortGetOutUnicasts,
       "rmonWANPortGetExcessive": rmonWANPortGetExcessive,
       "rmonWANPortGetOutMulticasts": rmonWANPortGetOutMulticasts,
       "rmonWANPortGetOutBroadcasts": rmonWANPortGetOutBroadcasts,
       "rmonWANPortGetSingle": rmonWANPortGetSingle,
       "rmonWANPortGetOutPause": rmonWANPortGetOutPause,
       "rmonWANPortGetInPause": rmonWANPortGetInPause,
       "rmonWANPortGetMultiple": rmonWANPortGetMultiple,
       "rmonWANPortGetUndersize": rmonWANPortGetUndersize,
       "rmonWANPortGetFragments": rmonWANPortGetFragments,
       "rmonWANPortGetOversize": rmonWANPortGetOversize,
       "rmonWANPortGetJabber": rmonWANPortGetJabber,
       "rmonWANPortGetInMACRcvErr": rmonWANPortGetInMACRcvErr,
       "rmonWANPortGetInFCSErr": rmonWANPortGetInFCSErr,
       "rmonWANPortGetCollisions": rmonWANPortGetCollisions,
       "rmonWANPortGetLate": rmonWANPortGetLate,
       "rmonLAN1Port": rmonLAN1Port,
       "rmonLAN1PortGetInGoodOctetsLo": rmonLAN1PortGetInGoodOctetsLo,
       "rmonLAN1PortGetInGoodOctetsHi": rmonLAN1PortGetInGoodOctetsHi,
       "rmonLAN1PortGetInBadOctets": rmonLAN1PortGetInBadOctets,
       "rmonLAN1PortGetOutFCSErr": rmonLAN1PortGetOutFCSErr,
       "rmonLAN1PortGetInUnicasts": rmonLAN1PortGetInUnicasts,
       "rmonLAN1PortGetDeferred": rmonLAN1PortGetDeferred,
       "rmonLAN1PortGetInBroadcasts": rmonLAN1PortGetInBroadcasts,
       "rmonLAN1PortGetInMulticasts": rmonLAN1PortGetInMulticasts,
       "rmonLAN1PortGetOctets64": rmonLAN1PortGetOctets64,
       "rmonLAN1PortGetOctets127": rmonLAN1PortGetOctets127,
       "rmonLAN1PortGetOctets255": rmonLAN1PortGetOctets255,
       "rmonLAN1PortGetOctets511": rmonLAN1PortGetOctets511,
       "rmonLAN1PortGetOctets1023": rmonLAN1PortGetOctets1023,
       "rmonLAN1PortGetOctetsMax": rmonLAN1PortGetOctetsMax,
       "rmonLAN1PortGetOutOctetsLo": rmonLAN1PortGetOutOctetsLo,
       "rmonLAN1PortGetOutOctetsHi": rmonLAN1PortGetOutOctetsHi,
       "rmonLAN1PortGetOutUnicasts": rmonLAN1PortGetOutUnicasts,
       "rmonLAN1PortGetExcessive": rmonLAN1PortGetExcessive,
       "rmonLAN1PortGetOutMulticasts": rmonLAN1PortGetOutMulticasts,
       "rmonLAN1PortGetOutBroadcasts": rmonLAN1PortGetOutBroadcasts,
       "rmonLAN1PortGetSingle": rmonLAN1PortGetSingle,
       "rmonLAN1PortGetOutPause": rmonLAN1PortGetOutPause,
       "rmonLAN1PortGetInPause": rmonLAN1PortGetInPause,
       "rmonLAN1PortGetMultiple": rmonLAN1PortGetMultiple,
       "rmonLAN1PortGetUndersize": rmonLAN1PortGetUndersize,
       "rmonLAN1PortGetFragments": rmonLAN1PortGetFragments,
       "rmonLAN1PortGetOversize": rmonLAN1PortGetOversize,
       "rmonLAN1PortGetJabber": rmonLAN1PortGetJabber,
       "rmonLAN1PortGetInMACRcvErr": rmonLAN1PortGetInMACRcvErr,
       "rmonLAN1PortGetInFCSErr": rmonLAN1PortGetInFCSErr,
       "rmonLAN1PortGetCollisions": rmonLAN1PortGetCollisions,
       "rmonLAN1PortGetLate": rmonLAN1PortGetLate,
       "rmonLAN2Port": rmonLAN2Port,
       "rmonLAN2PortGetInGoodOctetsLo": rmonLAN2PortGetInGoodOctetsLo,
       "rmonLAN2PortGetInGoodOctetsHi": rmonLAN2PortGetInGoodOctetsHi,
       "rmonLAN2PortGetInBadOctets": rmonLAN2PortGetInBadOctets,
       "rmonLAN2PortGetOutFCSErr": rmonLAN2PortGetOutFCSErr,
       "rmonLAN2PortGetInUnicasts": rmonLAN2PortGetInUnicasts,
       "rmonLAN2PortGetDeferred": rmonLAN2PortGetDeferred,
       "rmonLAN2PortGetInBroadcasts": rmonLAN2PortGetInBroadcasts,
       "rmonLAN2PortGetInMulticasts": rmonLAN2PortGetInMulticasts,
       "rmonLAN2PortGetOctets64": rmonLAN2PortGetOctets64,
       "rmonLAN2PortGetOctets127": rmonLAN2PortGetOctets127,
       "rmonLAN2PortGetOctets255": rmonLAN2PortGetOctets255,
       "rmonLAN2PortGetOctets511": rmonLAN2PortGetOctets511,
       "rmonLAN2PortGetOctets1023": rmonLAN2PortGetOctets1023,
       "rmonLAN2PortGetOctetsMax": rmonLAN2PortGetOctetsMax,
       "rmonLAN2PortGetOutOctetsLo": rmonLAN2PortGetOutOctetsLo,
       "rmonLAN2PortGetOutOctetsHi": rmonLAN2PortGetOutOctetsHi,
       "rmonLAN2PortGetOutUnicasts": rmonLAN2PortGetOutUnicasts,
       "rmonLAN2PortGetExcessive": rmonLAN2PortGetExcessive,
       "rmonLAN2PortGetOutMulticasts": rmonLAN2PortGetOutMulticasts,
       "rmonLAN2PortGetOutBroadcasts": rmonLAN2PortGetOutBroadcasts,
       "rmonLAN2PortGetSingle": rmonLAN2PortGetSingle,
       "rmonLAN2PortGetOutPause": rmonLAN2PortGetOutPause,
       "rmonLAN2PortGetInPause": rmonLAN2PortGetInPause,
       "rmonLAN2PortGetMultiple": rmonLAN2PortGetMultiple,
       "rmonLAN2PortGetUndersize": rmonLAN2PortGetUndersize,
       "rmonLAN2PortGetFragments": rmonLAN2PortGetFragments,
       "rmonLAN2PortGetOversize": rmonLAN2PortGetOversize,
       "rmonLAN2PortGetJabber": rmonLAN2PortGetJabber,
       "rmonLAN2PortGetInMACRcvErr": rmonLAN2PortGetInMACRcvErr,
       "rmonLAN2PortGetInFCSErr": rmonLAN2PortGetInFCSErr,
       "rmonLAN2PortGetCollisions": rmonLAN2PortGetCollisions,
       "rmonLAN2PortGetLate": rmonLAN2PortGetLate,
       "rmonLAN3Port": rmonLAN3Port,
       "rmonLAN3PortGetInGoodOctetsLo": rmonLAN3PortGetInGoodOctetsLo,
       "rmonLAN3PortGetInGoodOctetsHi": rmonLAN3PortGetInGoodOctetsHi,
       "rmonLAN3PortGetInBadOctets": rmonLAN3PortGetInBadOctets,
       "rmonLAN3PortGetOutFCSErr": rmonLAN3PortGetOutFCSErr,
       "rmonLAN3PortGetInUnicasts": rmonLAN3PortGetInUnicasts,
       "rmonLAN3PortGetDeferred": rmonLAN3PortGetDeferred,
       "rmonLAN3PortGetInBroadcasts": rmonLAN3PortGetInBroadcasts,
       "rmonLAN3PortGetInMulticasts": rmonLAN3PortGetInMulticasts,
       "rmonLAN3PortGetOctets64": rmonLAN3PortGetOctets64,
       "rmonLAN3PortGetOctets127": rmonLAN3PortGetOctets127,
       "rmonLAN3PortGetOctets255": rmonLAN3PortGetOctets255,
       "rmonLAN3PortGetOctets511": rmonLAN3PortGetOctets511,
       "rmonLAN3PortGetOctets1023": rmonLAN3PortGetOctets1023,
       "rmonLAN3PortGetOctetsMax": rmonLAN3PortGetOctetsMax,
       "rmonLAN3PortGetOutOctetsLo": rmonLAN3PortGetOutOctetsLo,
       "rmonLAN3PortGetOutOctetsHi": rmonLAN3PortGetOutOctetsHi,
       "rmonLAN3PortGetOutUnicasts": rmonLAN3PortGetOutUnicasts,
       "rmonLAN3PortGetExcessive": rmonLAN3PortGetExcessive,
       "rmonLAN3PortGetOutMulticasts": rmonLAN3PortGetOutMulticasts,
       "rmonLAN3PortGetOutBroadcasts": rmonLAN3PortGetOutBroadcasts,
       "rmonLAN3PortGetSingle": rmonLAN3PortGetSingle,
       "rmonLAN3PortGetOutPause": rmonLAN3PortGetOutPause,
       "rmonLAN3PortGetInPause": rmonLAN3PortGetInPause,
       "rmonLAN3PortGetMultiple": rmonLAN3PortGetMultiple,
       "rmonLAN3PortGetUndersize": rmonLAN3PortGetUndersize,
       "rmonLAN3PortGetFragments": rmonLAN3PortGetFragments,
       "rmonLAN3PortGetOversize": rmonLAN3PortGetOversize,
       "rmonLAN3PortGetJabber": rmonLAN3PortGetJabber,
       "rmonLAN3PortGetInMACRcvErr": rmonLAN3PortGetInMACRcvErr,
       "rmonLAN3PortGetInFCSErr": rmonLAN3PortGetInFCSErr,
       "rmonLAN3PortGetCollisions": rmonLAN3PortGetCollisions,
       "rmonLAN3PortGetLate": rmonLAN3PortGetLate,
       "rmonLAN4Port": rmonLAN4Port,
       "rmonLAN4PortGetInGoodOctetsLo": rmonLAN4PortGetInGoodOctetsLo,
       "rmonLAN4PortGetInGoodOctetsHi": rmonLAN4PortGetInGoodOctetsHi,
       "rmonLAN4PortGetInBadOctets": rmonLAN4PortGetInBadOctets,
       "rmonLAN4PortGetOutFCSErr": rmonLAN4PortGetOutFCSErr,
       "rmonLAN4PortGetInUnicasts": rmonLAN4PortGetInUnicasts,
       "rmonLAN4PortGetDeferred": rmonLAN4PortGetDeferred,
       "rmonLAN4PortGetInBroadcasts": rmonLAN4PortGetInBroadcasts,
       "rmonLAN4PortGetInMulticasts": rmonLAN4PortGetInMulticasts,
       "rmonLAN4PortGetOctets64": rmonLAN4PortGetOctets64,
       "rmonLAN4PortGetOctets127": rmonLAN4PortGetOctets127,
       "rmonLAN4PortGetOctets255": rmonLAN4PortGetOctets255,
       "rmonLAN4PortGetOctets511": rmonLAN4PortGetOctets511,
       "rmonLAN4PortGetOctets1023": rmonLAN4PortGetOctets1023,
       "rmonLAN4PortGetOctetsMax": rmonLAN4PortGetOctetsMax,
       "rmonLAN4PortGetOutOctetsLo": rmonLAN4PortGetOutOctetsLo,
       "rmonLAN4PortGetOutOctetsHi": rmonLAN4PortGetOutOctetsHi,
       "rmonLAN4PortGetOutUnicasts": rmonLAN4PortGetOutUnicasts,
       "rmonLAN4PortGetExcessive": rmonLAN4PortGetExcessive,
       "rmonLAN4PortGetOutMulticasts": rmonLAN4PortGetOutMulticasts,
       "rmonLAN4PortGetOutBroadcasts": rmonLAN4PortGetOutBroadcasts,
       "rmonLAN4PortGetSingle": rmonLAN4PortGetSingle,
       "rmonLAN4PortGetOutPause": rmonLAN4PortGetOutPause,
       "rmonLAN4PortGetInPause": rmonLAN4PortGetInPause,
       "rmonLAN4PortGetMultiple": rmonLAN4PortGetMultiple,
       "rmonLAN4PortGetUndersize": rmonLAN4PortGetUndersize,
       "rmonLAN4PortGetFragments": rmonLAN4PortGetFragments,
       "rmonLAN4PortGetOversize": rmonLAN4PortGetOversize,
       "rmonLAN4PortGetJabber": rmonLAN4PortGetJabber,
       "rmonLAN4PortGetInMACRcvErr": rmonLAN4PortGetInMACRcvErr,
       "rmonLAN4PortGetInFCSErr": rmonLAN4PortGetInFCSErr,
       "rmonLAN4PortGetCollisions": rmonLAN4PortGetCollisions,
       "rmonLAN4PortGetLate": rmonLAN4PortGetLate,
       "rmonModuleGroup": rmonModuleGroup}
)
